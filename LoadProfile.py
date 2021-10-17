from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


def LoadProfile(index):
    chrome_options = Options()
    chrome_options.add_argument(
        "--user-data-dir=C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data/"
    )
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(f"--profile-directory=Profile {index}")

    driver = webdriver.Chrome(
        executable_path=r"./WebDriver/chromedriver.exe",
        options=chrome_options,
    )
    return driver
