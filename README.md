# fve-report

The FVE report is tool used for monitoring of home photovoltaic.  

Script connects to SEMS portal and download basic information about inverter as battery state, actual consumption,
grid input/output. Report would be displayed with actual OTE prices. OTE is downloaded with separate script once per day. 

The OTE prices are automatically downloaded with scraper and stored in data/output.csv.

## How it works

A scrapperOTE.sh script download actual day prices from OTE market and store them in data/output.csv. A fve-report.sh starts main script which connect to SEMS portal, download actual values of inverter as battery state, grid flow, fve panel output or actual consumption. Script also reads stored OTE prices from output.csv and display all on display (e-paper hat), whole process is repeated every 10 minutes.

## Hardware

rpi zero W with waveshare 2.13 V2 e-paper hat.

## Environment and dependencies

### SEMS configuration

for automated connection to SEMS portal you have to update configuration with (pygoodwe documentation has instruction where you can find station id, ...)
```
cp config.py.example config.py
vim config.py
```

### Display set up on rpi
enable spi interface (https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual)
```
sudo raspi-config
Choose Interfacing Options -> SPI -> Yes Enable SPI interface
```

check if fallowing lines are uncommented in /boot/firmware/config.txt
```
dtparam=i2c_arm=on
dtparam=spi=on
```

### Python dependencies
prepare python environment
```
python -m venv --system-site-packages .venv
source .venv/bin/activate
python -m pip -r requirements
```

### Automated script startup
update cron with OTE price actualization script and main script startup on boot.
```bash
crontab -e
0 0 * * * /home/buky/git/fve-report/scripts/scrapperOTE.sh
@reboot /home/buky/git/fve-report/scripts/fve-report.sh
```
