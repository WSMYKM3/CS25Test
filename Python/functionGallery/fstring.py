def get_name():
    return input("What's your name? ")  # Takes user input inside the function

name = get_name()  # No need to pass a parameter
print(f"Hello, {name}!")