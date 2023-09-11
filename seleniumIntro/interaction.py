from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(driver_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(article_count.text)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")

# typing must rerender dom and the element gets an error if we don't find again
search = driver.find_element(By.NAME, "search")
search.send_keys(Keys.RETURN)

driver.quit()
