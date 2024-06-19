def convert_to_title_case(input_string):
    # Use the title() method to convert the string to title case
    title_case_string = input_string.title()
    return title_case_string

# Example usage:
if __name__ == "__main__":
    # Input string
    input_string = "hello world! this is a test string."
    
    # Convert to title case
    title_cased_string = convert_to_title_case(input_string)
    
    # Print the result
    print(title_cased_string)
