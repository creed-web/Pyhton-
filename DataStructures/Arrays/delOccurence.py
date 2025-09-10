#Delete first Occurence of given element from an array 

#Using built-in methods->
arr = [10,20,30,20,40,50,80]
ele = 30

arr.remove(ele)
for i in range(len(arr)):
    print(arr[i], end = " ")


#Using custom methods->
arra = [1,3,12,3,5,678,76]
ele = 3

for i in range(len(arra)):
    if (arra[i] == ele):
        for j in range(i+1,len(arra)):
            arra[j-1] = arra[j]
        arra = arra[:-1]
        break

for i in range(0,len(arra)):
    print(arra[i], end =" ")
