#Inserting an array element without using built-in methods

arr = [3,5,6,7,2,1,69,0]
ele = 9
pos = 2
n = 7

print("Array before insertion ->")
for i in range(n):
    print(arr[i], end=' ')

for i in range(n,pos-1,-1):
    arr[i] = arr[i - 1]

arr[pos-1] = ele
n+=1

print("\nArray after insertion ->")
for i in range(n):
    print(arr[i], end=' ')