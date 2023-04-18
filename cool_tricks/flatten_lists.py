# Flattening a list of lists

lst = [[1,2,3],[4,5],[6,7,8,9]]

flattened = [num for sublist in lst 
             for num in sublist]

print(flattened)


