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

# Get the episode minute
death_time_list = browser.find_elements_by_class_name('bubble')
death_times = [int(death.text.split(':')[0]) for death in death_time_list]

# Add what episode each character died in
death_ep_list = []
ep_num = 1
time_stamp = 0
for minute in death_times:
    if minute < time_stamp:
        ep_num += 1

    death_ep_list.append(ep_num)
    time_stamp = minute

# Find Death Names
death_container = browser.find_elements_by_class_name('death-right')
death_names = [death.find_element_by_tag_name('h3').text for death in death_container]

# print(death_times.text)
# print(len(seasons))
# print(len(death_times))
# print(len(death_names))

# Make Dict
death_dict = dict(zip(death_names, death_ep_list))

# Save to Pickle
with open('got_data/death_dict.pickle', 'wb') as handle:
    pickle.dump(death_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Should be 50 (37)
# Should be 60 (46)
# Should be 59 (45)

print(death_dict)
browser.quit()
