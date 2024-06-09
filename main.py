from dependency import *
from login import *
from feed import *
from collectlink import *
from reaction import *
from interactall import *
from createpost import *
from readdocx import *
from readpdf import *
from directoryfileread import *



def react_to_n_posts(n):
    driver = linkedin_login()
    collectlink(driver,n)
    interactall(driver)

def add_post(prompt, schedule=[], directory=''):
    driver = linkedin_login()
    try:
        context = read_files(directory)
    except:
        context = ''
    print("Context-",context)
    create_post(driver,prompt,schedule, context)

react_to_n_posts(5)
#add_post("Write a linkedin post about hiring 2 Asp.Net interns at GTR Ltd whose application deadline is 24 April, 2024.",['04/23/2024','11:00 AM'], "C:\\Users\\HP\\Downloads")

