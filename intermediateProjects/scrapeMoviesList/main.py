import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
title_list_tags = soup.find_all(name="h3", attrs={ "class": "title"})
text = [tag.text for tag in title_list_tags]
text.reverse()
print(text)
# write them to movie file
with open("movies.txt", "w") as file:
    for t in text:
        file.write(f"{t}\n")

