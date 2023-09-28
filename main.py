from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from mongo import m_connect
import json

db_client = m_connect().client
db = db_client.get_database('datapruebafinal')
col = db.get_collection('moto_list')

driver = webdriver.Edge()
driver.get("https://www.patiodemotos.com/ecuador/anunciante/yamaha-ecuador")
moto_list = driver.find_elements(By.CLASS_NAME, "even")

for f in moto_list:
  moto = f.find_element(By.CLASS_NAME, "views-field-title").text
  price_m = f.find_element(By.CLASS_NAME, "views-field-field-precio").text
  city_m = f.find_element(By.CLASS_NAME, "views-field-field-ciudad").text
  owner_m = f.find_element(By.CLASS_NAME, "views-field-body").text
  telf_m = f.find_element(By.CLASS_NAME, "views-field-field-tel").text

  doc = {
    "type": moto,
    "cost": price_m,
    "location": city_m,
    "person": owner_m,
    "phone": telf_m
  }

  doc_json = json.dumps(doc)
  col.insert_one(json.loads(doc_json))

  print(moto)
  print(price_m)
  print(city_m)
  print(owner_m)
  print(telf_m)
  print('*'*40)
  print()



driver.close()