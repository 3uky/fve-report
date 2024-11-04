import logging
import time

from display.display import Display
from inverter.goodwe import GoodweInverter as Inverter
from ote.ote import OTE

SLEEP_MIN = 10
SLEEP_SEC = SLEEP_MIN * 60

logging.StreamHandler().setLevel(logging.INFO)


def main():
    try:
        ote = OTE()
        inverter = Inverter()

        while (True):
            inverter.refresh()
            logging.info(f'{inverter}\n{ote}')
            Display.update(inverter, ote)
            time.sleep(SLEEP_SEC)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
