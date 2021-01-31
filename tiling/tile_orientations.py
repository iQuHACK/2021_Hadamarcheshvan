def get_orientations(tile):
    # tile = list of tups 
    orientations = []
    original_tile = tile[:]
    next_tile = tile

    orientations.append(None)
    for i in range(4):
        orientations.append(next_tile)
        next_tile = rotate_clockwise(next_tile)
    
    next_tile = mirror(original_tile)
    for i in range(4):
        orientations.append(next_tile)
        next_tile = rotate_clockwise(next_tile)

    return orientations

def rotate_clockwise(tile):
    new_tile = []
    for square in tile:
        new_tile.append((square[1], -1*square[0]))
    return new_tile

def mirror(tile):
    new_tile = []
    for square in tile:
        new_tile.append((square[0], -1*square[1]))
    return new_tile 

#tile = [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)]
#print(rotate_clockwise(tile))
#print(get_orientations(tile))

if __name__ == "__main__":
    from graphics import TileDisplay
    
    disp = TileDisplay(6,40)
    tile = [(0,0),(1,0),(0,1),(0,2)]

    orientations = get_orientations(tile)

    for i in range(1,len(orientations)):
        t = orientations[i]
        offset = i*4
        disp.add_tile((3,offset), t)
    
    print(disp)

