import json

people_string = '''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "123456789",
            "emails" : ["j.smith@gmail.com", "john.smith@gmail.com"],
            "has_license" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "987654321",
            "emails" : null,
            "has_license" : true
        }
    ]
}
'''

data = json.loads(people_string)
print(type(data))
print(data)
#print(data["people"][1]["name"])
#Itareta through objects in people list
for person in data["people"]:
    for key, value in person.items():
        print("{} : {}".format(key,value))

#Access names only
print("\nAccess names only:")
for person in data["people"]:
    print("\t",person["name"])


with open("jsonFiles/sample.json", 'r') as file:
    json_data = file.read()
    sampleJSON = json.loads(json_data)

print("\n"*3,type(sampleJSON))
print(sampleJSON)

#modify JSON
sampleJSON['grades']['math'] = 85
print(sampleJSON)
with open("jsonFiles/sample.json", "w") as file:
    json.dump(sampleJSON, file, indent=4)

#Dumps example
print("\njson.dumps(indent=4, sort_keys=True) example:")
jsonDumpsExample = json.dumps(sampleJSON, indent=4, sort_keys=True)
print(jsonDumpsExample)