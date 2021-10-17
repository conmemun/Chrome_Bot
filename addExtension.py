from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from LoadProfile import LoadProfile
from data import *


def addExtension(profileNo, url, xpath):
    driver = LoadProfile(profileNo)
    driver.maximize_window()
    # access extension url
    driver.get(url)
    driver.get(url)

    # click add button
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()
        time.sleep(1)
    except:
        print(f"Profile {profileNo} failed to installed extension {url}")
        failedProfile[profileNo] = url

    # accept popup
    pyautogui.press("tab")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(2)
    driver.close()
    driver.quit()
