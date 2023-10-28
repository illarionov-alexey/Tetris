import numpy as np

a = int(input())
b = int(input())
c = int(input())
arr = np.array((a, b, c))
print(arr.max())
print(arr.argmax())

class City:
    all_cities = []

    def __init__(self, name, year):
        self.name = name
        self.year = year

ny = City("New York", 1624)
ny.all_cities.append("New York")

stockholm = City("Stockholm", 1187)
stockholm.all_cities = ["Stockholm"]
print(City.all_cities)

class Alien:
    count = 0
    places = []

    def __init__(self, planet, species):
        self.planet = planet
        self.species = species


mart = Alien("Mars", "martian")
mart.places.append("Mars")
mart.count += 1

dalek = Alien("Scaro", "dalek")
dalek.places.append("Scaro")
dalek.count += 1

Alien.count += 2