import json
from functools import lru_cache


from config import args
from pygoodwe import SingleInverter


class Inverter():
    def __init__(self):
        self.inverter = self.get_single_inverter()

    def get_single_inverter(self, args=args): #pylint: disable=redefined-outer-name,dangerous-default-value
        inverter = SingleInverter(
                system_id=args.get('gw_station_id', '1'),
                account=args.get('gw_account', 'thiswillnotwork'),
                password=args.get('gw_password', 'thiswillnotwork'),
                )
        inverter.getCurrentReadings()
        return inverter

    def get_pv(self):
        return self.inverter.getPVFlow()

    def get_batteries_soc(self):
        return self.inverter.get_batteries_soc()

    def get_batteries_flow(self):
        return self.inverter.getPVFlow() - self.inverter.getPmeter() - self.inverter.getLoadFlow()

    def get_home_consumption(self):
        return self.inverter.getLoadFlow()

    def get_power_flow(self):
        return self.inverter.getPmeter()


        # battery = inverter.getPVFlow() - inverter.getPmeter() - inverter.getLoadFlow()
    # print(f"PV(W):\t\t{inverter.getPV()} W")
    #     print(f"Battery(W):\t{battery} W")
    #     print(f"Meter(W):\t{inverter.getPmeter()} W")
    #     print(f"Load(W):\t{inverter.getLoadFlow()} W")
    #     print(f"\nBattery(W):\t{inverter.get_batteries_soc()} %")
    # print(f"Teplota:\t{inverter.get_inverter_temperature()} C")




    #print(json.dumps(gw.data))
    #print(f"Are the batteries full? {gw.are_batteries_full(fullstate=90.0)}")

    #print(gw.data.keys())
    #print(json.dumps(gw.data['inverter']))
    #print(json.dumps(gw.data))

    # print(f"PV Flow: {gw.getPVFlow()}")
    # print(f"Voltage: {gw.getVoltage()}")

    # print("Getting XLS file - this doesn't work!")
    # inverter.getDayDetailedReadingsExcel(date.today() - timedelta(days=1))
