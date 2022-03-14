import inquirer
import pyautogui
import time
from alive_progress import alive_bar

from PIL import Image
import requests
from io import BytesIO
import os
import sys
from pprint import pprint
sys.path.append(os.path.realpath("."))
questions = [
    inquirer.List('option',
                  message="What would you like to do?",
                  choices=['spam text', 'spam images'],
                  ),
]

answers = inquirer.prompt(questions)


if answers == {'option': 'spam text'}:
    msg = input("Enter the message: ")
    n = input("How many times ?: ")

    print("t minus")

    count = 5           # 5 second countdown
    while(count != 0):
        print(count)
        time.sleep(1)
        count -= 1

    print("Prepare for lift off!")

    with alive_bar(int(n)) as bar:     # progress bar for visualization
        for i in range(0, int(n)):
            pyautogui.typewrite(msg + '\n')
            bar()
            

elif answers == {'option': 'spam images'}:
    print('Enter URL: ')
    url = input()
    response = requests.get.url
    img = Image.open(BytesIO(response.content))
    n = input("How many times ?: ")

    print("t minus")

    count = 5
    while(count != 0):
        print(count)
        time.sleep(1)
        count -= 1

    print("Prepare for lift off!")

    with alive_bar(int(n)) as bar:     # progress bar for visualization
        for i in range(0, int(n)):
            pyautogui.typewrite(img + '\n')
            bar()
