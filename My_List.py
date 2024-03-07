# Create an empty list
my_list = []

# Add elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert a value at the second position
my_list.insert(1, 15)

# Extend the list with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of the value 30
index_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_30}")

# Final content of my_list
print(f"my_list: {my_list}")
# Calculate the average of the list
average = sum(my_list) / len(my_list)
print(f"The average of my_list is: {average}")

# Find the maximum and minimum value in the list
max_value = max(my_list)
min_value = min(my_list)
print(f"The maximum value in my_list is: {max_value}")
print(f"The minimum value in my_list is: {min_value}")

# Count the occurrence of 30 in the list
count_30 = my_list.count(30)
print(f"The number 30 appears {count_30} times in my_list")
