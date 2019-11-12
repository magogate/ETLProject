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

import urllib.parse
import fetchGlassdoorJobs as glassdoor


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
    glassdoor.formulateURLfromGoogleSearch(baseUrl)



    
