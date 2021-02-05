class bac_finder(object):

    #the initiation, also containing std
    def __init__(self, myweight, timepassed, volume, amount, gender):
        self.myweight = myweight
        self.timepassed = timepassed 
        self.volume = volume
        self.amount = amount 
        self.gender = gender
        self.std = 0.0068

    #this function calculates the rouned value of a normal drink
    def normal_drink(self):
        return round((self.std * self.volume) * self.amount, 2)
        
    #this function calculates the promillage of a man
    def man_prom(self):
        return round((self.normal_drink() * 12) / ((self.myweight * 1.7) - (0.15 * self.time)), 2)

    #this function calculates teh promillage of a woman
    def woman_prom(self):
        return round((self.normal_drink() * 12) / ((self.myweight * 1.6) - (0.15 * self.time)), 2)

    #this functions prints the results
    def result(self):
        if self.gender == "woman":
            print(f'\nAs a woman who drank {self.amount} cl. of {self.volume}% vol, {self.time} hours ago.')
        elif self.gender == "man":
            print(f'\nAs a man who drank {self.amount} cl. of {self.volume}% vol, {self.time} hours ago.')