from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
a_tags = soup.find_all("a", attrs={ "rel": "noreferrer"})
titles_href = [tag.get("href") for tag in a_tags]
titles_list = [tag.text for tag in a_tags]
print(titles_list)
print(titles_href)
