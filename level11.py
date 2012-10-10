import Image

orig = Image.open("./extras/cave.jpg")
w, h = orig.size

sep = Image.new("RGB", (w / 2, h))

for i in range(w * h):
    y, x = divmod(i, w)
    pixel = orig.getpixel((x, y))

    if i % 2:
        sep.putpixel((x / 2, y / 2 + h / 2), pixel)
    else:
        sep.putpixel((x / 2, y / 2), pixel)

sep.save("./extras/level11.jpg")
