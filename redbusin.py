import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,
                          service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()))
driver.maximize_window()
driver.implicitly_wait(20)

WebD = WebDriverWait(driver, 20)
action = ActionChains(driver)

# Navigate to the website
driver.get("https://www.redbus.in")
print(driver.title)

# Select the source location
driver.find_element(By.ID, "src").send_keys("Ooty")
WebD.until(EC.visibility_of(driver.find_element(By.XPATH, "//text[text()='Charing Cross']")))
driver.find_element(By.XPATH, "//text[text()='Charing Cross']").click()

# Select the destination location
driver.find_element(By.ID, "dest").send_keys("Bangalore")
WebD.until(EC.visibility_of(driver.find_element(By.XPATH, "//text[text()='Madiwala']")))
driver.find_element(By.XPATH, "//text[text()='Madiwala']").click()

# Set the travel date
driver.find_element(By.XPATH, "//span[text()='2']").click()

# Initiate the search
driver.find_element(By.XPATH, '//*[@id="search_button"]').click()

# Select a bus from the search results
WebD.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "/html/body/section/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/ul/div[1]/li/div/div[2]/div[1]"
    ))
).click()

# Open seat selection for the selected bus
WebD.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "/html/body/section/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/ul/div[1]/li/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/i"
    ))
).click()

# Select a seat from the seat layout
busSeat = driver.find_element(By.XPATH,
                              "/html/body/section/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/ul/div[1]/li/div[2]/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]/canvas")

action.move_to_element_with_offset(busSeat, 50, -40).click().perform()