import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        # exit 1 means something went wrong
        sys.exit(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1], newline='') as csvfile:
        # Creates a DictReader object that interprets each row of the CSV as a dictionary
        # with form like{'name':'abc', 'STR1':'ass','STR2':'sss', ...}
        reader = csv.DictReader(csvfile)

        database = list(reader)  # Reads the entire CSV into a list of dictionaries

        # Exclude 'name', contains the list of column headers (e.g. ['name', 'AGAT', 'AATG', 'TATC']).
        str_sequences = reader.fieldnames[1:]
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    str_counts = {}
    for str_seq in str_sequences:
        str_counts[str_seq] = longest_match(dna_sequence, str_seq)

    # TODO: Check database for matching profiles
    for person in database:
        match = True
        for str_seq in str_sequences:

            # here to compare
            if int(person[str_seq]) != str_counts[str_seq]:
                match = False
                break
        if match:
            print(person["name"])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring"
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    return longest_run


main()
