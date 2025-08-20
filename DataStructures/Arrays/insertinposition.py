#Insert an element at the end of an array without using built-in methods

arr = [5,6,7,8,9,0]
ele = 50
n = 5

print("Array before insertioin ->")
for i in range(n):
    print(arr[i], end =" ")

arr[n] = ele
n+=1

print("\n Array after Insertion ->")
for i in range(len(arr)):
    print(arr[i], end=" ")