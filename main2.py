import random

# The randrange(100) selects any number from between 1 and 100 (100 not included)
x = random.randrange(100)
print (x)

colours = ['red', 'green']
#chooses one from the list randomly
colour = random.choice(colours)

#random of integers: both sides included
print(random.randint(0, 5))

#returns a random value between 0 and 1 (0 is inclusive and 1 is exclusive) - [0, 1)
print(random.random())

#returns with steps, not including the stop
print(random.randrange(0,100, 5))
#---------------------------PIL--------------------------------
from PIL import Image, ImageDraw

# print the image details
image = Image.open("magic_city.jpg"
print(image.format)
print(image.size)
print(image.mode

#rotate the image
new = image.rotate(60)

#crop the image
dimensions = (100, 100, 500, 500)
cropped = image.crop(dimensions)
cropped.show()

#creating new canvas
new_image = Image.new("RGB", (200, 300), (0, 0, 0)) # create image
draw = ImageDraw.Draw(new_image)                    # on image create picture for drawing

draw.line((0, 300, 200, 0), fill=(0, 255, 0), width=3) # draw line

draw.ellipse((x0, y0, x1, y1), fill=color, width=n)

draw.rectangle((x0, y0, x1, y1), fill=color, outline=color)

draw.polygon(((x0, y0), (x1, y1), (x2, y2), (x3, y3), (x4, y4)), color)

new_image.save('green_line.png', "PNG")