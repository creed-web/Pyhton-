#reverse a string using for loop 


demoStr = str(input("Enter a name: "))
reversed_Str = ""
for i in range(len(demoStr)-1, -1,-1):
    reversed_Str += demoStr[i]

print(f"Reversed string = {reversed_Str}")    
    
