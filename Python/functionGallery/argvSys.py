from sys import argv

if len(argv) == 2: # Checks if exactly 1 argument (besides the script name) was passed
    print(f"Hello, {argv[1]}")##this argvSys.py is the first, so if python argvSys.py David, David is the argv[1]
else:
    print("Hello, world")    
    