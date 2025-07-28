#The map() function applies a given function to each item in an iterable (like a list, tuple, etc.) and returns a map object (which you can convert to a list).

numbers = [1,2,3,4,5,6,7,8,9]
square = list(map(lambda x:x*x,numbers))
print(square)