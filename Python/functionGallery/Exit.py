# echo $?   to check the exit status

#  sys.exit(1)
# Meaning: Abnormal/Error termination.
# Use when: The program encounters an error or problem and needs to exit.
# Effect: Returns an exit status code of 1, which is a general signal of failure to the OS or calling process.

# sys.exit(0)
# Meaning: Normal/Successful termination.
# Use when: Your program finishes without any error.
# Effect: Returns an exit status code of 0, which tells the OS or shell that everything went fine.

import sys

if len(sys.argv) != 2: # Checks if exactly 1 argument (besides the script name) was passed
    print(f"Missing command-line argument")
    sys.exit(1)

print(f"Hello, {sys.argv[1]}")
sys.exit(0)    