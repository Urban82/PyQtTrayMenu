import sys
import subprocess
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

class TrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, menu, parent = None):
        QtGui.QSystemTrayIcon.__init__(self, parent)
        self.setToolTip(menu['name'])
        self.setIcon(QtGui.QIcon(menu['icon']))

        m = QtGui.QMenu(parent)

        for item in menu['items']:
            self.__scan_menu(m, item)

        m.addSeparator()
        exitAction = m.addAction("Exit")
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.activated.connect(lambda: self.contextMenu().popup(QtGui.QCursor.pos()))

        self.setContextMenu(m)
        self.show()

    def __scan_menu(self, m, item):
        itemAction = m.addAction(item['name'])
        if 'icon' in item:
            itemAction.setIcon(QtGui.QIcon(item['icon']))
        if 'command' in item:
            itemAction.triggered.connect(lambda: self.__menu_clicked(item))
        elif 'items' in item:
            m2 = QtGui.QMenu(m)

            for subitem in item['items']:
                self.__scan_menu(m2, subitem)

            itemAction.setMenu(m2)

    def __menu_clicked(self, item):
        if 'command' in item:
            subprocess.Popen(item['command'])
