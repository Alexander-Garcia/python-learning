import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
BASE_URL = "https://www.espn.com"
URL = "https://www.espn.com/mlb/scoreboard"

response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")
a_list = soup.find_all(name="a")
target = [t for t in a_list if t.text == "Box Score"]
box_score_href = target[0]["href"]

box_score_response = requests.get(url=f"{BASE_URL}{box_score_href}", headers=HEADERS)
score_soup = BeautifulSoup(box_score_response.text, "lxml")
# grabbing player names
players_names = [refs.text for refs in score_soup.select("td div a") if "." in refs.text]
print(players_names)

player_stats_row = score_soup.find_all(name="tr", attrs={ "data-idx": "0"})
print(player_stats_row)
print(score_soup.find_all(name="div", attrs={ "class": "ResponsiveTable--fixed-left"}))

