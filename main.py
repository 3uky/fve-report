from inverter.goodwe import *
from datetime import datetime
import pandas as pd
from currency_converter import CurrencyConverter

import time

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


def main():
    try:
        ote = OTE()
        inverter = Inverter()

        while(True):
            inverter.refresh()
            print(str(inverter) + str(ote), flush=True)
            time.sleep(10)

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()