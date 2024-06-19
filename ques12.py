# Prompt the user to enter a number
number = input("Please enter a number: ")

# Initialize a variable to store the sum of the digits
sum_of_digits = 0

# Iterate over each character in the string representation of the number
for digit in number:
    # Convert the character to an integer and add it to the sum
    sum_of_digits += int(digit)

# Print the sum of the digits
print(f"The sum of the digits of the number {number} is: {sum_of_digits}")
