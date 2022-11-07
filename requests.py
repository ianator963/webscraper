'''
requests library
'''

import requests
from bs4 import BeautifulSoup

def scraper(domain, URL, depth):
	pass

def main():
	i_domain = input("Domain\n>>")
	i_url = input("URL\n>>")
	i_depth = input("Depth\n>>")
	scraper(i_domain, i_url, i_depth)

if __name__ == "__main__":
	main()