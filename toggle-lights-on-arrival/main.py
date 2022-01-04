import os
import yeelight
from time import sleep
from day_or_night import isNight

#Le script vérifie si je suis connecté au réseau, puis si j'étais connecté 5 secondes avant
#S'il fait nuit, il allume la lumière
#S'il fait jour, il l'éteint
def main():
    host = "192.168.0.184"
    lightbulb = yeelight.Bulb("192.168.0.136") #IP de mon tel
    isAlreadyHere = False

    while True:
        resp = os.system("ping -c 1 " + host)
        if resp == 0 and isNight() and not isAlreadyHere:
            isAlreadyHere = True
            lightbulb.turn_on()
        else:
            isAlreadyHere = False

        if not isNight():
            lightbulb.turn_off()
        sleep(5)

if __name__ == "__main__":
    main()
    

