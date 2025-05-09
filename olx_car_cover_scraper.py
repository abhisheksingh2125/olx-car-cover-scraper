import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.olx.in/items/q-car-cover"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

with open("olx_car_covers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Location", "Price", "Link"])
    
    for item in soup.select("li.EIR5N"):
        title = item.select_one("span._2tW1I")
        location = item.select_one("span._2tW1I + span")
        price = item.select_one("span.Tkt2p")
        link = item.a['href'] if item.a else ""

        writer.writerow([
            title.text.strip() if title else "N/A",
            location.text.strip() if location else "N/A",
            price.text.strip() if price else "N/A",
            "https://www.olx.in" + link if link else "N/A"
        ])

print("Done. File saved as olx_car_covers.csv")
