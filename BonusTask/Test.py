from PyQt6.QtWidgets import QApplication
from Uiext import EmployeeExt

app = QApplication([])
myui = EmployeeExt()
myui.showWindow()
app.exec()