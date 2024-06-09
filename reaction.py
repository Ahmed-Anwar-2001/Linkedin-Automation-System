from dependency import *

def linkedin_react(driver):   
    time.sleep(4)
    for _ in range(3):
        pyautogui.scroll(-1000)
        time.sleep(0.5)
    time.sleep(1)
    pyautogui.press('home')
    time.sleep(1)
    posts = driver.find_elements(By.CLASS_NAME, "text-view-model")
    reactions = driver.find_elements(By.CLASS_NAME, "social-details-social-counts__reactions-count")
    for react in reactions:
        react.click()
    detailed_reactions = driver.find_elements(By.CLASS_NAME,"mr1")
    for react in detailed_reactions:
            image_elements = react.find_elements(By.TAG_NAME,"img")
            for image_element in image_elements:
                    alt_value = image_element.get_attribute('alt')
                    print(f"Alt Value: {alt_value}")
            if len(react.text)!=0:
                print("React Count= ",react.text)
          
    user_query = '''You are given a post- \"'''
    for post in posts:
        post_text = post.text
        user_query+="\n"+post_text       
    user_query+='\".\nThe reacts in linkedin are- like, celebrate, support, love, insightful, funny. You are assigned to read a post and provide a necessary reaction from the 6 reactions available. What is the suitable linkedin reaction for the given post? You have to choose your reacton from-(like, celebrate, support, love, insightful, funny). Answer in one word.'
    print("Query Passed to LLM: \n")
    print(user_query)
    print('==================================================')
    output = query({"inputs": (user_query), "max_new_tokens":1, "return_full_text": False, "temperature":0.2})

    cleaned_response = (output[0]['generated_text']).replace(user_query, "").strip()
    print("LLM Response:",cleaned_response)
    print("Required Reaction: ",end='')
    print(extract_reaction_word(cleaned_response))
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.scroll(-200)
    time.sleep(2)
    like =  pyautogui.locateOnScreen(f'images/hover.png', confidence=0.9)
    pyautogui.moveTo(pyautogui.center(like))
    time.sleep(2)
    reaction_button_location = pyautogui.locateOnScreen(f'images/{(extract_reaction_word(cleaned_response)).lower()}.png', confidence=0.9)
    pyautogui.click(pyautogui.center(reaction_button_location)) 
    
    time.sleep(5)