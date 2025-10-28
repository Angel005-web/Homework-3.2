from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://invu.ge")


# Wait until the login link is clickable, then click it
wait = WebDriverWait(driver, 15)
try:
	login_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/login"]')))
	login_link.click()
except:
	print("Login link not found or not clickable.")

# Wait until the sign in link is clickable, then click it
try:
	sign_in_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/sign in"]')))
	sign_in_link.click()
except:
	print("Sign in link not found or not clickable.")

# The browser will stay open until you close it manually or call driver.quit()
