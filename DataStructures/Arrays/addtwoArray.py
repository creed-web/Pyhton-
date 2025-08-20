#WAP to add two arrays

arr1 = [3,4,5,6,7,8]
arr2 = [0,9,8,7,6,5]
addedArr = []
n = 6

for i in range(len(arr1)):
    addedArr.append(arr1[i] + arr2[i])

for i in range(len(addedArr)):
    print(addedArr[i], end= ' ')
    