from bs4 import BeautifulSoup as bs
import requests 
import os

url = 'https://www.youtube.com/results?search_query='
	
fo = open('songs.txt', 'r')

for s in fo.readlines():
	l = s.replace(' ', '+')

	url_search = url + l

	r = requests.get(url_search)

	soup = bs(r.content,'lxml')

	for a in soup.find_all('a',href=True):
		links = a['href']
		if('watch' in links):
			wlink = links
			break


	yb = 'https://www.youtube.com'
	dlink = yb + wlink

	command = 'youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 --embed-thumbnail ' + dlink
	os.system(command) 	
