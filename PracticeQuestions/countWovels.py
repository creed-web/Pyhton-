#Count Vowels in a String

inputString = str(input("Enter a word/sentence: "))
vowels = ["a","e","i","o","u"]

if inputString == vowels:
    for finding in inputString(1,-1):
       finding =  str(inputString.find(vowels))
print(finding)
        
