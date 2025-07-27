Set1 = {1,3,5,7,9,0}
Set2 = {2,4,6,8,10,0,8,4,1}

#Union
union_set = Set1.union(Set2)
print(union_set)

#Intersection - Prints out the common elements 
intersection_set = Set1.intersection(Set2)
print(intersection_set)

#Diffrence
print(Set1.difference(Set2))