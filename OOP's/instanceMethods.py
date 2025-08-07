#Defining a class with instance methods 
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #This is an instance method
    def bark(self): 
        print(f"{self.name} says woof woof!!")

dog1 = dog("batman",3)
dog2 = dog("Lucy", 3)
dog1.bark()
dog2.bark()