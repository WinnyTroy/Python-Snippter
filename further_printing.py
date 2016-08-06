# from sys import argv
#
# script, filename = argv
#
# print "We're going to erase %r. " % filename
# print "If you dont want it, hit CNTRL-C"
# print "If you dont want that, hit RETURN."
#
# raw_input("?")
#
# print " opening the file..."
# target = open(filename, 'r+')
#
# print "Truncating the file. Goodbye!"
# target.truncate()
#
# print "Now I'm going to ask you for three lines."
#
# line1 = raw_input("line1: ")
# line2 = raw_input("line2: ")
# line3 = raw_input("line3: ")
#
# print "I'm going to write these to the file."
#
# target.write(line1)
# target.write("\n")

# creating a function - to call afterwards

def ready():
    # opening the files in the reading mode
    m = open('name.txt', 'r+')
    k = m.read()
    # creating a list to hold the new data in the file
    l = []
    # appending the list so that it reads from the files string
    l.append(k)
    print l

ready()