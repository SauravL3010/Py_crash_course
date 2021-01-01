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

