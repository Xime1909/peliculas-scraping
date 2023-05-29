from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def abrir_pagina():
    driver.get('https://www.imdb.com/list/ls025598828/')

def obtener_peliculas():
    try:
        peliculas = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "lister-item-content"))
        )
        peliculas = [pelicula.text for pelicula in peliculas]
        return peliculas
    finally:
        driver.quit()








