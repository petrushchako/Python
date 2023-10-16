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
print(data["people"][1]["name"])



with open("jsonFiles/sample.json", 'r') as file:
    json_data = file.read()
    sampleJSON = json.loads(json_data)

print("\n"*3,type(sampleJSON))
print(sampleJSON)