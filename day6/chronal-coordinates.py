from progress.bar import Bar

data = open('day6/day6-input.txt', 'r').read().split('\n')

def manhattan_distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

coordinate_array = []
space_dim = (0,0)
for coordinate in data:
    x = int(coordinate.split(',')[0])
    y = int(coordinate.split(',')[1])
    coordinate_array.append((x,y))
    space_dim = (max(space_dim[0],x), max(space_dim[1],y))

space = [[[space_dim[0],(0,0)] for i in range(space_dim[0]+1)] for j in range(space_dim[1]+1)]

progress_bar = Bar("Processing Space ", max=len(coordinate_array)*(space_dim[0]+1)*(space_dim[1]+1))
for x in range(0,space_dim[0]+1):
    for y in range(0,space_dim[1]+1):
        for coordinate in coordinate_array:
            distance1 = manhattan_distance(coordinate, (x, y))
            distance2 = space[y][x][0]
            if distance1<distance2:
                #current coordinate is closer than closest coord for this point in space, update marker
                space[y][x] = [distance1, coordinate]
            elif distance1 == distance2:
                #current coordinate equidistant to another for this point of space, update marker
                space[y][x] = [distance1, -1, -1]
            else:
                #current coordinate is further from closest coord for this point of space, do nothing
                space[y][x] = [distance2, space[y][x][1]]
            progress_bar.next()
progress_bar.finish()

# identify coordinates with infinite area
infinite_area_coords = []
for x in range(0,space_dim[0]+1):
    if (space[0][x][1] not in infinite_area_coords):
        infinite_area_coords.append(space[0][x][1])
    if (space[space_dim[1]][x][1] not in infinite_area_coords):
        infinite_area_coords.append(space[space_dim[1]][x][1])
for y in range(0,space_dim[1]+1):
    if (space[y][0][1] not in infinite_area_coords):
        infinite_area_coords.append(space[y][0][1])
    if (space[y][space_dim[0]][1] not in infinite_area_coords):
        infinite_area_coords.append(space[y][space_dim[0]][1])

#
finite_area_coordinates = []
for coordinate in coordinate_array:
    if (coordinate not in infinite_area_coords):
        finite_area_coordinates.append(coordinate)

def area(space, coordinate):
    area = 0
    for x in range(0,space_dim[0]+1):
        for y in range(0,space_dim[1]+1):
            if (space[y][x][1] == coordinate):
                area = area + 1
    return area

max_area = 0
for coordinate in finite_area_coordinates:
    max_area = max(max_area,area(space, coordinate))

print("Maximum Finite Area = %d" % max_area)

