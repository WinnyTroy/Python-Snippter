my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
inch = 1
centimeter = inch * 2.54
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "I need around %f", 5 * centimeter, "centimeters of clothline"

print "I said: %r." % x

print "I also said: '%s'." % y

print "If I add %d, %d, and %d I get %d" % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Mary had a little lamb."
print "Its fleece was whaite as %s. " % 'snow'
print "And everywhere that Mary went."


# prints out the period over the specified number
print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing", "That you could type up right",
                   " But it didnt sing", " So I said goodnight.")

days = "Mon \nTue \nWed \nThur \nFri"
months = "Jan /nFeb \nMar \nApril \nMay \nJune","\nJuly \nAug \nSept \nOct \nNov \nDec"
print "Here are the months of the year: ",  months

age = raw_input("How old are you?" )
