import requests
from bs4 import BeautifulSoup

# base url represents the path 
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# defining objects and building lists
features = "html.parser"
soup = BeautifulSoup(page.content,features)
# find HTML element by ID
results =soup.find(id="ResultsContainer")
# can use prettify to clean up the results
# print(results.prettify())
# assign all card content to job elements
job_elements = results.find_all("div",class_ = "card-content")
# parse through job elements and pull title, company and location. Should be 10 sets of info
for job_element in job_elements:
    # print(job_element,end="\n"*2)
    
    title_element = job_element.find("h2",class_ = "title")
    # strip the white space
    print(title_element.text.strip())
    company_element = job_element.find("h3",class_ = "company")
    print(company_element.text.strip())
    location_element = job_element.find("p",class_ = "location")
    print(location_element.text.strip())

# collect python jobs into a list 
python_jobs = results.find_all("h2",string = lambda text: "python" in text.lower())

print(len(python_jobs))
# grab all the parent elements 
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
    ]

# parse through all the parent elements 
for job_element in python_jobs_elements:
    # this will do the same thing as the loop above
    title_element = job_element.find("h2",class_ = "title")
    print(title_element.text.strip())
    company_element = job_element.find("h3",class_ = "company")
    print(company_element.text.strip())
    location_element = job_element.find("p",class_ = "location")
    print(location_element.text.strip())
    
    # this will pull all the hyperlinks
    links = job_element.find_all("a")
    # parse through all the links for 
    for link in links:
        # print the stripped links
        print(link.text.strip())
        # find the link containing href
        link_url = link["href"]
        # print the link 
        print(f"Apply here: {link_url}\n")
        # should output
        # Apply
        # Apply here: https://realpython.github.io/fake-jobs/jobs/software-developer-python-90.html

    
    
