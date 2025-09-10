#Remove all occurences of an element in an array

def remove_all_Occurences(arr,ele):
    k = 0
    for i in range(len(arr)):
        if arr[i] != ele:
            arr[k] = arr[i]
            k += 1
    return k

arr = [3,1,2,3,4,3,5]
ele = 3

k = remove_all_Occurences(arr, ele)

print(f"K:{k}")
print(f"New arr: {arr[:k]}")