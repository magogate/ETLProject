# Created By: 
#     Grettel Canepari
#     Katherine Lee
#     Mandar Gogate
#     Petra Alex
#     Preet Puri
#     Sweta Shekhar
# Created On: 11/09/2019
# Updated On: 13/09/2019
# This program performs following steps in order to pull job information from glassdoor jobsite
# 1. function formulateURLforPagination creates urls based on pagination numbers
# 2.            and calls truncate table function
# 3. function extractData actually extracts the data
# 4.    Employer Name, Job Title, Salary and Job Posting Days 
# 5.    and calls insertData function for each record

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
    soup = bs4.BeautifulSoup(response.text, "html.parser")    
    # jobListing = soup.find_all('div', class_="summary")
    jobListing = soup.find_all('div', class_="flex-row")
    for job in jobListing:        
        myList = []
        jobName = job.find('div', class_="summary").header.h2.a.text
        company = job.find('div', class_="summary").div.text
        location = job.find('div', class_="summary").find('div', class_="location").text
        postedOn = job.find('div', class_="meta flex-col").find('time').text

        myList.append(jobName.replace("\n","").replace("\r",""))
        myList.append(company.replace("\n","").replace("\r",""))
        myList.append(location.replace("\n","").replace("\r",""))
        #Since there is no salary available, defaulting it to 0
        myList.append(0)
        myList.append(postedOn.replace("\n","").replace("\r",""))    
        
        # print(myList)
        dbCon.insertData(connection, myList, "monsterjobs")
        

def formulateURLforPagination(baseUrl):
    noOfPagesToExtract = 2

    conn = dbCon.OpenDBConnection()
    dbCon.truncateData(conn, "monsterjobs")
    dbCon.closeDBConnection

    # Create a URL for first 3 pages
    # https://www.monster.com/jobs/l-atlanta-ga?page=1
    for cnt in range(1, noOfPagesToExtract+1):
        extractData(baseUrl+f"?page={cnt}")
        
        
