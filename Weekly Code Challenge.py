#Write a program that accepts user input to create a list of integers.
#list_of_integers
numbers = input("enter a numbers separeteded by ,:").split(',')

# Convert the list of strings to a list of integers.
list_of_integers = [int(number) for number in numbers]
# Calculate the sum of the integers.
total_sum = sum(list_of_integers)
# Print the sum.
print(total_sum)


#Create a tuple containing the names of five of your favorite books.

favorite_books = ("Young Adult", "Non-Fiction", "Classic", "Mystrey", "Fantasy")

#use a for loop to print each book name on a separate line.

for book in favorite_books:
    print(book)
    


#Write a program that accepts user input to create two sets of integers.
#two sets of integers
set1 =set (input("enter numbers separated by commas").split(', '))
print("set1 = " , set1)
set2 =set (input("enter numbers separated by commas").split(', '))

print("set2 = " , set2)

# #create a new set that contains only the elements that are common to both sets.
set3 =set1.intersection(set2) 


#Create a program that stores a list of words.

set3 = set1.intersection(set2)



#Create a program that stores a list of words.

words = input("words").split()

#use list comprehension to create a new list that contains only the words that have an odd number of characters.

odd_words = [word for word in words if len(word) % 2 != 0]
print(odd_words)










