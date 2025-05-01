From selenium import webdriver



url = https://example.com

driver = webdriver.Chrome()

driver.get(url)

driver.save_screenshot(“webpage_screenshot.png”)

driver.quit()



print(“Screenshot saved successfully!”)



