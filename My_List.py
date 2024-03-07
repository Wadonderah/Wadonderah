```python:My_List.py
# Create an empty list called My_list
My_list = []

# Append the following elements to My_list: 10, 20, 30, 40
My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)

# Insert the value of 15 at the second position of the list
My_list.insert(1, 15)

# Extend My_list with another list: [50, 60, 70]
My_list.extend([50, 60, 70])

# Remove the last element from My_list
My_list.pop()

# Sort My_list in ascending order
My_list.sort()

# Find and print the index of the value of 30 in My_list
index_30 = My_list.index(30)
print(f"The index of 30 in My_list is: {index_30}")
