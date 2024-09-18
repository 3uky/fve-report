from inverter.goodwe import *
from datetime import datetime
import pandas as pd
from currency_converter import CurrencyConverter

def print_invertor_report(inverter):
    print(f"PV: \t{inverter.get_pv()} W")
    print(f"Bat:\t{inverter.get_batteries_flow()} W  {inverter.get_batteries_soc()} %")
    print(f"Grid:\t{inverter.get_power_flow()} W")
    print(f"Dum:\t{inverter.get_home_consumption()} W")

def print_ote_actual_price():
    hour = datetime.now().hour
    ote = pd.read_csv('data/output.csv', index_col=0)
    price_EUR = ote.loc[hour, 'price']
    price_CZK = CurrencyConverter().convert(price_EUR, 'EUR', 'CZK')
    print(f"OTE:\t{price_EUR:.2f} EUR/MW  {price_CZK:.0f} Kc/MW")


def main():
    print_invertor_report(Inverter())
    print_ote_actual_price()


if __name__ == "__main__":
    main()