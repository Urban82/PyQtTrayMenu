## Base configuration
The root element in the JSON file must contains the following keys: **app**, **version** and **menu**.

### `app` key
This key must contains the string `"PyQtTrayMenu"`.

### `version` key
This key is intended for future enhancements on the configuration format. The actual version is `1`.

### `menu` key
This key contains the menu. It is a JSON object with the following mandatory keys: **name**, **icon** and **items** keys.

#### `menu.name` key
This key contains the name for this menu: it will be showed in the tool-tip of the SysTray icon.

#### `menu.icon` key
This key contains the path of the icon that will be showed in the SysTray for this menu.

#### `menu.items` key
This key contains a JSON array of menu items.

## Menu items
Each menu item is formed as a JSON object with at least a **name** key. It can also contains a **icon** key.

There are two type of menu item: **sub-menu** and **command** items.

### `name` key
This key contains the name showed in the pop-up menu for this item.

### `icon` key
This key contains the path of the icon that will be showed in the pop-up menu for this item.

### Sub-menu item
A sub-menu item must contains the key **items**.

#### `items` key
This key contains the items in this sub-menu. It is a JSON array of menu items.

### Command item
A command item must contains the key **command**.

#### `command` key
This key contains the command to execute when this menu item is clicked.
It can be a string with the command or an array with a string for the command and each parameters.

## Example
The following configuration create a pop-up menu with two items:
* A command item named **Konsole** that run the command `konsole`.
* A sub-menu item with 3 items that run `kdialog` with a different message.

```json
{
    "app" : "PyQtTrayMenu",
    "version" : 1,
    "menu" : {
        "name" : "PyQtTrayMenu",
        "icon" : "/usr/share/icons/oxygen/32x32/apps/preferences-desktop-launch-feedback.png",
        "items" : [
            {
                "name" : "Konsole",
                "icon" : "/usr/share/icons/oxygen/32x32/apps/utilities-terminal.png",
                "command" : "konsole"
            },
            {
                "name" : "Altro",
                "icon" : "/usr/share/icons/oxygen/32x32/actions/edit-image-face-recognize.png",
                "items" : [
                    { "name" : "Item 1", "command" : ["kdialog", "--msgbox", "Item 1"] },
                    { "name" : "Item 2", "command" : ["kdialog", "--msgbox", "Item 2"] },
                    { "name" : "Item 3", "command" : ["kdialog", "--msgbox", "Item 3"] }
                ]
            }
        ]
    }
}
```
