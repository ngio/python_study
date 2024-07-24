""" Working With Lists  """

# 1. Creating a List
# To conjure a list into being:

# A list of mystical elements
elements = ['Earth', 'Air', 'Fire', 'Water']

# 2. Appending to a List
# To append a new element to the end of a list:

elements.append('Aether')

# 3. Inserting into a List
# To insert an element at a specific position in the list:

# Insert 'Spirit' at index 1
 elements.insert(1, 'Spirit')

# 4. Removing from a List
# To remove an element by value from the list:

elements.remove('Earth')  # Removes the first occurrence of 'Earth'

# 5. Popping an Element from a List
# To remove and return an element at a given index (default is the last item):

last_element = elements.pop()  # Removes and returns the last element

# 6. Finding the Index of an Element
# To find the index of the first occurrence of an element:

index_of_air = elements.index('Air')

# 7. List Slicing
# To slice a list, obtaining a sub-list:

# Get elements from index 1 to 3
sub_elements = elements[1:4]

# 8. List Comprehension
# To create a new list by applying an expression to each element of an existing one:

# Create a new list with lengths of each element
lengths = [len(element) for element in elements]

# 9. Sorting a List
# To sort a list in ascending order (in-place):

elements.sort()

10. Reversing a List
To reverse the elements of a list in-place:

elements.reverse()




