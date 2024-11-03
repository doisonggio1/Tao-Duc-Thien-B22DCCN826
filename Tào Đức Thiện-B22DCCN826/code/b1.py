import pandas as pd
from bs4 import BeautifulSoup
import requests

session = requests.session()
comp = "c9"
url = "https://fbref.com/en/squads/822bd0ba/Liverpool-Stats"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

squad_list_table = soup.find('table', {'class': 'stats_table sortable min_width'})
player_links = squad_list_table.find_all('a', href=True)

squad_player_links = [
    link.get('href') for link in player_links 
    if link.get('href').count('/') == 4 and link.get('href').startswith("/en/players/")
]
formatted_urls = [
    f"https://fbref.com/en/players/{link.split('/')[3]}/matchlogs/2023-2024/{comp}/{'-'.join(link.split('/')[-1].split('-')[:-1])}-Match-Logs"
    for link in squad_player_links
]


url_player = 'https://fbref.com/en/players/934e1968/matchlogs/2023-2024/c9/Dominik-Szoboszlai-Match-Logs'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

response_player = session.get(url_player, headers=headers)
soup_player = BeautifulSoup(response_player.text, "html.parser")

date_header_player = soup_player.find("th", text="Date")
header_row_player = date_header_player.find_parent("tr")
headers_player = [th.get_text(strip=True) for th in header_row_player.find_all("th")]
headers_player.insert(0, "Player Name")  # Adding "Player Name" as the first column header

url_keeper = 'https://fbref.com/en/players/7a2e46a8/matchlogs/2023-2024/c9/Alisson-Match-Logs'

response_keeper = session.get(url_keeper, headers=headers)
soup_keeper = BeautifulSoup(response_keeper.text, "html.parser")

date_header_keeper = soup_keeper.find("th", text="Date")
header_row_keeper = date_header_keeper.find_parent("tr")
headers_keeper = [th.get_text(strip=True) for th in header_row_keeper.find_all("th")]
headers_keeper.insert(0, "Player Name")  # Adding "Player Name" as the first column header

import re

player_data = []
keeper_data = []

for url in formatted_urls:
    response_data = session.get(url, headers=headers)
    soup_data = BeautifulSoup(response_data.text, "html.parser")

    title_data = soup_data.title.string
    pattern = r"2023-2024 (Premier League|Serie A|La Liga|Ligue 1|Bundesliga) Match Logs( \(Goalkeeping\))? \| FBref\.com"
    player_name = re.sub(pattern, "", title_data).strip()

    date_header = soup_data.find("th", text="Date")
    if date_header is None:
        continue  
    header_rows = date_header.find_parent("tr")
    data_rows = header_rows.find_all_next("tr")

    for row in data_rows[:-1]: 
        if row.get('class') is None: 
            cells = row.find_all(['th', 'td'])
            row_data = [cell.get_text(strip=True) for cell in cells]
            row_data.insert(0, player_name)

            if "Goalkeeping" in title_data:
                keeper_data.append(row_data)
            else:
                player_data.append(row_data)

df_player = pd.DataFrame(player_data, columns=headers_player)
df_keeper = pd.DataFrame(keeper_data, columns=headers_keeper)

df_player.to_csv("results.csv", sep=';', encoding='utf-8', index=False)
df_keeper.to_csv("Liverpoolkeeper.csv", sep=';', encoding='utf-8', index=False)