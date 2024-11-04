import logging
import time

from display.display import Display
from inverter.inverter import Inverter
from scraperOTE.ote import OTE


def main():
    try:
        ote = OTE()
        inverter = Inverter()
        display = Display()

        while (True):
            inverter.refresh()
            display.update(inverter, ote)
            time.sleep(10*60)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
