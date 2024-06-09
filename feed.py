from dependency import *

def feed():
    global buttons, links, posts

    # Set Chrome options to use the existing profile
    chrome_options = webdriver.ChromeOptions()

    # Initialize the webdriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window() 
    # Open a web page
    driver.get('https://www.linkedin.com/feed/')
    pyautogui.press('enter')
    time.sleep(7)
    return driver