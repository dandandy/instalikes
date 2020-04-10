from driver import driver
import os

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

driver.get('https://www.instagram.com/')
username = driver.find_element_by_name('username')
username.clear()
username.send_keys(USER)
password = driver.find_element_by_name('password')
password.clear()
password.send_keys(PASSWORD)
login = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
login.click()
