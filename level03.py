import re
mess = open("./extras/level03.txt", "r").read()
print ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', mess))
