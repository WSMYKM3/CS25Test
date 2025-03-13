def get_int():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass  # Ignore invalid input and re-prompt

if __name__ == "__main__":
    height = get_int()
    
    for i in range(1, height + 1):
        left_spaces = " " * (height - i)
        hashes = "#" * i
        print(f"{left_spaces}{hashes}  {hashes}")
