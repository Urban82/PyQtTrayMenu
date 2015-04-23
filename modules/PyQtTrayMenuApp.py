import sys
from PyQt4 import QtCore, QtGui

import PyQtTrayMenuConfig
import PyQtTrayMenuGui

class App:
    __config = None
    __trayIcon = None

    def __init__(self):
        pass

    def run(self):
        w = QtGui.QWidget()

        # Check config
        self.__config = PyQtTrayMenuConfig.Config(QtGui.qApp.arguments()[1:])

        # Create TrayIcon
        self.__trayIcon = PyQtTrayMenuGui.TrayIcon(self.__config.menu(), w)

        sys.exit(QtGui.qApp.exec_())
