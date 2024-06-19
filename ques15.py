import csv

# Specify the path to your CSV file
file_path = 'data.csv'

# Open the CSV file
with open("file_path, mode='r', newline=") as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Print each row to the console
        print(', '.join(row))  # Adjust the separator as needed
