#one more input method you can use to pass variables to a script
#(script being another name for your .py fi les).
#when run from the terminal

from sys import argv

#argv is the argument variable
#This variable holds the arguments you pass to your Python script
#when you run it. In the exercises you will get to play with this more and see what happens.

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is : ", first
print "Your second variable is: ", second
print " Your third variable is: ", raw_input()