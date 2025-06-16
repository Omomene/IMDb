import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.themoviedb.org/movie"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select("div.card.style_1")

data = []
for movie in movies:
    title_tag = movie.select_one("h2 a")
    if not title_tag:
        continue
    title = title_tag.text.strip()
    link = "https://www.themoviedb.org" + title_tag["href"]

    score_tag = movie.select_one(".user_score_chart")
    note = score_tag["data-percent"] if score_tag else "N/A"

    data.append([title, note, link])

df = pd.DataFrame(data, columns=["Titre", "Note", "Lien"])
df.to_csv("movies_tmdb.csv", index=False, encoding="utf-8-sig", sep=';')
print("✅ Fichier movies_tmdb.csv généré !")
print(df.to_string())
