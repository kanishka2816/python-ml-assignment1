# Open the file in read mode ('r')
file_path = 'example.txt'  # Replace with your file path
try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Print the content to the console
        print(content)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except IOError:
    print(f"An error occurred while reading the file {file_path}.")
