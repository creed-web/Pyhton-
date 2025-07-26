#Calculate sum of first n natural numbers

n = int(input("Enter a number: "))
total = 0
expression = ""

for i in range(1,n+1):
    total+= i
    expression += str(i)
    if i != n:
        expression += " + "


print(f"{expression} = {total}")

       