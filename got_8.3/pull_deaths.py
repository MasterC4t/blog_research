from selenium import webdriver
import time
import pickle

browser = webdriver.Chrome()

browser.get('https://deathtimeline.com/')

# Compact View
elem = browser.find_element_by_class_name('toggle-inner')
elem.click()

# Click and Scroll Down to Season 6
seasons = browser.find_elements_by_class_name('season-link')
seasons[5].click()
time.sleep(5)

# Find Death Episodes

eps = browser.find_elements_by_class_name('episode-container')
print(len(eps))

death_name_list = []
death_ep_list = []
for i in range(len(eps)):
    episode = eps[i]
    ep_number = i + 1
    death_containers = episode.find_elements_by_class_name('death-right')
    if len(death_containers) > 0:
        death_names = [death.find_element_by_tag_name('h3').text for death in death_containers]
    for person in death_names:
        death_name_list.append(person)
        death_ep_list.append(ep_number)

death_dict = dict(zip(death_name_list, death_ep_list))

print(death_dict['Mace Tyrell'])

# Save to Pickle
with open('got_data/death_dict.pickle', 'wb') as handle:
    pickle.dump(death_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


browser.quit()
