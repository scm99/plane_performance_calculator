from PyQt6.QtWidgets import QApplication, QMainWindow
from view import UiForm
import sys

try:
    
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
    print(e)