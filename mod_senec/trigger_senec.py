#!#!/usr/local/bin/python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import sys
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.binary_location = "/usr/bin/chromium-browser"
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

start_url = "https://" + sys.argv[1]
print("Start URL: " + start_url)
driver.get(start_url)
#print(driver.page_source.encode("utf-8"))
submenu_setup = driver.find_element(By.XPATH, '//*[@id="lSetup"]')
time.sleep(0.5)
driver.execute_script("arguments[0].click();", submenu_setup)
time.sleep(0.5)
#print(driver.page_source.encode("utf-8"))
submenu_maintenance = driver.find_element(By.XPATH, '//*[@id="btnKonfiguration_AccuService"]')
driver.execute_script("arguments[0].click();", submenu_maintenance)
time.sleep(0.5)
driver.find_element(By.ID, "iconSafetyCharge").click()
time.sleep(0.5)
driver.quit()
