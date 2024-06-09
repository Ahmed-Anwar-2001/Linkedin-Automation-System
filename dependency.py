from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import pyautogui
import time
import requests
import re
import csv
import os
import pandas as pd

posts = []
buttons = []
links = []
jobs = []

pyautogui.FAILSAFE = False

def extract_reaction_word(sentence):
    reaction_words = ['like', 'support', 'love', 'insightful', 'celebrate', 'funny']

    pattern = r'\b(?:' + '|'.join(reaction_words) + r')\b'

    match = re.search(pattern, sentence, flags=re.IGNORECASE)

    if match:
        return match.group(0)
    else:
        return 'like'

def scroll():
    pyautogui.scroll(-1000)
    time.sleep(0.5)

def query(payload):
	response = requests.post("https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1", headers={"Authorization": "Bearer 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"}, json=payload)
	return response.json()


def save_links_to_csv(links, save_previous_links=False):
    csv_filename = "links.csv"

    # Check if the CSV file already exists
    if os.path.exists(csv_filename) and save_previous_links:
        mode = "a"  # Append mode
    else:
        mode = "w"  # Write mode
        with open(csv_filename, mode, newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Links"])

    # Write the links to the CSV file
    with open(csv_filename, mode, newline='') as file:
        writer = csv.writer(file)
        for link in links:
            writer.writerow([link])

    print(f"Links {'appended to' if save_previous_links else 'saved in'} {csv_filename}")