def get_int():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass


height = get_int()

# here, I cannot replace to for i in range(height) because it start from 0 and hashed and space in first line is all empty
for i in range(1, height + 1):
    space = " " * (height-i)
    hashes = "#" * i
    print(f"{space}{hashes}  {hashes}")