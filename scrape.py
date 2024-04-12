from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a page
driver.get("https://dininguiowa.nutrislice.com/menu/burge-market/dinner-3/2024-04-11")

# Wait for some time for the page to load
driver.implicitly_wait(10)  # Waits up to 10 seconds before throwing an exception if it cannot find the element

view_menus_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="018026bcdb3445168421175d9ae4dd06"]'))
    )
view_menus_button.click()

# Find elements
food_categories = driver.find_elements(By.TAG_NAME, 'h3')

# Process elements
for element in food_categories:
    print(element.text)

# Close the browser
driver.quit()
