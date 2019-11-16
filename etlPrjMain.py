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
import dbConnection as dbCon

# base url for google
# https://www.google.com/search?q=glassdoor+jobs+marietta+ga
# base url for glassdoor
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436.htm
# base url for glassdoor pagination
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436_IP2.htm
# https://www.glassdoor.com/Job/san-jose-jobs-SRCH_IL.0,8_IC1147436_IP3.htm

citiState = ['New York-NY','Los Angeles-CA','Chicago-IL','Houston-TX','Phoenix-AZ','Philadelphia-PA'
,'San Antonio-TX','San Diego-CA','Dallas-TX','San Jose-CA','Austin-TX','Jacksonville-FL','Fort Worth-TX'
,'Columbus-OH','San Francisco-CA','Charlotte-NC','Indianapolis-IN','Seattle-WA','Denver-CO'
,'Washington-DC','Boston-MA','El Paso-TX','Detroit-MI','Nashville-TN','Portland-OR','Memphis-TN'
,'Oklahoma City-OK','Las Vegas-NV','Louisville-KY','Baltimore-MD','Milwaukee-WI','Albuquerque-NM'
,'Tucson-AZ','Fresno-CA','Mesa-AZ','Sacramento-CA','Atlanta-GA','Kansas City-MO','Colorado Springs-CO'
,'Miami-FL','Raleigh-NC','Omaha-NE','Long Beach-CA','Virginia Beach-VA','Oakland-CA','Minneapolis-MN'
,'Tulsa-OK','Arlington-TX','Tampa-FL']

conn = dbCon.OpenDBConnection()
dbCon.truncateData(conn, "glassdoorjobs")
dbCon.closeDBConnection


for city in citiState:    
    searchCityState = urllib.parse.quote(city)
    baseUrl = "https://www.google.com/search?q=glassdoor+jobs+"+searchCityState
    print(baseUrl)
    glassdoor.formulateURLfromGoogleSearch(baseUrl)

print("Glassdoor Process Completed....")

conn = dbCon.OpenDBConnection()
dbCon.truncateData(conn, "monsterjobs")
dbCon.closeDBConnection

cityState2 = ['New Orleans-LA','Wichita-KS','Cleveland-OH','Bakersfield-CA','Aurora-CO'
,'Anaheim-CA','Honolulu-HI','Santa Ana-CA','Riverside-CA','Corpus Christi-TX','Lexington-KY'
,'Stockton-CA','Henderson-NV','Saint Paul-MN','St. Louis-MO','Cincinnati-OH','Pittsburgh-PA'
,'Greensboro-NC','Anchorage-AK','Plano-TX','Lincoln-NE','Orlando-FL','Irvine-CA','Newark-NJ'
,'Toledo-OH','Durham-NC','Chula Vista-CA','Fort Wayne-IN','Jersey City-NJ','St. Petersburg-FL'
,'Laredo-TX','Madison-WI','Chandler-AZ','Buffalo-NY','Lubbock-TX','Scottsdale-AZ','Reno-NV'
,'Glendale-AZ','Gilbert-AZ','Winston–Salem-NC','North Las Vegas-NV','Norfolk-VA','Chesapeake-VA'
,'Garland-TX','Irving-TX','Hialeah-FL','Fremont-CA','Boise-ID','Richmond-VA','Baton Rouge-LA']

for city in cityState2:
    searchCityState = urllib.parse.quote(city)
    cityName = city.split("-")[0]
    stateName = city.split("-")[1]
    baseUrl = f"https://www.monster.com/jobs/l-{cityName}-{stateName}"
    print(baseUrl)    
    monster.formulateURLforPagination(baseUrl)
    
print("Monster Process Completed....")
    
