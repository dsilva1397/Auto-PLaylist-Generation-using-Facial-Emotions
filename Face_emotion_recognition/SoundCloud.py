from selenium import webdriver
import requests
import bs4
from pynput.mouse import Button
from pynput.mouse import Controller as CMouse
import time
from pynput.keyboard import Key
from pynput.keyboard import Controller as CKey


first_click = 0

def get_song(song_name, browser, track_url,first_click):
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

	if first_click == 0:
		mouse = CMouse()
		mouse.position = (1053.60546875, 786.0703125)
		time.sleep(9)
		mouse.click(Button.left, 2)
		mouse.position = (553.3046875, 653.88671875)
		time.sleep(6)
		mouse.click(Button.left, 2)		
	else:
		keyboard = CKey()
		keyboard.press(Key.cmd)
		keyboard.press(Key.tab)
		keyboard.release(Key.cmd)
		keyboard.release(Key.tab)
		mouse = CMouse()
		mouse.position = (553.3046875, 653.88671875)
		time.sleep(5)
		mouse.click(Button.left, 2)
	

	while True:
		break

def StartChrome():
	track_url = "https://soundcloud.com/search/sounds?q="

	# Setting Up Chrome
	chrome_driver_binary = "/usr/local/bin/chromedriver"
	browser = webdriver.Chrome(chrome_driver_binary)
	browser.get("https://soundcloud.com")
	return(track_url, chrome_driver_binary, browser)

def Play_Songs(songs,click):
	# Start Chrome
	print(">>> Welcome to the Emotion Based Music Player")
	
	track_url, chrome_driver_binary, browser = StartChrome()

	# Top Songs to Play
	counter = 0
	get_song(songs[counter], browser,track_url,click)
	click = 1

	while True:
		print(">>>1 - Play Next Song")
		print(">>>0 - EXIT!!!")

		choice = int(input(">>> Your Choice: "))
		
		if choice == 0:
			browser.quit()
			break

		if choice == 1:
			get_song(songs[counter+1],browser,track_url,click)
			counter = counter +1
			continue


# songs1 = ["Hello", 'Snowman - Sia', 'Ambarsarya','love me like you do']

# Play_Songs(songs1,first_click)