def get_orientations(tile):
    # tile = list of tups 
    orientations = []
    next_tile = tile
    for i in range(9):
        if i == 0:
            orientations.append(None)
        else:
            orientations.append(next_tile)
            next_tile = rotate_clockwise(next_tile)
    return orientations

def rotate_clockwise(tile):
    new_tile = []
    for square in tile:
        new_tile.append((square[1], -1*square[0]))
    return new_tile


#tile = [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)]
#print(rotate_clockwise(tile))
#print(get_orientations(tile))
