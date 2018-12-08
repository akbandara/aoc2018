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

safe_area = 0
progress_bar = Bar("Processing Space ", max=len(coordinate_array)*(space_dim[0]+1)*(space_dim[1]+1))
for x in range(0,space_dim[0]+1):
    for y in range(0,space_dim[1]+1):
        distance = 0
        for coordinate in coordinate_array:
            distance = distance + manhattan_distance(coordinate, (x, y))
            progress_bar.next()
        if distance < 10000:
            safe_area = safe_area + 1
progress_bar.finish()

print("Safe Area = %d" % safe_area)

