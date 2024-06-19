def find_min_max_builtin(numbers):
    # Use built-in min and max functions to find the smallest and largest numbers
    min_value = min(numbers)
    max_value = max(numbers)
    
    return min_value, max_value

# Example usage:
if __name__ == "__main__":
    # Input list of numbers
    numbers = [23, 1, 56, 3, 78, 0, -5, 22, 45]
    
    # Find the minimum and maximum values
    min_val, max_val = find_min_max_builtin(numbers)
    
    # Print the results
    print("Minimum value in the list is:", min_val)
    print("Maximum value in the list is:", max_val)
