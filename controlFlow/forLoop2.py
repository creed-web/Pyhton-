#Print multiplication table of a number 

a = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{a} X {i} = {a*i}")