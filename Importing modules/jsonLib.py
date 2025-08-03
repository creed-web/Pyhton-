#Data Serialization
import json
data = {'name':'Varun', 'age':'19', 'course':'B.Tech RPA'} ## The default data type of thisi is dictionary
print(type(data))

json_str = json.dumps(data) #this converts the data into string
print(json_str)
print(type(json_str))

parsed_json = json.loads(json_str) #thos converts the data to dictionary
print(parsed_json)
print(type(parsed_json))