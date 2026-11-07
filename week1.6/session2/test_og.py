from image import Image

pic = Image()
create = Image.create_pixels(pic, 5, 10)
print(create)

with open('peppers.pgm','r') as file:
    parse = Image._parse_pixels(pic, file)
    write = Image._write_pixels(pic, file)

print(parse)
print(write)

print(Image.get(pic, 3, 7))
set = Image.set(pic, 3, 7, 45)
print(Image.get(pic, 3, 7))
