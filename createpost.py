from dependency import *
from openai import OpenAI

def llmquery(query):
    url='https://4lpbgikbvgb54o-11434.proxy.runpod.net/'
    client = OpenAI(
                    base_url = url+'v1',
                    api_key='sk-111111111111111111111111111111111111111111111111', # required, but unused
                )

    response = client.chat.completions.create(
                model="mistral",
                messages=[
                    {"role": "user", "content": query},
                ]
                )
    return response.choices[0].message.content

def contains_link(text):
    # Regular expression pattern to match URLs
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    # Search for URLs in the text
    matches = re.findall(url_pattern, text)
    return bool(matches)

def create_post(driver, prompt, schedule=[], context = ""):
    time.sleep(3)
    print(schedule)
    button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-button.artdeco-button--muted.artdeco-button--4.artdeco-button--tertiary.ember-view.share-box-feed-entry__trigger"))
    )
    button.click()
    
    time.sleep(2)
    prompt =f"There are multiple linkedin post formats inside the document- {context}. You can take a hint from these while writing linkedin posts. Now" + prompt
    #output = query({"inputs": (prompt), "return_full_text": True, "temperature":0.0})
    #cleaned_response = (output[0]['generated_text']).replace(prompt, "").strip()
    cleaned_response=llmquery(prompt)
    print(cleaned_response)
    link = contains_link(cleaned_response)
    pyautogui.write(cleaned_response)
    
    time.sleep(10)
    if schedule==[]:
        n = 7
        if link:
            n = 6
        for i in range(n):
            pyautogui.press('tab')
        time.sleep(5)
    else:
        n = 6
        if link:
            n = 5
        for i in range(5):
            pyautogui.press('tab')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write(schedule[0])
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.write(schedule[1])
        time.sleep(1)
        for i in range(4):
            pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(2)
