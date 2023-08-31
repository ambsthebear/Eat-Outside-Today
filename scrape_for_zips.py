from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# FIND elements using developer tools
    # clickable zip codes class = "si-content-label__link"
    # 
    # 
    # 
    # 
    # 
    # 
    
# CSV setup
file=open("zipsandneighborhoods.csv", "w", newline="")
writer=csv.writer(file)
writer.writerow(["id", "zip code", "neighborhood comments"])

# SCRAPER setup for page
browser_driver=Service("C:\\Users\\16306\\OneDrive\\Desktop\\chromedriver.exe")
scraper=webdriver.Chrome(service=browser_driver)
scraper.get("https://www.seechicagorealestate.com/zip-codes/")

# CREATE wait to make sure data loads before scraping
wait = WebDriverWait(scraper, 10)
element_to_watch = scraper.find_element(By.CLASS_NAME, "si-content-label__link")
wait.until(EC.element_to_be_clickable(element_to_watch))
element_to_watch.click()

# SCRAPE the page
unique_id=1
while True:
    zips=scraper.find_elements(By.CLASS_NAME, "si-content-label__link")
    for zip in zips:
        code=zip.find_element(By., "title")
    try:
        element=scraper.find_element(By.PARTIAL_LINK_TEXT, "zip-codes/60")
        element.click()
    except NoSuchElementException:
        break

# QUIT browser and close file
file.close()
scraper.quit()