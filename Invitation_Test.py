from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://invu.ge")
    print("Opened invu.ge")

    # Step 1: Click 'შესვლა' (Sign In)
    sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'შესვლა') or contains(text(),'Sign In')]")))
    sign_in_btn.click()
    print("Clicked 'შესვლა'")

    # Step 2: Fill in login form
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @name='email' or contains(@placeholder, 'Email')]")))
    email_input.clear()
    email_input.send_keys("anzhelazena@gmail.com")
    password_input = driver.find_element(By.XPATH, "//input[@type='password' or @name='password' or contains(@placeholder, 'Password')]")
    password_input.clear()
    password_input.send_keys("Lanuka15")
    print("Entered email and password")

    # Step 3: Click login button
    driver.find_element(By.XPATH, "//button[contains(text(),'შესვლა') or contains(text(),'Sign In')]").click()
    print("Logged in")

    # Step 4: Go to 'Create Invitation'
    create_inv_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Create Invitation') or contains(text(),'შექმენით მოსაწვევა')]")))
    create_inv_btn.click()
    print("Clicked 'Create Invitation'")

    # Step 5: Fill invitation form (adjust selectors as needed)
    # Example: fill event date
    date_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='date' or @name='eventDate']")))
    date_input.clear()
    date_input.send_keys("15.04.2026")
    print("Entered event date 15.04.2026")

    # Submit invitation (adjust selector as needed)
    driver.find_element(By.XPATH, "//button[contains(text(),'Create') or contains(text(),'შექმნა')]").click()
    print("Invitation created!")

except Exception as e:
    print("❌ Test Failed:", e)
finally:
    time.sleep(3)
    driver.quit()
    print("Browser closed.")