import os
import yeelight
from time import sleep
from day_or_night import isNight

def main():
    host = "192.168.0.174"
    lightbulb = yeelight.Bulb("192.168.0.136")

    while True:
        resp = os.system("ping -c 1 " + host)
        if resp == 0 and isNight():
            lightbulb.turn_on()
        sleep(5)

if __name__ == "__main__":
    main()
    

