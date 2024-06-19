import string

def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translation_table = str.maketrans('', '', string.punctuation)
    
    # Use the translate method to remove all punctuation
    no_punctuation_string = input_string.translate(translation_table)
    
    return no_punctuation_string

# Example usage:
if __name__ == "__main__":
    # Input string
    input_string = "Hello, world! This is a test string with punctuation: @#&*()."
    
    # Remove punctuation
    cleaned_string = remove_punctuation(input_string)
    
    # Print the result
    print("Original String: ", input_string)
    print("String without Punctuation: ", cleaned_string)
