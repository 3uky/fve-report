import json
from functools import lru_cache
from datetime import date

from config import args
from pygoodwe import SingleInverter

@lru_cache()
def get_single_inverter(args=args): #pylint: disable=redefined-outer-name,dangerous-default-value
    """ test fixture """
    # print("Single Inverter")
    goodwe = SingleInverter(
            system_id=args.get('gw_station_id', '1'),
            account=args.get('gw_account', 'thiswillnotwork'),
            password=args.get('gw_password', 'thiswillnotwork'),
            )
    # print("Grabbing data")
    goodwe.getCurrentReadings()
    return goodwe

def print_battery_data(inverter):
    batterydata = inverter.data.get('inverter',{}).get('battery',"").split("/")
    if batterydata:
        voltage = float(batterydata[0][:-1])
        print(f"Battery voltage is: {voltage}")

def print_inverter_data(inverter):
    print(f"Available fields in data: {inverter.data.keys()}")
    print(json.dumps(inverter.data.get('inverter').get('battery'), indent=2))

def print_invertor_report():
    inverter = get_single_inverter()
    battery = inverter.getPVFlow() - inverter.getPmeter() - inverter.getLoadFlow()
    print(f"PV(W):\t\t{inverter.getPVFlow()} W")
    print(f"Battery(W):\t{battery} W")
    print(f"Meter(W):\t{inverter.getPmeter()} W")
    print(f"Load(W):\t{inverter.getLoadFlow()} W")
    print(f"\nBattery(W):\t{inverter.get_batteries_soc()} %")
# print(f"Teplota:\t{inverter.get_inverter_temperature()} C")

print_invertor_report()


#print(json.dumps(gw.data))
#print(f"Are the batteries full? {gw.are_batteries_full(fullstate=90.0)}")

#print(gw.data.keys())
#print(json.dumps(gw.data['inverter']))
#print(json.dumps(gw.data))

# print(f"PV Flow: {gw.getPVFlow()}")
# print(f"Voltage: {gw.getVoltage()}")

# print("Getting XLS file - this doesn't work!")
# inverter.getDayDetailedReadingsExcel(date.today() - timedelta(days=1))
