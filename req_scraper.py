'''
requests library
'''

import requests
import requests.exceptions
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

def scraper(domain, p_URL, depth):
	page = requests.get(domain)
	return page.text

def main():
	i_domain = input("Domain\n>>")
	i_domain = i_domain[:-1]
	i_url = input("URL\n>>")
	i_url = i_url[:-1]
	i_depth = input("Depth\n>>")
	html_doc = scraper(i_domain, i_url, i_depth)
	soup = BeautifulSoup(html_doc, "html.parser")
	for link in soup.find_all('a'):
		link_href = str(link.get('href'))
		if len(link_href) > 0 and link_href[0] == "/":
			print(i_domain + link_href)
		elif len(link_href) > 0 and link_href[0] != "#" and link_href != "None" and "http" in link_href:
			print(link_href)

if __name__ == "__main__":
	main()