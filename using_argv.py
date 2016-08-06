from sys import argv

script, user_name = argv

#Notice though that we make a variable prompt that is set to the prompt we want, and we give
#that to raw_input instead of typing it over and over.
prompt = '$'

print "HI I am %s, I'm the %s." % (user_name, script)
print "I'd like to ask you afew questions."
print "Do you like  %s?" % (user_name)
likes =raw_input(prompt)

print "Where do you live %s?" % (user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
