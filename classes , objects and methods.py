class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

  def printName(self):
    print(self.name)

  def printAge(self):
    print(self.age)

  def printEveryInfo(self):
    print(f"{self.name} {self.age}")


p1 = Person("Emil")
p2 = Person("Tobias", 25)

p1.printName()
p1.printAge()
p2.printName()
p2.printAge()

p1.printEveryInfo()