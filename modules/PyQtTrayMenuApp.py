import sys
from PyQt4 import QtCore, QtGui

class App:

    def __init__(self):
        pass

    def run(self):
        w = QtGui.QWidget()

        # TODO Check config

        # TODO Create TrayIcon

        sys.exit(QtGui.qApp.exec_())
