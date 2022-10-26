'''
This  is the scraper
'''

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#this takes the html from the website provided as "URL" and assigns it to a variable "page"

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#after analyzing, we take the category "Results Container" and find only the elements in that category
# print(results.prettify())
#commented out code above takes the raw input and makes it slightly more legible but not good enough: continue

'''
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    ##3 lines above can be written without ".text" and ".strip"
    ##".text" removes all the html tags when print and ".strip" removes all the unnecessary whitespace
    print()
'''

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
#defines the parent for the python jobs so that you can see the actual text instead of just the header

job_elements = results.find_all("div", class_="card-content")
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    #runs the same thing as above, but for the python job elements.
    '''links = job_element.find_all("a")
	for link in links:
		link_url = link["href"]
		print(f"Apply here: {link_url}\n")'''
	#prints the links in the child fields from the python job elements in the <h2> tags
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
    #changes the above code to print just the application link and not the information link