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
import re
import dbConnection as dbCon

def extractData(url):
    connection = dbCon.OpenDBConnection()
    hdr = {'User-Agent': 'Mozilla/5.0'}
    # https://stackoverflow.com/questions/42814637/glassdoor-api-login-not-working-with-python-response-403-bots-not-allowed
    # print(requests.get(str(url).replace(" › ","/Job/"), headers=hdr).text)
    response = requests.get(url, headers=hdr)
    print(response)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    jobListing = soup.find_all(class_="jobContainer")

    for job in jobListing:
        jobList = []
        print("---------------------------------")
        print((str(job.contents[0]).split('class="jobInfoItem jobEmpolyerName"')[1].split("<")[0]))
        jobList.append((str(job.contents[0]).split('class="jobInfoItem jobEmpolyerName"')[1].split("<")[0]))

        print((str(job.contents[1]).split('">')[1].split("<")[0]))
        jobList.append((str(job.contents[1]).split('">')[1].split("<")[0]))

        print((str(job.contents[2]).split("subtle loc")[1].split("<")[0]))
        jobList.append((str(job.contents[2]).split("subtle loc")[1].split("<")[0]))

        if(len((job.contents)) > 3 and "salaryText" in str(job.contents[3])):
            print((str(job.contents[3]).split("salaryText")[1].split("<")[0]))     
            jobList.append((str(job.contents[3]).split("salaryText")[1].split("<")[0]))   
            print((str(job.contents[3]).split("jobLabels")[1].split('<span class="minor">')[1].split("<")[0]))
            jobList.append((str(job.contents[3]).split("jobLabels")[1].split('<span class="minor">')[1].split("<")[0]))
        else:
            print((str(job.contents[2]).split("jobLabels")[1].split('<span class="minor">')[1].split("<")[0]))
            jobList.append(0)
            jobList.append((str(job.contents[2]).split("jobLabels")[1].split('<span class="minor">')[1].split("<")[0]))
        print("---------------------------------")
        dbCon.insertData(connection, jobList)

    dbCon.closeDBConnection

def formulateURLfromGoogleSearch(baseUrl):
    noOfPagesToExtract = 1
    response = requests.get(baseUrl)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # https://stackoverflow.com/questions/8936030/using-beautifulsoup-to-search-html-for-string
    # https://www.regular-expressions.info/quickstart.html
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    # urls = soup.body.find_all(text=re.compile("https://www.glassdoor.com › +[a-zA-Z]+-+jobs"))
    urls = soup.body.find_all(href=re.compile("https://www.glassdoor.com/"), limit=1)

    # for url in urls:    
    finalJobURL =str(urls[0]).split("q=")[1].split("&")[0]
    # Create a URL for first 3 pages
    for cnt in range(0, noOfPagesToExtract):
        if(cnt == 0):
            # print(finalJobURL)
            extractData(finalJobURL)
        else:
            # print(finalJobURL+f"_IP{cnt}.htm")
            extractData(finalJobURL+f"_IP{cnt}.htm")
