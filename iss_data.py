import requests
import json
class IssData : 
    # Here took url as argument since url configuration may vary.
    # So created url in parent class Iss
    def __init__(self,url) :
        data = requests.get(url).json()
        # parse the data
        self.latitude = data['latitude']
        self.longitude = data['longitude']
        self.continent = data['continent']
        self.lookupSource = data['lookupSource']
        self.continentCode = data['continentCode']
        self.localityLanguageRequested = data['localityLanguageRequested']
        self.city = data['city']
        self.countryName = data['countryName']
        self.countryCode = data['countryCode']
        self.principalSubdivision = data['principalSubdivision']
        self.principalSubdivisionCode = data['principalSubdivisionCode']
        self.plusCode = data['plusCode']
        self.locality = data['locality']
        self.localityInfo = data['localityInfo']
