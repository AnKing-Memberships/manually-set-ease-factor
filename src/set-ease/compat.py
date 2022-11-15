from aqt import mw
from aqt.browser import Browser
from aqt.gui_hooks import browser_will_show, profile_did_open


def setup_compat_aliases():
    def on_browser_will_show(browser: Browser):
        add_compat_alias(browser, "selected_cards", "selectedCards")

    browser_will_show.append(on_browser_will_show)
    
    def on_profile_did_open():
        add_compat_alias(mw.col, "get_card", "getCard")
    profile_did_open.append(on_profile_did_open)


def add_compat_alias(namespace, new_name, old_name):
    if new_name not in dir(namespace):
        setattr(namespace, new_name, getattr(namespace, old_name))
        return True

    return False
