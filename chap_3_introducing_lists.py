''' Adding new elements to lists '''
# use .append to add an item to the end
# like lst.append('this')
lst = []
# .insert(index, item)
lst.insert(0, 'that')

''' Deleting item from list '''
# knowing the position to delete
del lst[0]
# del lst[3]

# .pop() --> 'returns' and 'removes' the last element from the list 
lst.append('pop this')
print(lst.pop())

# also can pop(index #)
# lst.pop(4) or lst.pop(0)

''' Remove by value 
    only removes the first occurrence of the value, use a loop to remove the rest if any 
'''
# .remove(value)
lst.remove('pop this')

''' Sort lists '''
''' permenant sorts '''
lst.sort() # sort alphabeticaly  
lst.sort(reverse=True) # sort reverse
''' temporary sort '''
sorted(lst) # doesn't effect the original lst
lst.reverse() # reverses the orginal list 
len(lst)




