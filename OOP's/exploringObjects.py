class Dog:
    def __init__(self,name,age):
        self.name = name #This is an instance variable
        self.age = age#This is also an instance variable
#Now creating Objects

dog1 = Dog('batman','3')
print(dog1)
print(dog1.name)