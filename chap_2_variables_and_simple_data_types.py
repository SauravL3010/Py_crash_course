# Variable rules 
# 1--> variable names do not start with numbers
# 2--> do not use python keywords

''' Uppper, Lower, Title '''
str1 = "this is love"
str2 = 'Admire this'
print(str1.upper())
print(str2.lower())
print(str1.title()) # title case

''' Concatenation '''
str3 = 'rich dad'
str4 = 'poor dad'
book_title = str3.title() + ' ' + str4.title() + ' ' + 'A book on smart fincance'
print(book_title)

''' WhiteSpace \t (Tab) \n (New Line)'''
str5 = 'Determination is doing something'
str6 = "when you don't feel like doing it"
qoute_1 = str5 + ' ' + '\n\t' + str6
print(qoute_1)
