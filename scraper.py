import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from datetime import date
import csv
import pandas as pd
import time
import json
import fnmatch
import os
from bs4 import BeautifulSoup
import re
import unidecode

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(
    ChromeDriverManager().install(),
    options=chrome_options
)
driver.get(
    "https://www.amazon.com/Kindle-Now-with-Built-in-Front-Light/dp/B07978J597/")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
price_raw = soup.find("span", {"class": "a-offscreen"})
price = price_raw.text

date_time = datetime.now()
date = (date_time.strftime("%Y-%b-%d %H:%M"))
print(date)
with open('log_with_date.txt', 'a') as f:
    f.write('\n')
    f.write(f'{price} ----- {date}')
with open('log_price_only.txt', 'a') as f:
    f.write('\n')
    f.write(f'{price}')
print('Logged!')
print('Done!')
