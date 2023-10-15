from iss_location import IssLocation
from iss_data import IssData
class Iss : 
    def __init__(self, p_language = "en") :
        self.language = p_language
        self.updateLocationAndGetData()

    # This function gets the current location of the ISS and creates the corresponding url to request ISS's data 
    def getLocation(self) : 
        self.location = IssLocation()
        self.latitude = self.location.latitude
        self.longitude = self.location.longitude
        self.timeStamp = self.location.timestamp
        self.createURL()

    # This function creates the related url according to current location of the ISS
    def createURL(self) : 
        # will be written
        self.url = f'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={self.latitude}&longitude={self.longitude}&localityLanguage={self.language}'

    # This function gets the current location of the iss and requests the corresponding data from api and parses it to a IssData object 
    def updateLocationAndGetData(self) : 
        self.getLocation() 
        self.data = IssData(self.url)

    def getLatitude(self) : 
        self.updateLocationAndGetData()
        return self.data.latitude

    def getLongitude(self) : 
        self.updateLocationAndGetData()
        return self.data.longitude
    
    def getContinent(self) : 
        self.updateLocationAndGetData()
        return self.data.continent
    
    def getLookUpSource(self) : 
        self.updateLocationAndGetData()
        return self.data.lookUpSource
    
    def getContinentCode(self) : 
        self.updateLocationAndGetData()
        return self.data.continentCode

    def getLocalityLanguageRequested(self) : 
        self.updateLocationAndGetData()
        return self.data.localityLanguageRequested
    
    def getCity(self) : 
        self.updateLocationAndGetData()
        return self.data.city
    
    def getCountryName(self) : 
        # make request and return name
        self.updateLocationAndGetData() 
        return self.data.countryName
    
    def getCountryCode(self) : 
        self.updateLocationAndGetData()
        return self.data.countryCode

    def getPostCode(self) : 
        self.updateLocationAndGetData()
        return self.data.postCode

    def getPrincipalSubdivision(self) : 
        self.updateLocationAndGetData()
        return self.data.principalSubdivision
    
    def getPrincipalSubdivisionCode(self) : 
        self.updateLocationAndGetData()
        return self.data.principalSubdivisionCode
    
    def getPlusCode(self) : 
        self.updateLocationAndGetData()
        return self.data.plusCode
    
    def getLocality(self) : 
        self.updateLocationAndGetData()
        return self.data.locality

    def getTimeStamp(self) : 
        self.updateLocationAndGetData()
        return self.timeStamp


