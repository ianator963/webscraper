'''
This is the data parser
'''

# import json5
# with open('>>') as json_data:jsonData = json.load(json_data)
import scraper

#info = content.findAll('p', attrs={"class": "content"}).textprint info

for info in content.findAll('p', attrs={"class": "content"}):print
info.text.encode('utf-8')