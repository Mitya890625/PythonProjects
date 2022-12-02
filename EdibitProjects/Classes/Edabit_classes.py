class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b

    def substract(self):
        return self.a - self.b

    def multiply(self):
        return self.a*self.b

    def divide(self):
        return self.a / self.b

class FootBallPlayer:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def get_age(self):
        print(self.name +" is " + str(self.age) + " old")
    def get_height(self):
        print(self.name +" height is " + str(self.height) + " cm")
    def get_weight(self):
        print(self.name +" weight is " + str(self.weight) + " kg")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        print("Title: " + self.title)
    def get_author(self):
        print("Author: " + self.author)
class Employee:
    email = ''
    fullname = ''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Employee.email = firstname + '.' + lastname + "@company.com"
        Employee.fullname = firstname + ' ' + lastname
class OneThreeNines:
    def __init__(self, number):
        self.number = number
    def ones(self):
        i = 0
        while i < self.number:
            i += 1
        print(i)
    def threes(self):
        i = 3
        count = 0
        while i <= self.number:
            i += 3
            count += 1
        print(count)
    def nines(self):
        i = 9
        count = 0
        while i <= self.number:
            i += 9
            count += 1
        print(count)
class User:
    user_count = 0
    def __init__(self, user):
        self.user = user
        User.user_count += 1
class Name:
	fullname = ''
	initials = ''
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		Name.fullname = fname + ' ' + lname
		Name.initials = fname[0] + '.' + lname[0]
class Person:
    def __init__(self, name, like_list, hate_list):
        self.name = name
        self.like_list = like_list
        self.hate_list = hate_list
    def taste(self, food_name):
        str1 = f"{self.name} eats the {food_name}"
        if food_name in self.like_list:
            return str1 + " and he loves it"
        elif food_name in self.hate_list:
            return str1 + " and he hates it"
        else:
            return str1

class Country:
    is_big = False
    def __init__(self, country_name, country_square, country_population):
        self.country_name = country_name
        self.country_square = country_square
        self.country_population = country_population
        self.density = self.country_population / self.country_square
        if country_population > 250000000 or country_square > 3000000:
            Country.is_big = True
        else:
            Country.is_big = False
    def compare_pd(self, other):
        result = ['smaller', 'larger'][self.density < other.density]
        return '{} has a {} population density than {}'.format(self.country_name, result, other.country_name)

def main():
    australia = Country("Australia", 23545500, 7692024)
    andorra = Country("Andorra", 76098, 468)
    print(andorra.compare_pd(australia))












main()
