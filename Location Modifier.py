import json

location_spot = input("Enter location spot (e.g. location1): ")
location_name = input("Enter the name of the new location: ")

with open("./spyfall/i18n/en.i18n.json", "r") as data_file:
    data = json.load(data_file)

data["locations"][location_spot] = location_name

with open("./spyfall/i18n/en.i18n.json", "w") as data_file:
    data_file.write(json.dumps(data))

# ####

with open("./spyfall/i18n/en.i18n.json", "r") as data_file:
    data = json.load(data_file)

for i in range(1,8):
    role = input("Enter a role: ")
    data["locations"]["roles"][location_spot][str(i)] = role

with open("./spyfall/i18n/en.i18n.json", "w") as data_file:
    data_file.write(json.dumps(data))