#Write a program to detect double spaces in a string
userInput = input("Enter something: ")
spaceDetector = userInput.find("  ")

if spaceDetector == -1:
    print("No double spaces found")
else:
    while spaceDetector != -1:
        print(f"double spaces are on indexes {spaceDetector}")
        spaceDetector = userInput.find("  ", spaceDetector + 1)

