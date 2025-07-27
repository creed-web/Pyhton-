#Sets are denoted by {}
#set cannot use a list inside them because lists are mutable, hence hashable however an set is an unhashable data type but we can definetly use tupples.

my_set = {1,2,3,4,5,8}
print(type(my_set))


#set operations
my_set.add(11)
my_set.remove(2)