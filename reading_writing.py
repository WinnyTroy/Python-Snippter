# Opening that file in our script and printing it out.

from sys import argv

# use of argv to get the filename
script, filename = argv


# #when using raw_input to get the file name
# prompt = '> '
# filename = raw_input(prompt)

#give it a variable, to help recalling it.
text = open(filename)

#Print out the variable
print "Here's your file %r:" % filename

#Read the file read
print text.read()

#closing the text file
text.close()

print "Type the filename again: "

#prompting the user for input
file_again = raw_input("$")

#opening the file
text_again = open(file_again)

#reading the file and printing it out
print text_again.read()

#closing the text_again file
text_again.close()