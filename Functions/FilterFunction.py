#This function is used to filter out elements from a list 

def evenOrOdd(nums):
    if nums % 2 ==0:
        return True
    

lst = [1,2,3,4,5,6,7,8,9]
evenList = list(filter(evenOrOdd,lst))
print(evenList)