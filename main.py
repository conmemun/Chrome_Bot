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
from data import *
from LoadProfile import LoadProfile
from addExtension import addExtension


# main
def main():
    for i in range(20, 25):
        addExtension(i, linkAuthentication, addToChromeXpath)
        addExtension(i, linkProxyHelper, addToChromeXpath)
        print(i)
        time.sleep(1)
    print(failedProfile)


main()