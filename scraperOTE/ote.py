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