def string_to_char_list(string):
    """Convert a string into a list of its characters."""
    char_list = [char for char in string]
    return char_list

# Example usage:
if __name__ == "__main__":
    input_string = "Hello, World!"
    
    # Convert the string to a list of characters
    char_list = string_to_char_list(input_string)
    
    # Print the result
    print(f"The string '{input_string}' converted to a list of characters:")
    print(char_list)
