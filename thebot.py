from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import csv
from namegenerator import *
from mixingalgorithm import merge_strings
import os 
import time

totalfiles = 0

for i in os.listdir():
    if totalfiles == 0:
        print("")
    else:
        if i.split()[1] == "txt":
            totalfiles += 1


def the_csv_file(filename):
    with open(filename, "r") as csvfilemain:
        reader = csv.reader(csvfilemain)
        rows1 = [rows for rows in reader]
    for row in rows1[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome('chromedriver.exe', chrome_options = options)
driver = webdriver.Chrome()


def connect():
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    
def createcred():
    k = namegenerator_()
    username = merge_strings(k[0], k[2])
    passwrd= merge_strings(username, random_masala())
    with open(f'credential{totalfiles+1}.txt', "a+") as cred:
        cred.write(f"name = {k[0]} {k[2]}\nusername = {username}\npassword = {passwrd}\n\n------------------------\n")
    return username, passwrd


#gmail account
# def nameedition():
#     the_firstname = driver.find_element("id", 'firstName')
#     the_firstname.send_keys(k[0])
#     the_firstname.send_keys(Keys.ENTER)
#     the_lastname = driver.find_element("xpath", '//*[@id="lastName"]')
#     the_lastname.send_keys(k[2])
#     the_username = driver.find_element(By.ID, "username")
#     the_username.send_keys(createcred()[0])
#     the_password = driver.find_element("xpath", '//*[@id="passwd"]/div[1]/div/div[1]/input')
#     the_password.send_keys(createcred()[1])
#     the_password.send_keys(Keys.ENTER)
#     the_confirmpassword = driver.find_element("xpath", '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
#     the_confirmpassword.send_keys(passwrd)
#     the_confirmpassword.send_keys(Keys.ENTER)
#     nextbutton = driver.find_element("xpath", '//*[@id="accountDetailsNext"]/div/button')
#     nextbutton.send_keys(Keys.ENTER)

def instagram(email):
    time.sleep(10)
    fullname = driver.find_element('xpath', '//*[@id="mount_0_0_X5"]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')
    fullname.send_keys(k[0]+" "+k[2])
    username = driver.find_element('xpath', '//*[@id="mount_0_0_X5"]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input')
    username.send_keys(createcred()[0])
    password = driver.find_element('xpath', '//*[@id="mount_0_0_X5"]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input')
    password.send_keys(createcred()[1])


if __name__ =="__main__":
    print(createcred())
    connect()
    instagram("pranavdwivedi45645@gmail.com")
    