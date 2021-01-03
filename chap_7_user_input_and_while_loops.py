''' Prompt '''
question = {1 : 'what is ur name'}
ask = input(question[1])

''' Take in numerical input '''
age = int(input('age'))
if age > 18:
    print('Adult')

''' Using while loops to ask repetetive question '''
prompt = 'enter age:'
prompt += '\nenter q to end the program'

error_1 = 'Enter a valid # or q to exit'
error_2 = 'Enter q to exit'

ask_age = ''

while ask_age != 'q':
    if aak_age != 'q':
        ask_age = input("Enter age")
    print(ask_age)

''' Using Flags '''
flag = True
while flag:
    # do somthing
    if #condition:
        flag = False
        #exits loop 

''' break loop '''
# break, exits the enitre loop
while flag:
    if #condition:
        break


''' continue '''
#  skips anything after continue in the loop, increments by one.
counter = 0
while counter < 10:
    if counter % 2 == 0:
        continue
    counter += 1
    print(counter) 

