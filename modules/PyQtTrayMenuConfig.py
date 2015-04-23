import argparse
import sys
import json
from PyQt4 import QtCore

import PyQtTrayMenuGui

class Config:
    __configFileName = None
    __configFile = None
    __config = None
    __currentConfigVersion = 1

    def __init__(self, args):
        parser = argparse.ArgumentParser(description='Create a SysTray icon with a configurable menu')
        parser.add_argument('-c', '--create', action='store_true', dest='create', default=False, help='create configuration file')
        parser.add_argument('filename', metavar='<config file>', action='store', help='path of the configuration file')
        options = parser.parse_args(args)
        self.__configFileName = options.filename
        if options.create:
            # TODO
            PyQtTrayMenuGui.warning("Not implemented yet!")
            sys.exit(0)
        else:
            try:
                self.__configFile = open(self.__configFileName, "r")
                self.__config = json.loads(self.__configFile.read())
                self.__check_config()
            except OSError as ex:
                PyQtTrayMenuGui.critical("Unable to read config file \"{0}\"".format(self.__configFileName), ex.strerror, 1)
            except ValueError as ex:
                PyQtTrayMenuGui.critical("Unable to read config file \"{0}\"".format(self.__configFileName), str(ex), 1)
            except:
                PyQtTrayMenuGui.critical("Unable to read config file \"{0}\"".format(self.__configFileName), sys.exc_info()[0], 1)

    def __check_config(self):
        if not 'app' in self.__config:
            raise ValueError("Invalid configuration JSON: missing key \"app\"")
        if type(self.__config['app']) != type("") or self.__config['app'] != "PyQtTrayMenu":
            raise ValueError("Invalid configuration JSON: wrong value \"{0}\" for key \"app\"".format(self.__config['app']))
        if not 'version' in self.__config:
            raise ValueError("Invalid configuration JSON: missing key \"version\"")
        if type(self.__config['version']) != type(0):
            raise ValueError("Invalid configuration JSON: invalid value \"{0}\" for key \"version\"".format(self.__config['version']))
        if self.__config['version'] != self.__currentConfigVersion:
            if self.__config['version'] < self.__currentConfigVersion:
                self.__update_config()
            else:
                raise ValueError("Invalid configuration JSON: found newer version {0} (current is {1})".format(self.__config['version'], self.__currentConfigVersion))
        if not 'menu' in self.__config:
            raise ValueError("Invalid configuration JSON: missing key \"menu\"")
        if type(self.__config['menu']) != type({}):
            raise ValueError("Invalid configuration JSON: invalid value for key \"menu\"")
        if not 'name' in self.__config['menu']:
            raise ValueError("Invalid configuration JSON: missing key \"menu.name\"")
        if type(self.__config['menu']['name']) != type(""):
            raise ValueError("Invalid configuration JSON: invalid value for key \"menu.name\"")
        if not 'icon' in self.__config['menu']:
            raise ValueError("Invalid configuration JSON: missing key \"menu.icon\"")
        if type(self.__config['menu']['icon']) != type(""):
            raise ValueError("Invalid configuration JSON: invalid value for key \"menu.icon\"")
        if not 'items' in self.__config['menu']:
            raise ValueError("Invalid configuration JSON: missing key \"menu.items\"")
        if type(self.__config['menu']['items']) != type([]):
            raise ValueError("Invalid configuration JSON: invalid value for key \"menu.items\"")
        i = 0
        for item in self.__config['menu']['items']:
            self.__check_config_item(item, "menu.items[{0}]".format(i))
            i = i + 1

    def __check_config_item(self, item, path):
        if not 'name' in item:
            raise ValueError("Invalid configuration JSON: missing key \"{0}.name\"".format(path))
        if type(item['name']) != type(""):
            raise ValueError("Invalid configuration JSON: invalid value \"{1}\" for key \"{0}.name\"".format(path, item['name']))
        if 'icon' in item and type(item['icon']) != type(""):
            raise ValueError("Invalid configuration JSON: invalid value \"{1}\" for key \"{0}.icon\"".format(path, item['icon']))
        if 'command' in item and 'items' in item:
            raise ValueError("Invalid configuration JSON: found both keys \"{0}.command\" and \"{0}.items\"".format(path))
        if not 'command' in item and not 'items' in item:
            raise ValueError("Invalid configuration JSON: missing key \"{0}.command\" or \"{0}.items\"".format(path))
        if 'command' in item and type(item['command']) != type("") and type(item['command']) != type([]):
            raise ValueError("Invalid configuration JSON: invalid value \"{1}\" for key \"{0}.command\"".format(path, item['command']))
        if 'items' in item:
            if type(item['items']) != type([]):
                raise ValueError("Invalid configuration JSON: invalid value for key \"{0}.items\"".format(path))
            i = 0
            for subitem in item['items']:
                self.__check_config_item(subitem, "{0}.items[{1}]".format(path, i))
                i = i + 1

    def __update_config(self):
        # TODO
        PyQtTrayMenuGui.warning("Not implemented yet!")

    def menu(self):
        return self.__config['menu']
