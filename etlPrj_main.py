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
import psycopg2

def OpenDBConnection():
    from sqlalchemy import create_engine    
    # http://www.postgresqltutorial.com/postgresql-serial/
    # engine = create_engine("postgresql://postgres:"+password+"@localhost:5432/Jobs")    

    # Connect to the database
    connection = psycopg2.connect(host='localhost',
                             port="5432",
                             user='postgres',
                             password='magogate',
                             database='Jobs')
    return connection

def closeDBConnection(connection):
    connection.close()

def insertData(connection, jobList):
    companyname = jobList[0].replace("'","")
    jobtitle = jobList[1].replace("'","")
    location = jobList[2].replace("'","")
    salary = jobList[3]
    daysofposting = jobList[4].replace("'","")

    cursor = connection.cursor()
    sql = """
    insert into GlassdoorJobs(companyname, jobtitle, location, salary, daysofposting)
    values('{}', '{}', '{}', '{}', '{}')
    """.format(companyname, jobtitle, location, salary, daysofposting)
    cursor.execute(sql)
    connection.commit()

def extractData(url):
    connection = OpenDBConnection()
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
        insertData(connection, jobList)

    closeDBConnection

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


# base url for google
# https://www.google.com/search?q=glassdoor+jobs+marietta+ga
# base url for glassdoor
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436.htm
# base url for glassdoor pagination
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436_IP2.htm
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436_IP3.htm

citiState = ["marietta-ga", "atlanta-ga", "san jose-ca", "birmingham-al"]

for city in citiState:    
    searchCityState = urllib.parse.quote(city)
    baseUrl = "https://www.google.com/search?q=glassdoor+jobs+"+searchCityState
    print(baseUrl)
    formulateURLfromGoogleSearch(baseUrl)



    
