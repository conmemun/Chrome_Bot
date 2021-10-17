
# input info by xpath
def inputByXpath(xpath, info):

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    ).send_keys(info)

    grabElement = driver.find_element_by_xpath(xpath)
    getFilledValue = grabElement.get_attribute("value")

    while getFilledValue != info:
        grabElement.clear()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        ).send_keys(info)
        getFilledValue = grabElement.get_attribute("value")
        print(getFilledValue)
    time.sleep(0.2)


# input info by id
def inputById(id, info):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, id))
    ).send_keys(info)
    time.sleep(0.1)


# click by id
def clickById(id):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, id))).click()
    time.sleep(0.5)


# click by XPATH
def clickByXpath(xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()
    time.sleep(0.1)


# Accept pop up
def acceptPopup():
    pyautogui.press("tab")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()


def fillInAuthentication(username, password):
    inputByXpath(authUsernameXpath, username)
    inputByXpath(authPasswordXpath, password)


def addToChrome(url):
    driver.get(url)
    clickByXpath(addToChromeXpath)
    time.sleep(0.5)
    acceptPopup()
    time.sleep(1)
    switchToNewWindow()


def fillInProxy(httpProxy, httpPort):
    # get http host element then send value if not satisfied do again
    grabHttpHostElement = driver.find_element_by_id("http-host")
    currentHttpProxyValue = grabHttpHostElement.get_attribute("value")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "http-host"))
    ).send_keys(httpProxy)

    while currentHttpProxyValue != httpProxy:
        grabHttpHostElement.clear()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "http-host"))
        ).send_keys(httpProxy)
        currentHttpProxyValue = grabHttpHostElement.get_attribute("value")
    time.sleep(0.2)

    # get http port element then send value if not satisfied do again
    grabHttpPortElement = driver.find_element_by_id("http-port")
    currentHttpPortValue = grabHttpHostElement.get_attribute("value")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "http-port"))
    ).send_keys(httpPort)

    while currentHttpPortValue != httpPort:
        grabHttpPortElement.clear()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "http-port"))
        ).send_keys(httpPort)
        currentHttpPortValue = grabHttpPortElement.get_attribute("value")
    time.sleep(0.2)


def switchToNewWindow():
    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    time.sleep(0.5)


