class Person:
    full_name = None
    age = None
    place = None

    def __init__(self, full_name, place, age=18):
        self.full_name = full_name
        self.age = age
        self.place = place

    def __str__(self):
        return f'{self.full_name} {self.age} {self.place}'

    def talk(self):
        print(f"This {self.full_name} say")

    @classmethod
    def move(cls, address):
        cls.place = address
        print(cls.place)

person = Person('Tima', 'Osh bazar')
person.talk()
Person.move('yug3')