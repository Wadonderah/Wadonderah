# class named person
class Person:
  
  #  is called automatically when creating a new Person
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

    # This method defines how a person object can introduce itself. It uses f-strings (formatted string literals) to create a message that includes the person's name, age, and gender.

  def introduce(self):
    print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Wadondera", 30, "Male",)

# Call the introduce method
person1.introduce()
