from dependency import *
def linkedin_login():
    global buttons, links, posts
    chrome_options = webdriver.ChromeOptions()
    # Initialize the webdriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window() 
    # Open a web page
    driver.get('https://www.linkedin.com/feed/')
    pyautogui.press('enter')
    time.sleep(2)
    text_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Email or Phone')]")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write("jawadtestgtr@gmail.com")
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.write(f"jA<7rlDf92")
    time.sleep(2)   
    pyautogui.press('enter')
    time.sleep(15)
    return driver