import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

dir = os.path.dirname(sys.argv[0])
if len(dir) == 0:
    dir = 'modules'
else:
    dir = dir + '/modules'
sys.path.insert(0, dir)

app = QtWidgets.QApplication(sys.argv)

try:
    import PyQtTrayMenuApp
except ImportError as e:
    w = QtWidgets.QWidget()
    QtCore.qCritical("PyQtTrayMenu.py: error: Cannot find PyQtTrayMenu modules: {0}".format(e.args));
    QtGui.QMessageBox.critical(w, "PyQtTrayMenu", "Cannot find PyQtTrayMenu modules!")
    sys.exit(1)

myApp = PyQtTrayMenuApp.App()
myApp.run()
