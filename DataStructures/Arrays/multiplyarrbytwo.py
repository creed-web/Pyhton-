#multiply every elment of the array by teo

arr = [1,2,3,4,5]
element = 2
n = 4

for i in range(len(arr)):
    arr = arr[i*2]
    
print(arr)