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
