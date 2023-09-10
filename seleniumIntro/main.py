from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/ViewSonic-VX3218-PC-MHD-Monitor-Adaptive-Sync-Frameless/dp/B08V85DH1R/ref=sr_1_2_sspa?crid=23UYJNGTOQDE5&keywords=monitors&qid=1694383285&sprefix=monitor%2Caps%2C177&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(f"The price is {price_dollar}.{price_cents}")

driver.quit()
