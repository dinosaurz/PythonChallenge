import urllib
import re

seed = "12345"  # original
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

seed = "8022"
for i in range(400):
    text = urllib.urlopen(url + seed).read()
    seed = ''.join(re.findall(r'nothing is (\.+)', text))

    try:
        int(seed)
        print "    Next:", seed
    except:
        print "    Last:", text
        break
