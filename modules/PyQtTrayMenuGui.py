import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

def critical(msg, err = None, exit_val = 1):
    if err:
        m1 = "{0}: {1}".format(msg, err)
        m2 = "{0}\n{1}".format(msg, err)
    else:
        m1 = msg
        m2 = msg
    QtCore.qCritical("PyQtTrayMenu.py: error: {0}".format(m1))
    w = QtWidgets.QWidget()
    QtGui.QMessageBox.critical(w, "PyQtTrayMenu", m2)
    sys.exit(exit_val)

def warning(msg, err = None):
    if err:
        m1 = "{0}: {1}".format(msg, err)
        m2 = "{0}\n{1}".format(msg, err)
    else:
        m1 = msg
        m2 = msg
    QtCore.qWarning("PyQtTrayMenu.py: warning: {0}".format(m1))
    w = QtWidgets.QWidget()
    QtGui.QMessageBox.warning(w, "PyQtTrayMenu", m2)

def info(msg, err = None):
    if err:
        m1 = "{0}: {1}".format(msg, err)
        m2 = "{0}\n{1}".format(msg, err)
    else:
        m1 = msg
        m2 = msg
    QtCore.qDebug("PyQtTrayMenu.py: info: {0}".format(m1))
    w = QtWidgets.QWidget()
    QtGui.QMessageBox.information(w, "PyQtTrayMenu", m2)

def get_icon(icon):
    if icon[0] == "/":
        return QtGui.QIcon(icon)
    else:
        return QtGui.QIcon.fromTheme(icon)

class TrayIcon(QtWidgets.QSystemTrayIcon):
    __menu = None

    reloadConfig = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, parent)

        self.__menu = QtWidgets.QMenu(parent)
        self.setContextMenu(self.__menu)

        self.activated.connect(self.__activated)

    def readConfig(self, menu):
        self.setToolTip(menu['name'])
        self.setIcon(get_icon(menu['icon']))

        self.__menu.clear()

        for item in menu['items']:
            self.__scan_menu(self.__menu, item)

        self.__menu.addSeparator()
        exitAction = self.__menu.addAction("Exit")
        exitAction.triggered.connect(QtWidgets.qApp.quit)

    def __scan_menu(self, m, item):
        if 'separator' in item:
            m.addSeparator()
            return
        itemAction = m.addAction(item['name'])
        if 'icon' in item:
            itemAction.setIcon(get_icon(item['icon']))
        if 'command' in item:
            itemAction.triggered.connect(lambda: self.__menu_clicked(item))
        elif 'items' in item:
            m2 = QtWidgets.QMenu(m)

            for subitem in item['items']:
                self.__scan_menu(m2, subitem)

            itemAction.setMenu(m2)

    def __activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.MiddleClick:
            self.reloadConfig.emit()
        else:
            self.contextMenu().popup(QtGui.QCursor.pos())

    def __menu_clicked(self, item):
        if 'command' in item:
            subprocess.Popen(item['command'])
