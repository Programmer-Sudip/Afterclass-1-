# Define the file name
file_name = 'example.txt'

# Step 1: Read the content of the file
file = open(file_name, 'r')
print("Read mode:")
print(file.read())
file.close()

# Step 2: Write new content to the file
file = open(file_name, 'w')
file.write("This is the new content that will overwrite the original content.\n")
file.close()



# Step 3: Read and print the new content
file = open(file_name, 'r')
print("\nContent after writing new content:")
print(file.read())
file.close()

# Step 4: Append content to the file
file = open(file_name, 'a')
file.write("This content will be appended to the end of the file.\n")
file.close()



# Step 5: Read and print the final content
file = open(file_name, 'r')
print("\nContent after appending new content:")
print(file.read())
file.close()
