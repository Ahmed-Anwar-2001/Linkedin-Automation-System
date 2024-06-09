from dependency import *


def collectlink(driver,count):   
    global buttons, links 
    time.sleep(5)
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y)
    for _ in range(count):
        scroll()
    time.sleep(1)
    pyautogui.press('home')
    time.sleep(1)
    buttons = driver.find_elements(By.CSS_SELECTOR, ".feed-shared-control-menu__trigger.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--1.artdeco-button--circle.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view")
    time.sleep(2)
    for button in buttons:
        button.click()
        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
        link = pyperclip.paste()
        links.append(link)
        time.sleep(2)
        if len(links)==count:
            break
    time.sleep(2)
    with open('links.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Links"])
        for link in links:
            writer.writerow([link])

    print("CSV file created with the column 'Links'.")
