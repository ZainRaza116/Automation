from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-extensions")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

page_number = 1
for page_number in range(1, 100):
    driver.get(f"https://sa.aqar.fm/%D8%B9%D9%82%D8%A7%D8%B1%D8%A7%D8%AA/{page_number}")
    elements = driver.find_elements(By.XPATH, "//div[@class='_content__W4gas']")
    for i, element in enumerate(elements):
        name = driver.find_elements(By.XPATH, "//h4")[i]
        prices = driver.find_elements(By.XPATH, "//p[@class='_price__X51mi']")[i]
        area_elements = driver.find_elements(By.XPATH, "//div[contains(@class, '_spec__SIJiK') and contains(., 'm²')]")
        if area_elements:
            area = area_elements[i].text
        else:
            area = "None"
        print("Element:", name.text)
        print("Price:", prices.text)
        print("Area", area)
        print()
        page_number = page_number + 1


driver.quit()
