# fve-report

The FVE report is tool used for monitoring of home photovoltaic.  

Script connects to SEMS portal and download basic information about inverter as battery state, actual consumption,
grid input/output. Report would be displayed with actual OTE price. OTE is downloaded with separate script once per day. 

## OTE prices

The OTE prices for today could be downloaded with scraper.

```bash
cd scraper OTE
scrapy crawl ote -O ../date/output.csv
```

## Data display

