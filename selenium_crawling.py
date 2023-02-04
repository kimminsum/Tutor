from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, time

def main():
    driver = webdriver.Chrome(f"{os.getcwd()}/chromedriver.exe")
    driver.get("https://www.google.com/webhp")
    search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
    search_box.send_keys("날씨 \n")

    time.sleep(10)

    driver.close()

if __name__=="__main__":
    main()