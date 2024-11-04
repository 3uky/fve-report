import os
import sys
import logging

from display.lib.waveshare_epd import epd2in13_V2
from PIL import Image,ImageDraw,ImageFont

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'display', 'pic')

logging.basicConfig(level=logging.DEBUG)


class Display:
    @staticmethod
    def update(inverter, ote):
        logging.info("epd2in13_V2 display init")
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
