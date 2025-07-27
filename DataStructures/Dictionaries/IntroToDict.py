#Empty curly brakets are syntax of dictionaries, dictionaries are unordered, mutable, and indexed collections of key-value pairs. They are used to store data in a way that allows fast lookup by key, not by position like lists or tuples
demo_dict = {"student":"Varun", "course":"B.Tech CSE", "Department":"SOET", "College":"JNU"}
print(type(demo_dict))

#Accesing dictionary elements-
print(demo_dict['course'])
demo_dict["student"] = "Divya Pratap"
demo_dict["Address"] = "Jaipur,Raj" #Adding new key
del demo_dict["Department"] #Deleting a key
print(demo_dict)