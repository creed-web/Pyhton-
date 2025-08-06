# exception Handling in python is done using try, except and block methods

'''try:
    a = b
except:
    print("Variable 'b' is not defined!!" )'''

try:
    a = b
except NameError as ex:
    print(ex)