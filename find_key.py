#!/bin/python

from bs4 import BeautifulSoup
import requests
import re

def reCompiler(template):
	regex_add = ''
	for letter in template:
		if letter == '?':
			regex_add += "[A-Z0-9_]"
		elif letter == '-':
			regex_add += '-'
	return regex_add

#query = raw_input('Enter software: ')

template = '?????-?????-?????-?????-?????'
query = 'windows 7'

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
	print link
	chance_html = requests.get(link).text
	chance_text = BeautifulSoup(chance_html, 'html.parser').find('body').get_text()
	#print chance_html
	print pattern.findall(chance_text)
