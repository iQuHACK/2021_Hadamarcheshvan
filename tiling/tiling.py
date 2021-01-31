


grid = [(0,0), (1,1)] #...
num_orientations = 8
num_squares_in_tile = 3
tile = [(0,0),(1,0),(1,1)]

location_log = {}
out_of_bounds_log = []

for prime_location in grid:
    x, y = prime_location
    for orientation in range(num_orientations):
        for tile_square_index in range(num_squares_in_tile):
            x_offset, y_offset = tile[tile_square_index]

            #calculate location of new tile
            location = (x+x_offset, y+y_offset)

            #check if off grid
            if location not in grid:
                out_of_bounds_log.append((location, orientation))
            else:
                location_log[location].append((location, orientation))

