from selenium import webdriver
import requests
import bs4
import os

# Searching Song
def get_song(song_name):
	name = song_name
	print()
	"%20".join(name.split(" "))
	browser.get(track_url + name)

	url = track_url + name
	request = requests.get(url)
	soup = bs4.BeautifulSoup(request.text, 'html.parser')
	tracks = soup.select("h2")[3:]
	track_links = []
	track_names = []
	for index, track in enumerate(tracks):
		track_links.append(track.a.get("href"))
		track_names.append(track.text)

	while True:
		break

# Track Url
track_url = "https://soundcloud.com/search/sounds?q="

# Setting Up Chrome
chrome_driver_binary = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary)
browser.get("https://soundcloud.com")

# Start Chrome
print(">>> Welcome to the Emotion Based Music Player")

# Top Songs to Play
songs = ["Hello", 'Snowman - Sia', 'Cant Help Falling in Love with you']
counter = 0
get_song(songs[counter])
while True:
	print(">>>1 - Play Next Song")
	print(">>>0 - EXIT!!!")

	choice = int(input(">>> Your Choice: "))
	
	if choice == 0:
		browser.quit()
		break

	if choice == 1:
		get_song(songs[counter+1])
		counter = counter +1
		continue
