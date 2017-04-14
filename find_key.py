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

number = 0      # 0 = page 1. 10 = page 2. ...

while True:
	page = requests.get('https://www.google.com/search?q=' + query.replace(' ', '+') + '+product+key&start=' + str(number)).text
	soup = BeautifulSoup(page, 'html.parser')
	#print soup
	#print 'searching'
	#print soup.find_all('h3', {'class':'r'})
	try:
		for x in soup.find_all('h3', {'class':'r'}):
			raw_link = x.find('a')['href']
			end = raw_link.find('&sa=')
			#print 'checking validity'
			if raw_link[7:end].find('?q=') == -1:
				link = raw_link[7:end]
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
	except KeyboardInterrupt:
		exit()
	except:
		pass
	number += 10
