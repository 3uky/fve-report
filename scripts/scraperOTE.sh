#!/bin/bash
cd /home/buky/git/fve-report
source .venv/bin/activate
cd ./ote
scrapy crawl ote -O /home/buky/git/fve-report/data/output.csv
