string = "24e3hih7"
print ''.join([chr(ord(string[c]) - c) for c in range(len(string))])
