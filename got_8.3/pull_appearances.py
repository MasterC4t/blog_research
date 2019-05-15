from selenium import webdriver
import time
import pickle

browser = webdriver.Chrome()

with open('got_data/death_dict.pickle', 'rb') as handle:
    death_dict = pickle.load(handle)

i = 0
for character in death_dict.keys():
    # browser.get('https://gameofthrones.fandom.com/wiki/'+character)
    # time.sleep(0.5)
    print(character)
browser.quit()
