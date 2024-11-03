from inverter.goodwe import *
from datetime import datetime
import pandas as pd
from currency_converter import CurrencyConverter

import logging
import time
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fve-report', 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fve-report', 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

logging.basicConfig(level=logging.DEBUG)

from waveshare_epd import epd2in13_V2
from PIL import Image,ImageDraw,ImageFont

class OTE:
    def __init__(self):
        self.ote = pd.read_csv('data/output.csv', index_col=0)

    def __str__(self):
        return f"OTE:\t{self.get_actual_price_czk():.0f} Kc/MW  {self.get_actual_price_eur():.2f} EUR/MW"
        # return f"OTE:\t{self.get_actual_price_czk():.0f} Kc/MW"

    def get_actual_price_eur(self):
        return self.ote.loc[datetime.now().hour, 'price']

    def get_actual_price_czk(self):
        return CurrencyConverter().convert(self.get_actual_price_eur(), 'EUR', 'CZK')


class Inverter:
    def __init__(self):
        self.refresh()

    def refresh(self):
        self.goodwe = GoodweInverter()
        self.solar = self.goodwe.get_pv()
        self.bat_W = self.goodwe.get_batteries_flow()
        self.bat_per = self.goodwe.get_batteries_soc()
        self.grid = self.goodwe.get_power_flow()
        self.consumption = self.goodwe.get_home_consumption()

    def __str__(self):
        return f"PV: \t{self.solar} W\n" \
               f"Bat:\t{self.bat_W} W  {self.bat_per} %\n" \
               f"Grid:\t{self.grid} W\n" \
               f"Dum:\t{self.consumption} W\n"

def update_displayed_data(inverter, ote):
    logging.info("epd2in13_V2 Demo")

    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)

    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    draw.text((20, 0), f'PV: {inverter.solar} W', font=font24, fill=0)
    draw.text((20, 24), f'Bat: {inverter.bat_W} W  {inverter.bat_per} %', font=font24, fill=0)
    draw.text((20, 48), f'Grid: {inverter.grid} W', font=font24, fill=0)
    draw.text((20, 72), f'Dum: {inverter.consumption} W', font=font24, fill=0)
    draw.text((20, 96), f'OTE: {ote.get_actual_price_czk():.0f} Kc/MW  {ote.get_actual_price_eur():.2f} EUR/MW', font=font24, fill=0)
    epd.display(epd.getbuffer(image))

    logging.info("Goto Sleep...")
    epd.sleep()

def main():
    try:
        print(f'libdir: {libdir}')
        ote = OTE()
        inverter = Inverter()

        while (True):
            inverter.refresh()
            update_displayed_data(inverter, ote)
            time.sleep(10*60)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13_V2.epdconfig.module_exit(cleanup=True)
        exit()

if __name__ == "__main__":
    main()
