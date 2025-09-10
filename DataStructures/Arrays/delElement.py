#Delete an element from an given position in an array 
 
##Using built-in methods->

arr = [10,20,30,40,50]
pos = 2

del arr[pos-1]

for i in range(0,len(arr)):
    print(arr[i], end= " ")   

##Using custom methods->

arra = [10,20,30,40,50]
posi = 3

for i in range(posi,len(arra)):
    arra[i-1] = arra[i]

arra = arra[:-1]
print("\n")
for i in range(0,len(arra)):
    print(arra[i], end =" ")