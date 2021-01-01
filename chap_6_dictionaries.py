# key-value pairs 
alien_0 = {}
# adding new pairs
alien_0['speed'] = 'medium'

alien_0['x_pos'] = 0
alien_0['y_pos'] = 0

if alien_0['speed'] == 'slow':
    x_increment = 3
elif alien_0['speed'] == 'fast':
    x_increment = 2
else:
    x_increment = 1

alien_0['x_pos'] += x_increment

# delete
del alien_0['speed']

print(alien_0)

''' Best practice, god practice to leave a ',' after the last pair too '''
fav_languages = {
    'Sarah' : 'c',
    'Liam' : 'Python',
    'Mark' : 'c++',
}

''' Refer the rest from thr book ''' # --> dic in lists and dic in dic
webpage = 'http://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/No.Starch.Python.Oct_.2015.ISBN_.1593276036.pdf'
page_no = 110

''' extract stuff form dic '''
# key, value
for k, v in alien_0.items():
    print(k, v)

# key
for k in alien_0.keys():

# values
for v in alien_0.values():

# all the above return a list, so, could use, sorted(lst) or slicing etc. 
    

