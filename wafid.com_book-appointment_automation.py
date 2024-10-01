from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://wafid.com/book-appointment/")

# Fill in form fields with explicit waits
user_ap_fields = {
    "id_country": "Algeria",
    "id_city": "Algiers",
    "id_traveled_country": "Bahrain",
    "id_first_name": "John",
    "id_last_name": "Doe",
    "id_dob": "01/01/1990",
    "id_nationality": "Angolan",
    "id_gender": "male",
    "id_marital_status": "single",
    "id_passport": "123456789",
    "id_confirm_passport": "123456789",
    "id_passport_issue_date": "01/01/2020",
    "id_passport_issue_place": "LUANDA",
    "id_passport_expiry_on": "01/01/2030",
    "id_visa_type": "Work Visa",
    "id_email": "joe@gmail.com",
    "id_phone": "+8801734567891",
    "id_national_id": "123456789",
    "id_applied_position": "Cashier",
    "id_applied_position_other": "Cashier"
}

payment_fields = {
    "id_card_holder_name": "John Doe",
    "id_card_number": "123456789",
    "id_expiry_date": "01/28",
    "id_card_security_code": "123"
}

# Fill each field
for field_id, value in user_ap_fields.items():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        element.send_keys(value)
    except Exception as e:
        print(f"Error filling {field_id}: {e}")

# Wait and click the checkbox
try:
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "field.ui.checkbox.agree-checkbox.inline.reverse"))
    )
    checkbox.click()
except Exception as e:
    print(f"Error clicking checkbox: {e}")

# Optional: Wait before ending the session
time.sleep(2)

# Submit the form
try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui.primary.large.submit.fluid.button.small-side-paddings"))
    )
    submit_button.click()
except Exception as e:
    print(f"Error clicking submit button: {e}")

# Check for error messages after submission
try:
    # Wait for a potential error message to appear
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message"))  # Adjust this selector based on actual error message element
    )
    print("There was an error with the submission. Please check your inputs.")
except Exception:
    print("Submission was successful or no error message displayed.")

# Optionally, check the current URL or page elements to confirm submission
current_url = driver.current_url
print(f"Current URL: {current_url}")

if "pay" in current_url:
    print("Redirected to payment page.")
    for field_id, value in payment_fields.items():
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, field_id))
            )
            element.send_keys(value)
        except Exception as e:
            print(f"Error filling {field_id}: {e}")

    try:
        # Wait for the payment button to be clickable
        payment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui.primary.submit.button"))
        )
        payment_button.click()
    except Exception as e:
        print(f"Error clicking payment button: {e}")

# Wait before closing the driver
time.sleep(2)
# Close the driver after the operations
driver.quit()

