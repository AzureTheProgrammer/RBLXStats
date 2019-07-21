import requests, os, time
from bs4 import BeautifulSoup

print("Welcome to RBLX Stats! Made by Lee Everett / Null#8566")
print("Please know: ")
print("I am still working on updates for this script")

game = input("URL: ")

r  = requests.get(game)
data = r.text
soup = BeautifulSoup(data, features="lxml")

# FIND CURRENT PLAYERS
stats = soup.findAll('li', attrs={'class' : 'game-stat'})

current_players = stats[0]
player_count = current_players.find("p", attrs={'class': 'text-lead font-caption-body wait-for-i18n-format-render'}).text

# FIND FAVOURITES
favourites = stats[1]
favourite_count = favourites.find('p', attrs={'class' : 'text-lead font-caption-body wait-for-i18n-format-render'}).text

# FIND VISITS

visits = stats[2]
visit_count = visits.find('p', attrs={"id" : "game-visit-count"})['title']

# FIND CREATED

created = stats[3]
created_date = created.find('p', attrs={"class" : "text-lead font-caption-body"}).text

# FIND LAST UPDATED

updated = stats[4]
updated_date = updated.find('p', attrs={"class" : "text-lead font-caption-body"}).text

print("")
print("Grabbed these stats!")
print("Current Players: " + player_count)
print("Favourites: " + favourite_count)
print("Visits: " + visit_count)
print("Created Date: " + created_date)
print("Last Updated: " + updated_date)
