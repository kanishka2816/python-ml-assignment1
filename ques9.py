# Prompt the user to enter the main string
main_string = input("Please enter the main string: ")

# Prompt the user to enter the substring
substring = input("Please enter the substring to search for: ")

# Check if the substring is present in the main string using the 'in' keyword
if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")
