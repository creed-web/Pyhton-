#Delete an elment from the beginning of an array without using built-in methods 

arr = [7,3,4,57,90,1,2]

for i in range(0,len(arr)-1):
    arr[i] = arr[i+1]

arr = arr[:-1]

for i in range(len(arr)):
    print(arr[i], end =" ")