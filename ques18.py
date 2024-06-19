def are_anagrams(string1, string2):
    # Remove any whitespace and convert to lowercase to handle case insensitivity
    normalized_string1 = ''.join(string1.split()).lower()
    normalized_string2 = ''.join(string2.split()).lower()
    
    # Check if the sorted versions of the strings are equal
    return sorted(normalized_string1) == sorted(normalized_string2)

# Example usage:
if __name__ == "__main__":
    # Input strings
    string1 = "Listen"
    string2 = "Silent"
    
    # Check if they are anagrams
    result = are_anagrams(string1, string2)
    
    # Print the result
    if result:
        print(f'"{string1}" and "{string2}" are anagrams.')
    else:
        print(f'"{string1}" and "{string2}" are not anagrams.')
