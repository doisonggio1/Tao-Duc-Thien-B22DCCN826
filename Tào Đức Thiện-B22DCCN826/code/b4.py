import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://www.footballtransfers.com/en/transfers/latest-football-transfers"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Prepare CSV file
with open('transfers_2023_2024.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player', 'From / To', 'Date', 'Price'])  # CSV header

    # Scrape and save transfer data
    for row in soup.find_all('tr'):  # Loop through each row in the table
        player = row.find('td', scope="col").text if row.find('td', scope="col") else "N/A"
        from_to = row.find('td', scope="col", text="From / To").text if row.find('td', scope="col") else "N/A"
        date = row.find('td', class_="d-none d-lg-table-cell").text if row.find('td', class_="d-none d-lg-table-cell") else "N/A"
        price = row.find('td', class_="td-price").text if row.find('td', class_="td-price") else "N/A"
        
        writer.writerow([player, from_to, date, price])  # Write each row
