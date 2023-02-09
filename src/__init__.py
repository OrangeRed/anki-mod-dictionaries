from aqt import gui_hooks

from .src import main_menu, browser  # editor

gui_hooks.main_window_did_init.append(main_menu.insert_menu_item)
gui_hooks.browser_menus_did_init.append(browser.insert_menu_item)
# gui_hooks.browser_menus_did_init.append(editor.insert_menu_item)
