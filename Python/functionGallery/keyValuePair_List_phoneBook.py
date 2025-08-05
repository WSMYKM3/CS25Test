people = [
    {"name":"ABC", "number":"1243341"},
    {"name":"cde", "number":"12433asd41"},
    {"name":"fgh", "number":"12433dsf41"},
]

name = input("Name: ")
for person in people:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}")
        break
else:
    print("Not Found")    