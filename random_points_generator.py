from random import randint
from PIL import Image, ImageDraw
import pickle

a = 2
b = -130
width = 640
height = 480

number_of_pixels = width*height

red = (250,0,0)
green = (0, 250, 0)
white = (255, 255, 255)

point_colours = [red, green]

base = Image.new('RGB', (width, height), white)

draw =ImageDraw.Draw(base)

number_of_points = 500

training_data = []
test_data = []

for _ in range(number_of_points):
	x = randint(0, 640)
	y = randint(0, 480)
	x1 = x + 8
	y1 = y + 8

	if y > (a*x+b):
		colour = red
		index = 0
	else:
		colour = green
		index = 1

	training_data.append([(x, y), index])
	draw.ellipse([x, y, x1, y1], fill=colour)

for _ in range(100):
	x = randint(0, 640)
	y = randint(0, 480)	
	x1 = x + 9
	y1 = y + 9
	test_data.append([x, y])
	draw.rectangle([x, y, x1, y1], fill=(0, 0, 0))

del draw
base.save('points.png')

training_file = open("training_data","wb")
test_file = open('test_data', 'wb')

pickle.dump(training_data, training_file)
training_file.close()

pickle.dump(test_data, test_file)
test_file.close()
