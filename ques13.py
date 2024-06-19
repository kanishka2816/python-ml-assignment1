from datetime import datetime

# Prompt the user to enter their birth year
birth_year = int(input("Please enter your birth year: "))

# Get the current year
current_year = datetime.now().year

# Calculate the user's age
age = current_year - birth_year

# Print the user's age
print(f"Your age is: {age}")
