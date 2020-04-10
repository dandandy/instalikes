from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import os
import sys

SERVER = os.getenv("SERVER")
DRIVER = os.getenv('DRIVER')

if SERVER is not None:
    driver = webdriver.Remote(
        command_executor=SERVER,
        desired_capabilities=DesiredCapabilities.FIREFOX.copy())
elif DRIVER is not None:
    driver = webdriver.Chrome(DRIVER)
else:
    print("SERVER or DRIVER environment variables not set")
    sys.exit(1)

driver.implicitly_wait(10)
