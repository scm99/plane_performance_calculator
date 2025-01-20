from model import PerformanceGeneratorDR400, PerformanceGeneratorAquila
from data.aerodromes import Aerodrome
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt

class Controller:
    
    def __init__(self, interface):
        self.interface = interface

    def run(self):
        
        # Collect data
        generators, state = self.state_collector()
        if not generators and not state:
            return
        
        performances = ['take_off', 'landing']
        warning = False
        for i, performance in enumerate(performances):
            
            # Compute results for Take Off from the Model
            state['mode'] = performance
            distances = self.calculate_performance(generators, state)

            # Add Take Off performances to table of results
            for j in range(2):
                if distances[j] == '-':
                    warning = True
                item = QTableWidgetItem(str(distances[j]) + ' m')
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.interface.tableWidget.setItem(j, i, item)
                
        if warning:
            error = f"""Les valeurs introduits sont en dehors de la gamme de valeurs de calcule de la performance de l'avion."""
            msgBox = QMessageBox(QMessageBox.Icon.Critical, 'Erreur - Valeur de la Masse', error)
            msgBox.exec()
        
        self.wind_button_clicked = False
        
        
    def insert_aerodrome_information(self, name):
        
        aerodrome = Aerodrome(name)
        self.interface.alt_editor.setText(str(aerodrome.altitude))
        if aerodrome.herbe:
            self.interface.herbe.setChecked(True)
            self.interface.dur.setChecked(False)
        else:
            self.interface.dur.setChecked(True)
            self.interface.herbe.setChecked(False)
    
    def state_collector(self):
        
        # Aircraft performances generator
        # Aquila
        if self.interface.aquila.isChecked():
            generator = PerformanceGeneratorAquila()
        # DR400
        elif self.interface.dr400_1.isChecked():
            cv = '160'
            generator = PerformanceGeneratorDR400(cv)
            
        elif self.interface.dr400_2.isChecked():
            cv = '180'
            generator = PerformanceGeneratorDR400(cv)
        
        # Collect state
        state = {}
        error = ""
        state['mass'], aux = self.line_edit_collector(self.interface.mass_editor, ['mass', 'kg'])
        error += aux
        state['altitude'], aux = self.line_edit_collector(self.interface.alt_editor, ['altitude', 'ft'])
        error += aux
        state['temperature'], aux = self.line_edit_collector(self.interface.temp_editor, ['temperature', 'ºC'])
        error += aux
        state['wind'], aux = self.line_edit_collector(self.interface.wind_editor, ['wind', 'kt'])
        error += aux
        state['herbe'] = False
        if self.interface.herbe.isChecked():
            state['herbe'] = True
        
        if error:
            error = error + '\nVeuillez introduire des valeurs cohérentes pour les variables ci-dessus.'
            msgBox = QMessageBox(QMessageBox.Icon.Critical, 'Erreur - Valeurs Introduits', error)
            msgBox.exec()
            return False, False
        
        if state['mass'] > generator.max_mass:
            error = f"""La masse = {int(state['mass'])} kg dépasse la masse maximale de {generator.max_mass} kg pour le modèle choisi.
            \nVeuillez introduire une valeur cohérente pour la masse."""
            msgBox = QMessageBox(QMessageBox.Icon.Critical, 'Erreur - Valeur de la Masse', error)
            msgBox.exec()
            return False, False
        
        if state['mass'] < generator.min_mass:
            error = f"""La masse = {int(state['mass'])} kg est inférieure à la masse à vide {generator.min_mass} kg du modèle choisi.
            \nVeuillez introduire une valeur cohérente pour la masse."""
            msgBox = QMessageBox(QMessageBox.Icon.Critical, 'Erreur - Valeur de la Masse', error)
            msgBox.exec()
            return False, False
        
            
        return generator, state
        
            
    def line_edit_collector(self, line_editor, labels):
            
        # Collect Mass
        variable = line_editor.text()
        try:
            variable = float(variable)
            return variable, ""
        except:
            error = f"Le valeur {labels[0]} = {variable} {labels[1]} n'est pas valable.\n"
            return None, error
        
        
    def calculate_performance(self, generator, state):
        
        # Calculate distances
        partial_distance, total_distance = generator.calculate_distances(
            state['mode'],
            state['altitude'],
            state['temperature'],
            state['mass'],
            state['herbe'],
            state['wind']
            )
        
        return partial_distance, total_distance
        
        
    def get_wind_information(self):
        
        message = """Un vent positive (+) représente un vent de face au décollage ou atterrissage dans l'axe de la piste.
                    \nUn vent négative (-) correspond à un vent arrière."""
        
        msgBox = QMessageBox(QMessageBox.Icon.NoIcon, 'Direction du Vent', message)
        msgBox.exec()