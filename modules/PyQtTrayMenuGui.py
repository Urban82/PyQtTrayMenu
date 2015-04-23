import sys
from PyQt4 import QtCore, QtGui

def critical(msg, err = None, exit_val = 1):
    if err:
        m1 = "{0}: {1}".format(msg, err)
        m2 = "{0}\n{1}".format(msg, err)
    else:
        m1 = msg
        m2 = msg
    QtCore.qCritical("PyQtTrayMenu.py: error: {0}".format(m1));
    w = QtGui.QWidget()
    QtGui.QMessageBox.critical(w, "PyQtTrayMenu", m2)
    sys.exit(exit_val)

def warning(msg, err = None):
    if err:
        m1 = "{0}: {1}".format(msg, err)
        m2 = "{0}\n{1}".format(msg, err)
    else:
        m1 = msg
        m2 = msg
    QtCore.qWarning("PyQtTrayMenu.py: warning: {0}".format(m1));
    w = QtGui.QWidget()
    QtGui.QMessageBox.warning(w, "PyQtTrayMenu", m2)

def info(msg, err = None):
    if err:
        m1 = "{0}: {1}".format(msg, err)
        m2 = "{0}\n{1}".format(msg, err)
    else:
        m1 = msg
        m2 = msg
    QtCore.qDebug("PyQtTrayMenu.py: info: {0}".format(m1));
    w = QtGui.QWidget()
    QtGui.QMessageBox.information(w, "PyQtTrayMenu", m2)
