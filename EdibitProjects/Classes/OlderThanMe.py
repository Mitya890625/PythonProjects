class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def compare_age(self, other):
        if self.age < other.age:
            result = 'older than'
        elif self.age == other.age:
            result = 'the same age as'
        else:
            result = 'younger than'
        return f"{other.name} is {result} me"
def main():
    p1 = Person('Mitya', 26)
    p2 = Person('Tanya', 38)
    p3 = Person('Taras', 25)
    p4 = Person('Banan', 26)
    print(p1.compare_age(p2))
    print(p1.compare_age(p3))
    print(p1.compare_age(p4))
main()
