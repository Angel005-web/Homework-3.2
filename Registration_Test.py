from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://invu.ge")
wait = WebDriverWait(driver, 15)

try:
    print("Step 1: Click 'შესვლა' (Sign In)...")
    try:
        sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[self::button or self::a or self::div or self::span][contains(text(),'შესვლა') or contains(text(),'Sign In')]")))
        sign_in_btn.click()
    except Exception as e:
        print("Could not find/click 'შესვლა' button. Debugging candidates:")
        elements = driver.find_elements(By.XPATH, "//*[contains(text(),'შესვლა') or contains(text(),'Sign In')]")
        for el in elements:
            print(f"Tag: {el.tag_name}, Text: {el.text}, Displayed: {el.is_displayed()}, Enabled: {el.is_enabled()}")
        raise e

    # Step 1.5: Fill in Email and Password fields in the modal
    print("Step 1.5: Filling in Email and Password fields...")
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @name='email' or contains(@placeholder, 'Email')]")))
    email_input.clear()
    email_input.send_keys("lanuka15@xxx.com")
    password_input = driver.find_element(By.XPATH, "//input[@type='password' or @name='password' or contains(@placeholder, 'Password')]")
    password_input.clear()
    password_input.send_keys("123456")

    print("Step 2: Wait for 'Welcome Back' modal...")
    modal = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Welcome Back')]/ancestor::div[contains(@class,'modal') or @role='dialog']")))

    print("Step 3: Click 'Sign up here' link...")
    sign_up_link = modal.find_element(By.XPATH, ".//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'sign up here')]")
    sign_up_link.click()

    print("Step 4: Wait for registration form and fill fields...")
    first_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='firstName' or @placeholder='First Name']")))
    first_name.send_keys("Nino")
    last_name = driver.find_element(By.XPATH, "//input[@name='lastName' or @placeholder='Last Name']")
    last_name.send_keys("Beridze")
    email = driver.find_element(By.XPATH, "//input[@type='email' or @name='email']")
    email.send_keys(f"nino.beridze+{int(time.time())}@test.com")
    password = driver.find_element(By.XPATH, "//input[@type='password' or @name='password']")
    password.send_keys("Test@1234")
    try:
        confirm_password = driver.find_element(By.XPATH, "//input[@name='confirmPassword']")
        confirm_password.send_keys("Test@1234")
    except:
        print("No confirm password field found (skipping).")

    print("Step 5: Click 'Sign Up'...")
    sign_up_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Sign Up')]")
    sign_up_btn.click()

    print("Step 6: Validate registration success...")
    success = wait.until(lambda d: "Registration successful" in d.page_source or "dashboard" in d.current_url)
    if success:
        print("✅ Registration completed successfully!")
    else:
        print("⚠️ Registration test failed – success message not found.")

except Exception as ex:
    print(f"❌ Test failed: {ex}")
finally:
    driver.quit()
    print("Browser closed.")