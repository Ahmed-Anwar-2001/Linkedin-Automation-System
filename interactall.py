from dependency import *
from reaction import*

def interactall(driver):
    df = pd.read_csv('links.csv')
    for link in df['Links']:
        script = "window.open('"+link+"', '_blank');"
        print("Link-",link)
        driver.execute_script(script)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        linkedin_react(driver)
        time.sleep(5)