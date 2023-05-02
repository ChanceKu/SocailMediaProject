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

def switch():
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(3)

    # 按"評論"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]"))).click()

    time.sleep(3)

    # 按排序->最新
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[7]/div[2]/button/span/span"))).click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[2]").click()