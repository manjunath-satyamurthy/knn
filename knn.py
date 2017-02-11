import pickle, math, time
from PIL import Image, ImageDraw


k = int(raw_input("Enter the value for k\n"))

base = Image.open('points.png')

draw =ImageDraw.Draw(base)

red = (250,0,0)
green = (0, 250, 0)
point_colours = [red, green]

training_data = pickle.load(open("training_data", "rb"))
test_data = pickle.load(open("test_data", "rb"))

print len(test_data)

for unknown in test_data:
	nearest = {}
	for points in training_data:
		labelled_point = points[0]
		distance = math.sqrt((labelled_point[0] - unknown[0])**2 + (labelled_point[1] - unknown[1])**2)

		if len(nearest) < k:
			nearest[distance] = [points, unknown]
		else:
			distances = nearest.keys()
			distances.sort()
			for temp_dist in distances:
				if distance < temp_dist:
					del nearest[temp_dist]
					nearest[distance] = [points, unknown]

	class_0, class_1 = 0, 0
	unknown_class = None

	for distance in nearest.keys():
		if nearest[distance][0][1] == 0:
			class_0 += 1
		else:
			class_1 += 1

	if class_0 > class_1:
		unknown_class = 0
	else:
		unknown_class = 1

	x = unknown[0]
	y = unknown[1]
	x1 = x + 9
	y1 = y + 9
	draw.rectangle([x, y, x1, y1], fill=point_colours[unknown_class])
	base.save('points.png')

del draw

base.save('points.png')
