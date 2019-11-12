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
