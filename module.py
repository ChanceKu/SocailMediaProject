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
from progressbar import ProgressBar

def visited(loaded_json='Gmaps.json'):
    try:
        # load json to get visited place
        with open(loaded_json, 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
        try:
            # Convert the JSON data into a Pandas DataFrame
            loaded_df = pd.DataFrame(loaded_data)
            loaded_visited = loaded_df["地點"]
            loaded_visited = list(set(loaded_visited))
        except:
            loaded_visited = []
    except:
        loaded_data = []
        loaded_visited = []
    return loaded_visited, loaded_data

# scroll(滑幾多下, 滑的距離, 滑的等待)
def scroll(scroll_count_input = 10, scroll_height = -10000, scroll_sleep = 1):
    # move cursor and scroll
    pyautogui.moveTo(200,800,0.1)
    for scroll_i in range(scroll_count_input):
        pyautogui.moveTo(200,600)
        pyautogui.scroll(scroll_height)
        time.sleep(scroll_sleep)
