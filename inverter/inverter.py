from inverter.goodwe import GoodweInverter


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
