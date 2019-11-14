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
# 1. based on city and state provided, this program formulates the base url 
# 2. for glassdoor and monster jobs separately
# 3. and calls corresponding function for extraction and data load


import urllib.parse
import fetchGlassdoorJobs as glassdoor
import fetchMonstorJobs as monster

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
    # print(baseUrl)
    glassdoor.formulateURLfromGoogleSearch(baseUrl)

print("Glassdoor Process Completed....")

for city in citiState:
    searchCityState = urllib.parse.quote(city)
    cityName = city.split("-")[0]
    stateName = city.split("-")[1]
    baseUrl = f"https://www.monster.com/jobs/l-{cityName}-{stateName}"
    # print(baseUrl)    
    monster.formulateURLforPagination(baseUrl)
    
print("Monster Process Completed....")
    
