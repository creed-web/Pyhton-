#Functions Syntax ->

def demoFunction(nums):
    """This is a demo function which i created to understand who functions truly works"""
    if nums % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    return demoFunction

def Inputfunc():
    num = int(input("Enter a number: "))
    demoFunction(nums=num)

Inputfunc()