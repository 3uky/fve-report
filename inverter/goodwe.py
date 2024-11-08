from config import args
from pygoodwe import SingleInverter


class GoodweInverter():
    def __init__(self):
        self.refresh()

    def refresh(self):
        self.inverter = self.get_single_inverter()
        self.solar = self.get_pv()
        self.bat_W = self.get_batteries_flow()
        self.bat_per = self.get_batteries_soc()
        self.grid = self.get_power_flow()
        self.consumption = self.get_home_consumption()

    def get_single_inverter(self, args=args):
        inverter = SingleInverter(
                system_id=args.get('gw_station_id', '1'),
                account=args.get('gw_account', 'thiswillnotwork'),
                password=args.get('gw_password', 'thiswillnotwork'),
                )
        inverter.getCurrentReadings()
        return inverter

    def get_pv(self):
        return int(self.inverter.getPVFlow())

    def get_batteries_soc(self):
        return int(self.inverter.get_batteries_soc())

    def get_batteries_flow(self):
        return int(self.inverter.getPVFlow() - self.inverter.getPmeter() - self.inverter.getLoadFlow())

    def get_home_consumption(self):
        return int(self.inverter.getLoadFlow())

    def get_power_flow(self):
        return int(self.inverter.getPmeter())

    def __str__(self):
        return f"PV: \t{self.solar} W\n" \
               f"Bat:\t{self.bat_W} W  {self.bat_per} %\n" \
               f"Grid:\t{self.grid} W\n" \
               f"Dum:\t{self.consumption} W\n"