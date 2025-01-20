from PyQt6.QtWidgets import QApplication, QMainWindow
from view import UiForm
import sys
import logging

try:
    # Configure the logging system 
    logging.basicConfig(filename ='PerformancesAvion.log', 
                        level = logging.DEBUG) 
    
    # Generate the app
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QMainWindow()

    # Setup Window
    ui = UiForm()
    ui.setupUi(window)
    window.show()

    # Styling the app
    #app.setStyleSheet(Path('style.qss').read_text())

    # Start the event loop.
    app.exec()
except Exception as e: 
    logging.error(e)