import requests

class IssLocation : 
    api = "http://api.open-notify.org/iss-now.json" 
    def __init__(self) :
        location = requests.get(self.api).json()
        self.latitude = location['iss_position']['latitude']
        self.longitude = location['iss_position']['longitude']
        self.timestamp = location['timestamp']
        self.message = location['message'] 
    