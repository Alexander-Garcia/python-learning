# TODO: scrape python docs to gather upcoming events then print them in dict
from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# element is the parent <ul>
ul_element = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
date_elements = ul_element.find_elements(By.TAG_NAME, "time")
dates_list = [date.text for date in date_elements]
event_elements = ul_element.find_elements(By.TAG_NAME, "a")
event_list = [event.text for event in event_elements]
final_dict = { key: { "time": date, "name": event} for key in range(len(event_list)) for date in dates_list for event in event_list}
print(final_dict)


driver.quit()
