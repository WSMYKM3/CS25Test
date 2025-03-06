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

