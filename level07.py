import Image

img = Image.open("./extras/oxygen.png")
print "Image info:", img.format, img.size, img.mode

# look only at the grey
y_begin = 0
while True:
    p = img.getpixel((0, y_begin))
    if p[0] == p[1] == p[2]:
        break
    y_begin += 1
x_end = 0
while True:
    p = img.getpixel((x_end, y_begin))
    if not p[0] == p[1] == p[2]:
        break
    x_end += 1

print "X End:", x_end, "Y Begin:", y_begin

message = []
for i in range(0, x_end, 7):
    p = img.getpixel((i, y_begin))
    message.append(chr(p[0]))

print ''.join(message)

message = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for char in message:
    print chr(char),
