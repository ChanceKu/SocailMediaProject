import zipfile
import os
import csv
import json
from dateutil.relativedelta import relativedelta
import datetime
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

def visited(x='Gmaps.json'):
    try:
        # load json to get visited place
        with open(x, 'r', encoding='utf-8') as f:
            data = json.load(f)
        try:
            # Convert the JSON data into a Pandas DataFrame
            df = pd.DataFrame(data)
            visited = df["地點"]
            visited = list(set(visited))
        except:
            visited = []
    except:
        data = []
        visited = []
    return visited, data