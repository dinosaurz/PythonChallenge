import re
import zipfile

folder = "./extras/"
index = folder + "90052"
myzip = zipfile.ZipFile(folder + "channel.zip", 'r')
history = []

while True:
    history.append(index)
    text = myzip.read(index + ".txt")
    index = folder + ''.join(re.findall('[0-9.]', text))

    if len(index) == 1:
        break

print ''.join([myzip.getinfo(i + ".txt").comment for i in history])
