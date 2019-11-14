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
# 1. OpenDBConnection creates the connection and returns its object to calling function
# 2. closeDBConnection closes the connection
# 3. insertData function accepts 3 parameters
#       connection object, list - which has actual data, and table name
# 4. truncateData function accepts 2 parameters
#       connection object, and table name

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

def insertData(connection, jobList, tableName):
    companyname = jobList[0].replace("'","")
    jobtitle = jobList[1].replace("'","")
    location = jobList[2].replace("'","")
    salary = jobList[3]
    daysofposting = jobList[4].replace("'","")

    cursor = connection.cursor()
    sql = f"""
    insert into {tableName}(companyname, jobtitle, location, salary, daysofposting)
    values('{companyname}', '{jobtitle}', '{location}', '{salary}', '{daysofposting}')
    """
    cursor.execute(sql)
    connection.commit()

def truncateData(connection, tableName):
    cursor = connection.cursor()
    cursor.execute(f"truncate table {tableName}")
    connection.commit()
    