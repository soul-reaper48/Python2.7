from sys import argv

script, user_name = argv
prompt = '> '

print "%s is executing %s" % (user_name, script)
print "I'd like to ask a few questions"
print "Is your name %s ? " % user_name
likes = raw_input(prompt)

print "Where do you live?"
lives = raw_input(prompt)

print """
Alright, so you said %r about your name.
You live in %r. Not sure where that is.
""" % (likes, lives)
