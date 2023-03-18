from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os

url = "https://branddb.wipo.int/en/explore/results"
directory = "./webscrapped"

driver = webdriver.Chrome()
driver.get(url)

images = driver.find_element(By.NAME,'img')
print(type(images))
for i, image in enumerate(images):
    image_url = image.get_attribute('src')
    if image_url.startswith('http'):
        filename = os.path.join(directory, f"image_{i}.jpg")
        urllib.request.urlretrieve(image_url, filename)

driver.quit()
