from PyQt5.QtWidgets import QMessageBox, QDialog
from GUI import appGUI
from plotter import Plotter
import sys

class App():
    def __init__(self):
        self.gui, self.guiApp, self.FunctionPlotter = appGUI()
        self.gui.btn1.clicked.connect(self.callPlotter)
        self.FunctionPlotter.show()
        
        
    def callPlotter(self):
        function = self.gui.txt1.text()
        minValue = self.gui.txt2.text()
        maxValue = self.gui.txt3.text()
        try:
            plotter = Plotter(function, minValue, maxValue)
            plotter.plotFunction()
        except ValueError as error:
            error = error.args[0]
            self.showErrorMessage(error)

            # reset values for another input
            self.gui.txt1.setText("")
            self.gui.txt2.setText("")
            self.gui.txt3.setText("")
            return
        
    def showErrorMessage(self, error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    app = App()
    sys.exit(app.guiApp.exec_())