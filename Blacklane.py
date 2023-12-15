from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)

# Replace the URL with the actual URL
url = 'https://www.blacklane.com/en/bookings/request/transfers/service_class/?booking_request%5Bpickup%5D=Heathrow+Airport+%28LHR%29%2C+Hounslow%2C+UK&booking_request%5Bpickup_place_id%5D=P%3AQ2hJSjZXM0Z6VFJ5ZGtnUlowSDJRMVZUNTQ4&booking_request%5Bpickup%5D=Heathrow+Airport+%28LHR%29%2C+Hounslow%2C+UK&booking_request%5Bdropoff%5D=17+Grosvenor+Square%2C+London%2C+UK&booking_request%5Bdropoff_place_id%5D=P%3AQ2hJSk4wTm5kaTBGZGtnUng0d0hMUEx5ZnBr&booking_request%5Bdropoff%5D=17+Grosvenor+Square%2C+London%2C+UK&no-data=Thu%2C+Dec+14%2C+2023&booking_request%5Bat_date%5D=2023-12-14&booking_request%5Bat_time%5D=19%3A30'

driver.get(url)

# Wait for the form elements to be present (adjust as needed)
pickup_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'booking_request[pickup]')))
dropoff_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'booking_request[dropoff]')))
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'submit-button')))

# Interact with the form elements (replace with actual values)
pickup_input.clear()
pickup_input.send_keys('Heathrow Airport (LHR), Hounslow, UK')

dropoff_input.clear()
dropoff_input.send_keys('17 Grosvenor Square, London, UK')

# Submit the form
submit_button.click()

# Continue with other actions on the page

# Quit the WebDriver
driver.quit()
