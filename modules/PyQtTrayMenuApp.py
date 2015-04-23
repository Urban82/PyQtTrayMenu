import sys
from PyQt4 import QtCore, QtGui

import PyQtTrayMenuConfig

class App:
    __config = None

    def __init__(self):
        pass

    def run(self):
        w = QtGui.QWidget()

        # Check config
        self.__config = PyQtTrayMenuConfig.Config(QtGui.qApp.arguments()[1:])

        # TODO Create TrayIcon

        sys.exit(QtGui.qApp.exec_())
