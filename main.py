from iss import Iss

apollo11 = Iss("en")


print(f"Continent Name : {apollo11.getContinent()} and continent code is : {apollo11.getContinentCode()}")
print(f"Country Name : {apollo11.getCountryName()} and country code is : {apollo11.getCountryCode()}")
print(f"Locality : {apollo11.getLocality()} ")
print(f"TimeStamp : {apollo11.getTimeStamp() }")
print(f"Latitude : {apollo11.getLatitude()} and longitude is : {apollo11.getLongitude()}")

