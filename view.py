from PyQt6 import QtCore, QtGui, QtWidgets
from controller import Controller


class UiForm(object):
    
    def setupUi(self, Window):
        
        # Settings of window
        Window.setObjectName("Window")
        Window.resize(650, 770)
        Window.setMinimumSize(QtCore.QSize(650, 750))
        Window.setMaximumSize(QtCore.QSize(650, 750))
        
        # Controller 
        self.controller = Controller(self)
        
        # Set Title
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Form", "Calculatrice de Performances"))
        
        # Mass Editor
        self.setup_mass(Window)
        
        # Temperature Editor
        self.setup_temperature(Window)
        
        # Wind Editor
        self.setup_wind(Window)
        
        # Wind Information Button
        self.setup_wind_information_button(Window)
        
        # Labels
        self.setup_text_labels(Window)
        
        # Altitude Editor
        self.setup_altitude(Window)
        
        # Runway Type Buttons
        self.setup_runway_type_buttons(Window)
        
        # Setup the Airplane
        self.setup_airplane_type(Window)
        
        # Setup Aerodrome Combo box
        self.setup_aerodrome_combo_box(Window)
        
        # Setup Validate Button
        self.setup_validate_button(Window)
        
        # Setup Table for Results
        self.setup_results_table(Window)

        # Connect to Window
        QtCore.QMetaObject.connectSlotsByName(Window)


    def setup_temperature(self, Window):
        
        # Horizontal Layot
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Window)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(190, 280, 81, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # Temperature Label
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        
        # Temperature Line Editor 
        self.temp_editor = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.temp_editor.setText("")
        self.temp_editor.setMaxLength(2)
        self.temp_editor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.temp_editor.setObjectName("temp_editor")
        self.horizontalLayout_2.addWidget(self.temp_editor)
        
        # Units Label
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        
        # Set Labels
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Form", "T:"))
        self.temp_editor.setPlaceholderText(_translate("Form", "17"))
        self.label_4.setText(_translate("Form", "ºC"))
        
        
    def setup_wind(self, Window):
        
        # Horizontal Layout
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=Window)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(350, 280, 101, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        # Wind Label
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        
        # Wind Edit Line
        self.wind_editor = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_3)
        self.wind_editor.setText("")
        self.wind_editor.setMaxLength(3)
        self.wind_editor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wind_editor.setObjectName("wind_editor")
        self.horizontalLayout_3.addWidget(self.wind_editor)
        
        # Units label
        self.label_6 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        
        # Set Labels
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("Form", "Vent:"))
        self.wind_editor.setPlaceholderText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "kt"))
        
    
    def setup_wind_information_button(self, Window):
        
        self.pushButton = QtWidgets.QPushButton(parent=Window)
        self.pushButton.setGeometry(QtCore.QRect(460, 280, 30, 31))
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.controller.get_wind_information)
        
        # Set Label
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "?"))
        
        
    def setup_altitude(self, Window):
        
        # Horizontal Layout
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=Window)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(280, 390, 151, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        # Altitude Label
        self.label_9 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        
        # Altitude Edit Line
        self.alt_editor = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_4)
        self.alt_editor.setText("")
        self.alt_editor.setMaxLength(4)
        self.alt_editor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.alt_editor.setObjectName("alt_editor")
        self.horizontalLayout_4.addWidget(self.alt_editor)
        
        # Unit Label
        self.label_10 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        
        # Set Labels
        _translate = QtCore.QCoreApplication.translate
        self.label_9.setText(_translate("Form", "Altitude:"))
        self.alt_editor.setText(_translate("Form", "460"))
        self.label_10.setText(_translate("Form", "ft"))
        
        
    def setup_mass(self, Window):
        
        # Horizontal Layout
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(parent=Window)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(270, 175, 141, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        
        # Mass Label
        self.label_15 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_9)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        
        # Mass Edit Line
        self.mass_editor = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_9)
        self.mass_editor.setText("")
        self.mass_editor.setMaxLength(4)
        self.mass_editor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mass_editor.setObjectName("mass_editor")
        self.horizontalLayout_9.addWidget(self.mass_editor)
        
        # Units Label
        self.label_16 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_9)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        
        # Set Label
        _translate = QtCore.QCoreApplication.translate
        self.label_15.setText(_translate("Form", "Masse:"))
        self.mass_editor.setPlaceholderText(_translate("Form", "900"))
        self.label_16.setText(_translate("Form", "kg"))
      
        
    def setup_runway_type_buttons(self, Window):
        
        # Horizontal Layout
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(parent=Window)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(450, 370, 161, 70))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        # Runway Type Label
        self.label_11 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        
        # Radio Buttons
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # Asphalt
        self.dur = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_5)
        self.dur.setChecked(True)
        self.dur.setObjectName("dur")
        self.verticalLayout_2.addWidget(self.dur)
        # Grass
        self.herbe = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_5)
        self.herbe.setObjectName("herbe")
        self.verticalLayout_2.addWidget(self.herbe)
        
        # Add to Layout
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        
        # Set Labels
        _translate = QtCore.QCoreApplication.translate
        self.label_11.setText(_translate("Form", "Type de Piste:"))
        self.dur.setText(_translate("Form", "Dur"))
        self.herbe.setText(_translate("Form", "Herbe"))
        
    
    def setup_airplane_type(self, Window):
        
        # Horizontal Layout
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(parent=Window)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(120, 135, 401, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        # DR400 - 160 cv
        self.dr400_1 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_7)
        self.dr400_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.dr400_1.setChecked(True)
        self.dr400_1.setObjectName("dr400_1")
        self.horizontalLayout_7.addWidget(self.dr400_1)
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        
        # DR400 - 180 cv
        self.dr400_2 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_7)
        self.dr400_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.dr400_2.setChecked(True)
        self.dr400_2.setObjectName("dr400_2")
        self.horizontalLayout_7.addWidget(self.dr400_2)
        
        # Aquila button
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        #self.horizontalLayout_7.addItem(spacerItem7)
        self.aquila = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_7)
        self.aquila.setObjectName("aquila")
        self.horizontalLayout_7.addWidget(self.aquila)
        
        # Set Label
        _translate = QtCore.QCoreApplication.translate
        self.dr400_1.setText(_translate("Form", "DR400 - 160 cv"))
        self.dr400_2.setText(_translate("Form", "DR400 - 180 cv"))
        self.aquila.setText(_translate("Form", "Aquila"))
        
    
    def setup_aerodrome_combo_box(self, Window):
        
        # Horizontal Layout
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(parent=Window)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(40, 380, 220, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        # Aerodrome Label
        self.label_12 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        
        # Combo Box
        self.comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox)
        
        # Change Labels
        _translate = QtCore.QCoreApplication.translate
        self.comboBox.setCurrentText(_translate("Form", "Lasbordes"))
        self.comboBox.setItemText(0, _translate("Form", "Lasbordes"))
        self.comboBox.setItemText(1, _translate("Form", "Cahors"))
        self.comboBox.setItemText(2, _translate("Form", "Graulhet"))
        self.comboBox.setItemText(3, _translate("Form", "Albi"))
        self.comboBox.setItemText(4, _translate("Form", "Muret"))
        self.comboBox.setItemText(5, _translate("Form", "Castelsarrasin"))
        self.comboBox.setItemText(6, _translate("Form", "Castelnaudary"))
        self.comboBox.setItemText(7, _translate("Form", "Pamiers"))
        self.comboBox.setItemText(8, _translate("Form", "St. Girons"))
        self.comboBox.setItemText(9, _translate("Form", "Auch"))
        self.comboBox.setItemText(10, _translate("Form", "Blagnac"))
        self.comboBox.setItemText(11, _translate("Form", "Agen"))
        self.comboBox.setItemText(12, _translate("Form", "Gaillac"))
        self.comboBox.setItemText(13, _translate("Form", "Custom"))
        
        
        # Set Label
        _translate = QtCore.QCoreApplication.translate
        self.label_12.setText(_translate("Form", "Aérodrome:"))
        
        # React combobox
        self.comboBox.currentTextChanged.connect(self.controller.insert_aerodrome_information)
        
        
    def setup_results_table(self, Window):
        
        # Results label
        _translate = QtCore.QCoreApplication.translate
        self.label_17 = QtWidgets.QLabel(parent=Window)
        self.label_17.setGeometry(QtCore.QRect(180, 490, 300, 40))
        self.label_17.setWordWrap(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_17.setText(_translate("Form", 'Résultats'))
        
        # Create Table
        self.tableWidget = QtWidgets.QTableWidget(parent=Window)
        self.tableWidget.setGeometry(QtCore.QRect(110, 540, 451, 111))
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(2)
        
        # Add Columns and Rows
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        
        # Add Headers
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        
        # Set Labels
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Distance de Roulement"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Distance Totale"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Décollage"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Atterrissage"))
        
        
    def setup_text_labels(self, Window):
        
        # Données Meteo
        self.label_7 = QtWidgets.QLabel(parent=Window)
        self.label_7.setGeometry(QtCore.QRect(210, 240, 251, 16))
        self.label_7.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        
        # Donnees Aerodrome
        self.label_8 = QtWidgets.QLabel(parent=Window)
        self.label_8.setGeometry(QtCore.QRect(210, 340, 251, 16))
        self.label_8.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        
        # Donnes Avion
        self.label_13 = QtWidgets.QLabel(parent=Window)
        self.label_13.setGeometry(QtCore.QRect(210, 100, 251, 16))
        self.label_13.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        
        # Title Label
        self.label_14 = QtWidgets.QLabel(parent=Window)
        self.label_14.setGeometry(QtCore.QRect(125, 10, 420, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        
        # Disclaimer
        self.label_disclaimer = QtWidgets.QLabel(parent=Window)
        self.label_disclaimer.setGeometry(QtCore.QRect(80, 665, 500, 100))
        self.label_disclaimer.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_disclaimer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_disclaimer.setObjectName("label_13")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_disclaimer.setFont(font)
        
        # Set Labels
        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate("Form", "Saisir les données météorologiques"))
        self.label_8.setText(_translate("Form", "Saisir les données de l\'aérodrome"))
        self.label_13.setText(_translate("Form", "Choisir votre avion"))
        self.label_14.setText(_translate("Form", "Calculatrice de Performances"))
        self.label_disclaimer.setText(_translate("Form", "Disclaimer: Cette application est uniquement destinée à des fins éducatives.\nElle ne remplace pas le manuel de vol ni une préparation adéquate par le pilote.\n\nCrée par: Sara Marques"))
        
        
    def setup_validate_button(self, Window):
        
        # Validate Button
        self.validate_button = QtWidgets.QPushButton(parent=Window)
        self.validate_button.setGeometry(QtCore.QRect(275, 450, 113, 32))
        self.validate_button.setObjectName("validate_button")
        self.validate_button.clicked.connect(self.controller.run)
        
        # Set Label
        _translate = QtCore.QCoreApplication.translate
        self.validate_button.setText(_translate("Form", "Calculer"))
        