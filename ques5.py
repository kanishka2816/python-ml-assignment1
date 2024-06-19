# Ask the user for input
user_input = input("Please enter a string: ")

# Specify the file name
file_name = "output.txt"

# Open the file in write mode ('w') and write the input string to the file
with open(file_name, 'w') as file:
    file.write(user_input)

print(f"The input has been written to {file_name}")
