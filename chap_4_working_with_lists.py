''' Range '''
''' in range(start, end(not included), skip_by(optional)) '''
for _ in range(2, 11, 2):
    print(_) # prints even no's only 

''' Make a list out of range() '''
lst1 = list(range(1, 5))
print(lst1)

''' max(lst), min(lst), sum(lst) '''

''' List Comprehension '''
squares = [values**2 for values in range(1, 6)]
print(squares)

''' Slicing and copying lists '''
lst1[:] # copy
lst1[-3:]

''' Tuples are immutable '''
''' But they can be sliced and concatenated '''

