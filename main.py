import time
import selenium



#Game PIN bit:

gamePIN = input("Type the game PIN (case sensitive) \n")

#name maker part:

botNumber = 1
botNumberStr = str(botNumber)
botName = input("Pick a name for the bots \n")

#bot count part:

botCount = input("How many bots should join the game? \n")
botCountInt = int(botCount)

#selenium setup:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def addBot():

    driver = webdriver.Chrome()
    driver.get('https://kahoot.it')

    PIN_box = driver.find_element_by_name('gameId')
    PIN_box.send_keys(gamePIN)
    PIN_enter = driver.find_element_by_tag_name('button')
    PIN_enter.click()

    time.sleep(1)

    NN_box = driver.find_element_by_name('nickname')
    NN_box.send_keys(botName + botNumberStr)
    NN_enter = driver.find_element_by_tag_name('button')
    NN_enter.click()

while True:

    addBot()

    print(botNumberStr)

    botNumberStr = str(botNumber)
    if (botNumber == botCountInt + 1):
        break
    else:
        botNumber = botNumber + 1

