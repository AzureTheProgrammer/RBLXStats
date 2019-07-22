import requests, os, time, argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("--gameID", help="ID of the game to grab stats of!")
args = parser.parse_args()

time.sleep(4)

game = f"https://www.roblox.com/games/{args.gameID}/"
r  = requests.get(game)
data = r.text
soup = BeautifulSoup(data, features="lxml")
stats = soup.findAll('li', attrs={'class' : 'game-stat'})

# FINDING STATS

# FIND NAME
game_title_container = soup.find("div", attrs={'class' : "game-title-container"})
game_title = game_title_container.find('h2', attrs={'class' : 'game-name'}).text
print("[*] Grabbed the name of the game.")

# FIND CREATOR
creator_container = game_title_container.find('div', attrs={'class' : 'game-creator'})
creator_name = creator_container.find('a', attrs={'class' : 'text-name'}).text
creator_link = creator_container.find('a', attrs={'class' : 'text-name'})['href']
print("[*] Grabbed the creator of the game.")

# FIND CURRENT PLAYERS
current_players = stats[0]
player_count = current_players.find("p", attrs={'class': 'text-lead font-caption-body wait-for-i18n-format-render'}).text
print("[*] Grabbed the current player count of the game.")

# FIND FAVOURITES
favourites = stats[1]
favourite_count = favourites.find('p', attrs={'class' : 'text-lead font-caption-body wait-for-i18n-format-render'}).text
print("[*] Grabbed the favourite count of the game.")

# FIND VISITS

visits = stats[2]
visit_count = visits.find('p', attrs={"id" : "game-visit-count"})['title']
print("[*] Grabbed the total visits of the game.")

# FIND CREATED

created = stats[3]
created_date = created.find('p', attrs={"class" : "text-lead font-caption-body"}).text
print("[*] Grabbed the created date of the game.")

# FIND LAST UPDATED
updated = stats[4]
updated_date = updated.find('p', attrs={"class" : "text-lead font-caption-body"}).text
print("[*] Grabbed the last updated date of the game.")

print("")
print("Grabbed these stats!")
try:
    print("Name: " + game_title)
except:
    print("Name: cant be grabbed!")
time.sleep(0.5)
print("Creator: " + creator_name + " (" + creator_link + ")")
time.sleep(0.5)
print("Current Players: " + player_count)
time.sleep(0.5)
print("Favourites: " + favourite_count)
time.sleep(0.5)
print("Visits: " + visit_count)
time.sleep(0.5)
print("Created Date: " + created_date)
time.sleep(0.5)
print("Last Updated: " + updated_date)
