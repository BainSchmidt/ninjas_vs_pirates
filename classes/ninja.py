class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 90
        self.rum = 0
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print(f"{pirate.name} has {pirate.health} health left!")
        return self
    
    def take_rum( self , pirate ):
        if pirate.rum > 0:
            pirate.rum -= 1
            self.rum += 1
            print(f"{self.name} steals 1 swig from {pirate.name}!")
        else:
            print(f"{pirate.name} has no rum left")
            

    def ninja_drink_rum(self):
        if self.rum > 0:
            self.rum -= 1
            self.strength += 5
            self.health -= 10
            print(f"{self.name} takes a swig of rum! + 5 Strength, - 10 Health..")
            print(f"There are {self.rum} swigs left")
        else:
            print(f"{self.name} tries to take another drink... Misses his mouth!")