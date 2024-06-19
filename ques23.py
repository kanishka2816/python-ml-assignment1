def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the formula
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the formula
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Temperature Conversion Program")
    print("Choose the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    # Get the user's choice
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        
    elif choice == '2':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        
    else:
        print("Invalid choice! Please enter 1 or 2.")

# Call the main function
if __name__ == "__main__":
    main()
