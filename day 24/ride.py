from datetime import datetime

class Ride:
    
    def __init__(self , start_time , end_location):
        self.start_time = start_time
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimate_fare = None
    
    
    def start_ride(self):
        self.start_time = datetime.now
        
    
    def end_ride(self):
        self.end_time = datetime.now
        self.rider.wallet -= self.estimate_fare
        self.driver.wallet -= self.estimate_fare
        
    def __repr__(self):
        return f'Ride details started {self.start_location} to {self.end_location}'


class RideRequest:
    def __init__(self):
        pass