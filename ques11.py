# Prompt the user to enter the number of terms
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the first two Fibonacci numbers
    fibonacci_series = []
    
    # Generate the Fibonacci series up to the n-th number
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    
    # Print the generated Fibonacci series
    print(f"The first {n} numbers in the Fibonacci series are: {fibonacci_series}")
