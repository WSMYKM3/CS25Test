# # Open the original file with UTF-8 encoding
# with open('WordsList.txt', 'r', encoding='utf-8') as file:
#     words = file.read().splitlines()  # Read the lines and split by newline

# # Add a comma after each word
# words_with_commas = [word + ',' for word in words]

# # Save the modified words into a new file
# with open('WordsList.txt', 'w', encoding='utf-8') as file:
#     file.write('\n'.join(words_with_commas))  # Join words with commas and write to the file


# Open the original file with UTF-8 encoding
with open('WordsList.txt', 'r', encoding='utf-8') as file:
    words = file.read().splitlines()  # Read the lines and split by newline

# Add double quotes and a comma after each word
words_with_quotes_and_commas = [f'"{word}",' for word in words]

# Save the modified words into a new file
with open('WordsList.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(words_with_quotes_and_commas))  # Join words with quotes and commas, then write to the file
    
#######this script is also in HTMLCSSJS\AutoComplete\split.py

# encoding='utf-8
# What It Does:
# It tells Python to decode the contents of the file using the UTF-8 character encoding.

# UTF-8 is the most common text encoding used today. It supports nearly all characters and symbols in the world.

# Why It Matters:
# Text files are stored as bytes on disk. To turn those bytes into readable characters, Python needs to know what character encoding was used when the file was saved. If you use the wrong encoding:

# Some characters might become garbled (e.g., é might show up as Ã©)

# Or it may raise a UnicodeDecodeError.