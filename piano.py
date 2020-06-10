from selenium import webdriver
import keyboard
import time
import random

driver = webdriver.Chrome()


main_url = 'https://virtualpiano.net/'
driver.get(main_url)

keys_to_press = """t y i p O p o i
i o i o i o i y
t i t i p d s P p o
s d s d s d s p
i o i o i p i i
o p s p s p i y t i
i u u y t t
o o i u i
i u u y t o
o i o p P s d d d P p
o p P s d s p
o i s d d d
P p o i u i"""
keys_to_press = keys_to_press.split()
for letter in keys_to_press:
    keyboard.press_and_release(letter)
    time.sleep(random.uniform(0.2, 0.32))