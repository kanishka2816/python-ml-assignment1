def sum_of_numbers(numbers):
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over each number in the list
    for number in numbers:
        # Add each number to the total sum
        total_sum += number
    
    return total_sum

# Example usage:
if __name__ == "__main__":
    # Input list of numbers
    numbers = [10, 20, 30, 40, 50]
    
    # Calculate the sum of numbers
    result = sum_of_numbers(numbers)
    
    # Print the result
    print("The sum of the list is:", result)
