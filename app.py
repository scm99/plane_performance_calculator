from PyQt6.QtWidgets import QApplication, QMainWindow
from view import UiForm
import sys
import logging

# Configure the logging system 
logging.basicConfig(filename ='PerformancesAvion.log', 
                    level = logging.DEBUG,
                    format = '%(levelname)s: %(asctime)s: %(message)s') 

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception

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