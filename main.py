from inverter.goodwe import *


def print_invertor_report(inverter):
    print(f"PV: \t{inverter.get_pv()} W")
    print(f"Bat:\t{inverter.get_batteries_flow()} W  {inverter.get_batteries_soc()} %")
    print(f"Grid:\t{inverter.get_power_flow()} W")
    print(f"Dum:\t{inverter.get_home_consumption()} W")


def main():
    print_invertor_report(Inverter())


if __name__ == "main":
    main()