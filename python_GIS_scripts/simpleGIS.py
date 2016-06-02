"""
simpleGIS.py

Complete exercise from Joel Lawheads "Geospatial Analysis with Python, 2nd Ed". (2015). Pages 39-47.

Hadleigh Thompson
June 2016
"""


import turtle as t

name = 0
points = 1 
pop = 2

state = ["Colorado", [[-109,37], [-109,41], [-102,41], [-102, 37]], 5187582]

cities = []
cities.append(["Denver", [-104.98, 39.74], 632265])
cities.append(["Boulder", [-105.27, 40.02], 98889])
cities.append(["Durnago", [-107.88, 37.28], 17069])

map_width = 400.
map_height = 300.

min_x = 180.
max_x = -180.
min_y = 90.
max_y = -90.

for x,y in state[points]:
	if x < min_x:
		min_x = x
	elif x > max_x:
		max_x = x

	if y < min_y:
		min_y = y
	elif y > max_y:
		max_y = y

dist_x = max_x - min_x
dist_y = max_y - min_y

x_ratio = map_width / dist_x
y_ratio = map_height / dist_y

def convert_points(point):
	lon = point[0]
	lat = point[1]
	x = map_width - ((max_x - lon) * x_ratio)
	y = map_height - ((max_y - lat) * y_ratio)

	x = x - (map_width/2.)
	y = y - (map_height/2.)

	return[x,y]

t.up()
first_pixel = None

for point in state[points]:
	pixel = convert_points(point)

	if not first_pixel:
		first_pixel = pixel

	t.goto(pixel)
	t.down()

t.goto(first_pixel)
t.up()
t.goto([0,0])
t.write(state[name], align="center", font=("Arial", 16, "bold"))

for city in cities:
	pixel = convert_points(city[points])

	t.up()
	t.goto(pixel)

	t.dot(10)

	t.write(city[name] + ", pop: " + str(city[pop]), align='left')
	t.up()

t.pen(shown=False)
t.done()































