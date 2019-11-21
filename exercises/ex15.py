from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r." % filename
print txt.read()

print "Type the filename again!"
file_again = raw_input('> ')

txt_again = open(file_again)
print txt_again.read()

txt_write = open(file_again, "a")
txt_new = raw_input("Enter your content\n")
txt_write.write("{}\n".format(txt_new))


