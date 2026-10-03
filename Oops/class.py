class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print("Name of the student: " , self.name) 
    print("age of the student: " , self.age) 

s1 =  Student("Debraj", 20)
s2 = Student("Rahul", 19)
s1.display()
s2.display()
    