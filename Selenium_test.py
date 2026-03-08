from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

# Disable password manager & leak detection
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}

chrome_options.add_experimental_option("prefs", prefs)

# Disable Chrome services that trigger popup
chrome_options.add_argument("--disable-save-password-bubble")
chrome_options.add_argument("--disable-password-generation")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")  # Fresh session

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

# -------------------------------
# 1 LOGIN TEST
# -------------------------------
print("Running Login Test")

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

msg = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
print("Login Message:", msg.text)

time.sleep(2)

# -------------------------------
# 2 CHECKBOX TEST
# -------------------------------
print("Running Checkbox Test")

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

for cb in checkboxes:
    if not cb.is_selected():
        cb.click()

print("Checkboxes selected")

time.sleep(2)

# -------------------------------
# 3 DROPDOWN TEST
# -------------------------------
print("Running Dropdown Test")

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")

print("Dropdown selected")

time.sleep(2)

# -------------------------------
# 4 ALERT TEST
# -------------------------------
print("Running Alert Test")

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

alert = wait.until(EC.alert_is_present())
print("Alert text:", alert.text)

alert.accept()

time.sleep(2)

# -------------------------------
# 5 FILE UPLOAD TEST
# -------------------------------
print("Running File Upload Test")

driver.get("https://the-internet.herokuapp.com/upload")

file_path = r"C:\testfile.txt"

driver.find_element(By.ID, "file-upload").send_keys(file_path)
driver.find_element(By.ID, "file-submit").click()

upload = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
print("Upload status:", upload.text)

time.sleep(2)

driver.quit()

print("All tests completed successfully")