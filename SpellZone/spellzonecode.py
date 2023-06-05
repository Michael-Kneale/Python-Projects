from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("SpellZone1.ui")

dlg.show()
app.exec()
