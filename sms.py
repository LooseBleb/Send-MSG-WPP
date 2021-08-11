import os
import time
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

number = --infome
msg = --infome


dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))

try:
    element = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, "side"))

    )
finally:
    
        texto = urllib.parse.quote(msg)

        link = f"https://web.whatsapp.com/send?phone={number}&text={texto}"
        navegador.get(link)
        time.sleep(6)
        navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
