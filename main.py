from inverter.goodwe import *
from datetime import datetime
import pandas as pd
from currency_converter import CurrencyConverter


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
        self.inverter = GoodweInverter()

    def __str__(self):
        return f"PV: \t{self.inverter.get_pv()} W\n" \
               f"Bat:\t{self.inverter.get_batteries_flow()} W  {self.inverter.get_batteries_soc()} %\n" \
               f"Grid:\t{self.inverter.get_power_flow()} W\n" \
               f"Dum:\t{self.inverter.get_home_consumption()} W\n"


def main():
    inverter = Inverter()
    ote = OTE()

    print(str(inverter) + str(ote))


if __name__ == "__main__":
    main()