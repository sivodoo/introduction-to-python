# Homework - Day 5 - Sivakumar
#
class Animal():
    kingdom = "Animalia"

class Cat(Animal):
    def __init__(self, nam, color, breed):
        self.phylum = "Chordata"
        self.clas = "Mammalia"
        self.order = "Carnivora"
        self.family = "Felidae"
        self.colour = color
        self.breed = breed
        self.name = nam

    def classification(self):
        print("Welcome ", self.name, " the cat")
        print("Kingdom : ", self.kingdom)
        print("Phylum  : ", self.phylum)
        print("Class   : ", self.clas)
        print("Order   : ", self.order)
        print("Family  : ", self.family)
        print("Color   : ", self.colour)
        print("Breed   : ", self.breed)

cat1 = Cat("Lucy", "brown", "Siamese")
cat1.classification()

class Dog(Animal):
    def __init__(self, nam, color, breed):
        self.phylum = "Chordata"
        self.clas = "Mammalia"
        self.order = "Carnivora"
        self.family = "Canidae"
        self.colour = color
        self.breed = breed
        self.name = nam

    def classification(self):
        print("Welcome ", self.name, " the dog")
        print("Kingdom : ", self.kingdom)
        print("Phylum  : ", self.phylum)
        print("Class   : ", self.clas)
        print("Order   : ", self.order)
        print("Family  : ", self.family)
        print("Color   : ", self.colour)
        print("Breed   : ", self.breed)

dog1 = Dog("shuzy", "grey", "Chihuahua")
dog1.classification()

        
