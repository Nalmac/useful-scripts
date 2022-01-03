import ephem
import time

def isNight():
    home = ephem.Observer()
    home.lat = "47.39484"
    home.lon = "0.70398"

    next_sunrise    = home.next_rising(ephem.Sun()).datetime()
    next_sunset     = home.next_setting(ephem.Sun()).datetime()

    if next_sunrise <= next_sunset:
        return True
    return False

