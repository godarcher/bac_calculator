class bac_finder(object):
    def __init__(self, myweight, timepassed, volume, amount, gender):
        self.myweight = myweight
        self.timepassed = timepassed 
        self.volume = volume
        self.amount = amount 
        self.gender = gender
        self.std = 0.0068

    def normal_drink(self):
        return round((self.std * self.volume) * self.amount, 2)
        
    '