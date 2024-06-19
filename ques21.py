def count_occurrences_loop(elements, target):
    # Initialize a counter to 0
    count = 0
    
    # Iterate over each element in the list
    for element in elements:
        # If the element matches the target, increment the count
        if element == target:
            count += 1
    
    return count

# Example usage:
if __name__ == "__main__":
    # Input list and target element
    elements = [1, 2, 3, 2, 4, 2, 5, 2, 6]
    target = 2
    
    # Count occurrences of the target element
    count = count_occurrences_loop(elements, target)
    
    # Print the result
    print(f"The element {target} occurs {count} times in the list.")
