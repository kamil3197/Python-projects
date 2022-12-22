from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



chrom_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3363438480&f_E=1%2C2&f_WT=1%2C2%2C3&geoId=101496088&keywords=python&location=Gda%C5%84sk%2C%20Woj.%20Pomorskie%2C%20Polska&refresh=true")
sign_click = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
sign_click.click()
email = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')

email.send_keys("yourmail")
password.send_keys("yourpass")

time.sleep(2)

log_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
log_in.click()

time.sleep(2)

offer = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for offers in offer:
    try:
        offers.click()
        time.sleep(2)
        save = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
        save.click()
        time.sleep(2)
        follow = driver.find_element(By.CLASS_NAME, 'follow')
        follow.click()
    except NoSuchElementException:
        print("nie było elementu")
        continue

time.sleep(100)
