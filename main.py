# Step 1: Take an input number and create a list of odd numbers below the input value
num = int(input("Enter a number: "))

# List of odd numbers under the input value
odd_numbers = [i for i in range(1, num) if i % 2 != 0]
print("List of odd numbers under", num, ":", odd_numbers)

# Step 2: Create a list of fruits and capitalize the first letter of each element
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Capitalizing the first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("List of fruits with the first letter capitalized:", capitalized_fruits)
