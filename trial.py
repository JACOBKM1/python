# Get the number of inputs from the user
m = int(input("Enter the number of integers you want to check: "))

# Initialize a list to store the results
results = []

# Loop to input and check 'm' numbers
for i in range(m):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        results.append(f"{num} is even")
    else:
        results.append(f"{num} is not even")

# Display the results
print("\nResults:")
for result in results:
    print(result)