people = {
    "Sam": "23125654",
    "David": "44133",
    "Tom": "254784"
}

name = input("Name: ").strip().lower().title()  # Convert input to lowercase for comparison
#strip()	Removes whitespace from both sides
#lstrip()	Removes whitespace from the left side only
#rstrip()	Removes whitespace from the right side only
#title() is for Captialize first letter
#so that if i input sam, will return Sam

if name in people:
    print(f"Number: {people[name]}")
else:
    print("Not Found")