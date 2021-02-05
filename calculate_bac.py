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
        
    def man_prom(self):
        return round((self.normal_drink() * 12) / ((self.myweight * 1.7) - (0.15 * self.time)), 2)