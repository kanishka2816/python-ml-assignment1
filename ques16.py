def count_character_frequencies(input_string):
    # Create an empty dictionary to store character frequencies
    frequency_dict = {}

    # Iterate over each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

# Example usage:
if __name__ == "__main__":
    # Input string
    input_string = "hello world"
    
    # Get the character frequencies
    frequencies = count_character_frequencies(input_string)
    
    # Print the results
    for char, freq in frequencies.items():
        print(f"'{char}': {freq}")
