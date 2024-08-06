# Number of Fibonacci numbers to generate
n = 10

# Starting values
a, b = 0, 1

# List to store the Fibonacci sequence
fib_sequence = []

# Generate the Fibonacci sequence using a for loop
for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

# Print the generated Fibonacci sequence
print("The first 10 numbers in the Fibonacci sequence are:")
print(fib_sequence)
