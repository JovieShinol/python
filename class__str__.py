class dog:
   species = "Canis familiaris"
   def __init__(self,name,age) -> None:
      self.name = name
      self.age = age
      print(self.name)
   
   def __str__(self) -> str:
      return f"'you have retuned the object'"
   def details(self):
      return f"{self.name} age is {self.age} and their species is {dog1.species}"

dog1 = dog("jimm",6)
print(dog1.details())