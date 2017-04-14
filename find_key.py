#!/usr/bin/env python

from bs4 import BeautifulSoup
from random import choice
import requests
import re
import sys
import os, os.path

if len(sys.argv) <= 2:
	print("Example: sudo python find_key.py 'windows 7' '?????-?????-?????-?????-?????'")
	exit()

if not os.path.exists('keys'):
	os.makedirs('keys')

headers = (
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
	'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko)',
	'Chrome/19.0.1084.46 Safari/536.5',
	'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko)',
	'Chrome/19.0.1084.46',
	'Safari/536.5',
	'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13',
	)

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
	header = {'User-agent': choice(headers)}
	url = 'https://www.google.com/search?q=' + query.replace(' ', '+') + '+product+key&start=' + str(number)
	page = requests.get(url, headers=header).text
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
					chance_html = requests.get(link, headers=header).text
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
