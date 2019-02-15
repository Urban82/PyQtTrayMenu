import sys
from PyQt5 import QtCore, QtWidgets

import PyQtTrayMenuConfig
import PyQtTrayMenuGui

class App:
    __config = None
    __trayIcon = None

    def __init__(self):
        pass

    def run(self):
        w = QtWidgets.QWidget()

        # Check config
        self.__config = PyQtTrayMenuConfig.Config(QtWidgets.qApp.arguments()[1:])

        # Create TrayIcon
        self.__trayIcon = PyQtTrayMenuGui.TrayIcon(w)
        self.__trayIcon.reloadConfig.connect(self.reloadConfig)
        self.__trayIcon.readConfig(self.__config.menu())
        self.__trayIcon.show()

        sys.exit(QtWidgets.qApp.exec_())

    def reloadConfig(self):
        self.__config.readConfig()
        self.__trayIcon.readConfig(self.__config.menu())
