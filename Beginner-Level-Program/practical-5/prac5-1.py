"""Aim : Program related to study of string functions

1) declare a string word which contains value "Hello World 11".
2) print the string with a message "String:"value.
3) print the first and 8th character of the string.
4) count the number of l,o,h in the string
5) print only the number in the string using slice operator
6) print 1st, 1st three, last three and all except last three characters using slice operator
7) split the string at the spaces
8) start with'H' or 'h'  and ends 'd' or 'x' or '1'
9) replace number with your name
10) print your name 10 times
11) print the string in different cases like uppercase,lowercase, capitailze(sentence case), title case and toggle case
12) Identify whether a string is in which case either upper case or lower case

"""
print('Program related to study of string functions')
print('-'*40)
word='hello world 11'
print(word)
print('1st Letter:',word[0])
print('8th Letter:',word[7])
print('Length of a string:',len(word))
print('Count of l:',word.count('l'))
print('Count of o:',word.count('o'))
print('Count of h:',word.count('h'))
#print('Count of x:',word.count('x'))
print('Roll no:',word[12:])
print('First letter:',word[0])
print('First 3 letter:',word[0:3])
print('Last 3 letter:',word[11:])
print('All letter (Except Last 3):',word[0:11])
print('Split at whitespace:',word.split(' '))
#print(word)
print('Starts with H:',word.startswith('H'))
print('Starts with h:',word.startswith('h'))
print('Ends with d:',word.endswith('d'))
print('Ends with x:',word.endswith('x'))
print('mudassar '*10)
print('Replace roll no with name:',word.replace('11','Mudassar'))
print('Uppercase:',word.upper())
print('Lowercase:',word.lower())
print('Capitalize:',word.capitalize())
print('Sentence Case:',word.title())
print('Swap case(toggle):',word.swapcase())
#others
print('String contains Numbers:',word.isalnum())
print('1234 contains Numbers:','1234'.isalnum())
print('String contains characters:',word.isalpha())
print('abcd contains characters:','abcd'.isalpha())
print('String contains digit:',word.isdigit())
print('String is in Uppercase:',word.isupper())
print('String is in Lowercase:',word.islower())
print('String is empty:',word.isspace())