from selenium import webdriver
from time import sleep
d = webdriver.Chrome()
d.get("c:///Users/tzah.m/Downloads/tip_calc/tip_calc/index.html")
d.find_element(by="id", value="billamt").send_keys("90")
d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
d.find_element(by="xpath", value='//*[@id="musicQual"]/option[3]').click()
d.find_element(by="id", value="peopleamt").send_keys("5")

sleep(10)