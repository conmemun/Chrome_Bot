from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


def createProfile(start, end):
    # init driver
    for i in range(start, end + 1):
        chrome_options = Options()
        chrome_options.add_argument(
            "--user-data-dir=C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data/"
        )
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_argument(f"--profile-directory=Profile {i}")

        driver = webdriver.Chrome(
            executable_path=r"./WebDriver/chromedriver.exe",
            options=chrome_options,
        )
        print(f"profile #{i} is created")
        driver.close()
        driver.quit()
