#Sets are denoted by {}
#set cannot use a list inside them because lists are mutable, hence hashable however an set is an unhashable data type but we can definetly use tupples.

my_set = {1,2,3,4,5,8}
print(type(my_set))


#set operations
my_set.add(11)
my_set.remove(2)
my_set.discard(91) #This method basically discards that number means that if the number is in the set it will get removed if it is not there it will just ccontinue no error will be thrown 
# There are many other things u can do explore while u practice


