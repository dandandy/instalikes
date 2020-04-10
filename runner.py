import time
from login import driver

if len(driver.find_elements_by_css_selector("button.aOOlW.HoLwm")) > 0:
    not_now = driver.find_elements_by_css_selector("button.aOOlW.HoLwm")[0]
    not_now.click()

like_count = 0
while like_count < 10:
	try:
		button = driver.find_element_by_css_selector('svg[aria-label=Like][height="24"]')
		button.click()
		like_count += 1
		print("liked ", like_count)
	except:
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

print(like_count)
