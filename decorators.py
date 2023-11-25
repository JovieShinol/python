class person(object):
    population = 50
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    @classmethod
    def get_population(ansal):
        return ansal.population
    
    @staticmethod
    def isadult(g):
        return g >= 18
    
    def display(self):
        return f"{self.name} is {self.age} years old!"


person1 = person("tim",34)
print(person1.display())
print(person.get_population())

# we no need to call static method using class instance
print(person.isadult(4))