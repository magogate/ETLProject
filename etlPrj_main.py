# Created By: 
#     Grettel Canepari
#     Katherine Lee
#     Mandar Gogate
#     Petra Alex
#     Preet Puri
#     Sweta Shekhar
# Created On: 11/09/2019
# This program performs following steps in order to pull job information from glassdoor jobsite
# 1. search glassdoor jobs with city/state name on google first
# 2. Extract very first glassdoor url from google search 
# 3. Using glassdoor url, it derives 3 URLs for first 3 pages of glassdoor for respective city/state 
# 4. Extracts Employer Name, Job Title, Salary and Job Posting Days for first 3 pages using derived URL at Step#3

import requests
import bs4
import urllib.parse
import re

def extractData(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    # https://stackoverflow.com/questions/42814637/glassdoor-api-login-not-working-with-python-response-403-bots-not-allowed
    # print(requests.get(str(url).replace(" › ","/Job/"), headers=hdr).text)
    response = requests.get(url, headers=hdr)
    print(response)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all(class_="jobContainer")

    for h in headlines:
        print("---------------------------------")
        print((str(h.contents[0]).split('class="jobInfoItem jobEmpolyerName"')[1].split("<")[0]))
        print((str(h.contents[1]).split('">')[1].split("<")[0]))
        print((str(h.contents[2]).split("subtle loc")[1].split("<")[0]))
        if(len((h.contents)) > 3 and "salaryText" in str(h.contents[3])):
            print((str(h.contents[3]).split("salaryText")[1].split("<")[0]))        
            print((str(h.contents[3]).split("jobLabels")[1].split('<span class="minor">')[1].split("<")[0]))
        else:
            print((str(h.contents[2]).split("jobLabels")[1].split('<span class="minor">')[1].split("<")[0]))
        print("---------------------------------")

# base url for google
# https://www.google.com/search?q=glassdoor+jobs+marietta+ga
# base url for glassdoor
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436.htm
# base url for glassdoor pagination
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436_IP2.htm
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436_IP3.htm

searchCityState = urllib.parse.quote("marietta")

baseUrl = "https://www.google.com/search?q=glassdoor+jobs+"+searchCityState

print(baseUrl)
response = requests.get(baseUrl)
soup = bs4.BeautifulSoup(response.text, "html.parser")
# https://stackoverflow.com/questions/8936030/using-beautifulsoup-to-search-html-for-string
# https://www.regular-expressions.info/quickstart.html
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
urls = soup.body.find_all(text=re.compile("https://www.glassdoor.com › +[a-zA-Z]+-+jobs"))

for url in urls:    
    finalJobURL = str(url).replace(" › ","/Job/")
    # Create a URL for first 3 pages
    for cnt in range(0,3):
        if(cnt == 0):
            # print(finalJobURL)
            extractData(finalJobURL)
        else:
            # print(finalJobURL+f"_IP{cnt}.htm")
            extractData(finalJobURL+f"_IP{cnt}.htm")
    
    # first urls for-loop is returning more than one url
    # however, we need only first seach results, and 
    # then using which we can do the pagination if needed
    break


