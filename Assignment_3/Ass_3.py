# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(50)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id", "twotabsearchtextbox") old syntax
search_bar = driver.find_element("id", "twotabsearchtextbox")
search_bar.send_keys("blanket")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(2)

# Verifying that the search results page has loaded
assert "blanket" in driver.title

# Selecting a blanket from the search results
blanket_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div[2]/span/a/div/img")
blanket_link.click()

# Waiting for the blanket details page to load
time.sleep(2)

# Amazon Logo
amazon_logo = driver.find_element("xpath", "/html/body/div[1]/header/div[1]/div[1]/div[1]/div/a/span[1]")
amazon_logo.click()

# Waiting for the Amazon logo to be clicked
time.sleep(2)

# Cart Icon
cart_icon = driver.find_element("xpath", "/html/body/div[1]/header/div[1]/div[1]/div[2]/a[2]/div/span")
cart_icon.click()

# Waiting for the Cart Button to be clicked
time.sleep(2)

# Clicking on no thanks button
# no_thanks_button= driver.find_element("xpath", "/html/body/div[9]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
# no_thanks_button.click()Y
# time.sleep(2)

# Closing the webdriver
driver.close()
