
num_rows = 4
num_cols = 4

grid_points = []
for r in range(num_rows):
    for c in range(num_cols):
        grid_points.append((r,c))

grid = set(grid_points)

num_orientations = 8
num_squares_in_tile = 3
tile = [(0,0),(1,0),(1,1)]
tiles = [[(0,0),(1,0),(1,1)],[(0,0),(0,1),(1,1)]] #... all the orientations

location_log = {}
out_of_bounds_log = []

for prime_location in grid:
    x, y = prime_location
    for orientation in range(num_orientations):
        for tile_square_index in range(num_squares_in_tile):
            x_offset, y_offset = tiles[orientation][tile_square_index] #orientation may be off by one

            #calculate location of new tile
            location = (x+x_offset, y+y_offset)

            #check if off grid
            if location not in grid:
                out_of_bounds_log.append((location, orientation))
            else:
                #log that this tile would hit this location
                if location in location_log:
                    location_log[location].append((location, orientation))
                else:
                    location_log[location] = [(location, orientation)]

            

