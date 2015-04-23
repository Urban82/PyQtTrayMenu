import sys
import os
from PyQt4 import QtCore, QtGui

dir = os.path.dirname(sys.argv[0])
if len(dir) == 0:
    dir = 'modules'
else:
    dir = dir + '/modules'
sys.path.insert(0, dir)

app = QtGui.QApplication(sys.argv)

try:
    import PyQtTrayMenuApp
except ImportError as e:
    w = QtGui.QWidget()
    QtCore.qCritical("PyQtTrayMenu.py: error: Cannot find PyQtTrayMenu modules: {0}".format(e.args));
    QtGui.QMessageBox.critical(w, "PyQtTrayMenu", "Cannot find PyQtTrayMenu modules!")
    sys.exit(1)

myApp = PyQtTrayMenuApp.App()
myApp.run()
