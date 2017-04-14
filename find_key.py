#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import re
import sys
import os, os.path

if len(sys.argv) <= 2:
	print("Example: sudo python find_key.py 'windows 7' '?????-?????-?????-?????-?????'")
	exit()

if not os.path.exists('keys'):
	os.makedirs('keys')

def reCompiler(template):
	regex_add = ''
	for letter in template:
		if letter == '?':
			regex_add += "[A-Z0-9_]"
		elif letter == '-':
			regex_add += '-'
		else:
			print('Unrecognized character used in key template')
			exit()
	return regex_add

query = sys.argv[1]
template = sys.argv[2]

regex_compile = reCompiler(template)
pattern = re.compile(regex_compile)

page = requests.get('https://duckduckgo.com/html/?q=' +  query + ' product key').text
soup = BeautifulSoup(page, 'html.parser')
links = soup.find_all('a', {'class':'result__a'})

for x in links:
	inner_link = 'https://duckduckgo.com' + x['href']
	page = requests.get(inner_link).text
	soup = BeautifulSoup(page, 'html.parser')
	link = (soup.find('script').get_text()).replace('window.parent.location.replace("', '').replace('");', '')
	if not link[-4:] == '.pdf':
		print(link)
		chance_html = requests.get(link).text
		chance_text = BeautifulSoup(chance_html, 'html.parser').find('body').get_text()
		#print chance_html
		print(pattern.findall(chance_text))
		print('')
		file = query.replace(' ', '_') + '.txt'
		with open(('keys/' + file), 'a') as key_file:
			for y in pattern.findall(chance_text):
				key_file.write(y + '\n')
