import sys
from PyQt4 import QtCore, QtGui

sys.path.insert(0, 'modules')

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
