#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from parsel import Selector
import time
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#I'm using this in brave browser
chromedriver = 'C:\chromedriver\chromedriver.exe'
option = webdriver.ChromeOptions()
option.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)

#driver.get method() will navigate to a page given by the URL address
driver.get("https://www.linkedin.com")

#Locate email form by_class_name
username=driver.find_element(By.ID, 'session_key')

#send_keys() to simulate key strokes
username.send_keys("YOUR EMAIL")

#sleep for 0.5 seconds
sleep(0.5)

#Locate password form by_class_name
password=driver.find_element(By.ID, "session_password")

#send_keys() to simulate key strokes
password.send_keys("YOUR PASSWORD")
sleep(0.5)

#Locate submit button by_xpath
sign_in_button=driver.find_element(By.XPATH, '//*[@type="submit"]')
         
#.click() to mimic button click
sign_in_button.click()   


# Input in the search bar
search = WebDriverWait(driver, 85).until(EC.element_to_be_clickable((By.XPATH, './/*[@class="search-global-typeahead__input"]')))
search.send_keys("Kunal Kumar", Keys.RETURN)
time.sleep(2)
#search.send_keys()

#Click on people 
#people = driver.find_element((By.XPATH, './/*[@id="search-reusables__filters-bar"]/ul/li/button'))[0]
#people.click()

# Main url
#driver.get('https://www.linkedin.com/search/results/people/?keywords=Rahul%20Kumar&origin=SWITCH_SEARCH_VERTICAL&sid=ny.')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, './/*[@class="display-flex"]//span/a[@href]')))

#links
links = driver.find_elements(By.XPATH, './/*[@class="display-flex"]//span/a[@href]')

#link in text form

for link in links:
    href = link.get_attribute('href')

Jobdata=[]    
# Iterate through each link and click on it
for index in range(len(links)):
    try:
        # Find the link again inside the loop
        #l = []
        link = driver.find_elements(By.XPATH, './/*[@class="display-flex"]//span/a[@href]')[index]
        #l.append(link)
        #print(l)
        #print('Links:', links)
        # Click on the link
        link.click()

        # Wait for the new page to load (you might need to adjust the wait time)
        time.sleep(7)
        # Extract the name from the new page
        name = driver.find_element(By.XPATH, './/*[@class="text-heading-xlarge inline t-24 v-align-middle break-words"]').text
        location = driver.find_element(By.XPATH, './/*[@class="text-body-small inline t-black--light break-words"]').text
        Education = driver.find_element(By.XPATH, './/*[@class="display-flex flex-column full-width align-self-center"]//div/a//div//div/div/span').text
        
        print(f"Name {index + 1}: {name}")
        print(f"location {index + 1}: {location}")
        print(f"Education {index + 1}: {Education}")
        #print(href(index))
        
        #Store data
        data= {
            'Name':name,
            'location':location,
            'Education':Education
        }
        Jobdata.append(data)
        
        #Go back to the original search results page
        driver.back()

        # Wait for the page to load again (you might need to adjust the wait time)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, './/*[@class="display-flex"]//span/a[@href]')))
    except StaleElementReferenceException:
        print("StaleElementReferenceException: Retrying...")
        # Continue to the next iteration of the loop
        continue
        
        
                            
df=pd.DataFrame(Jobdata)
df.to_csv('profile_linkedin.csv')
  

        
        
        
        
        
        
        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




