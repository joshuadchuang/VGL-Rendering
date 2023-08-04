from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Initialize empty set to hold all unique animation names
animationNames = set()

# Set up a wait object with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)

# Loop over the pages
for page in range(1, 53): # Total number of pages is 52, so I just added 1. Modify for ur own use
    driver.get(f"https://www.mixamo.com/#/?page={page}&type=Motion%2CMotionPack")

    # Wait for the elements with class "text-capitalize" to be present
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text-capitalize")))

    # Get the text from each element and add it to the set if it's not empty
    for elem in elements:
        # Wait until the text of the element is not empty
        wait.until(lambda driver: elem.text != '')
        name = elem.text
        if name:  # Check if name is not an empty string
            animationNames.add(name)
        else:
            print("empty string detected")

driver.quit()

# Write all unique animation names to a text file
with open('animationNames.txt', 'w') as f:
    for name in animationNames:
        f.write(name + '\n')