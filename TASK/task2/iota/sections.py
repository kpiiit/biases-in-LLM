# Initialize an empty set to store unique keywords
unique_keywords = set()

# Open the file
with open('extracted_data.txt', 'r') as file:
    # Read lines from the file
    for line in file:
        # Split the line into words
        words = line.strip().split()

        # Extract the first word (the keyword)
        keyword = words[0]

        # Add the keyword to the set
        unique_keywords.add(keyword)

# Convert the set to a list and sort it
unique_keywords_list = sorted(list(unique_keywords))

# Convert the list to a string with quotes around each keyword
keywords_string = ', '.join(['"' + keyword + '"' for keyword in unique_keywords_list])

# Print the string
print(keywords_string)
