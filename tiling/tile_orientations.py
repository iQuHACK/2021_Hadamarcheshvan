def get_orientations(tile):
    '''
    Generate all orientations of a tile
    '''
    orientations = []
    original_tile = tile[:]
    next_tile = tile

    #4 rotations separated by clockwise rotation
    orientations.append(None)
    for i in range(4):
        orientations.append(next_tile)
        next_tile = rotate_clockwise(next_tile)
    
    #4 mirrored rotations separated by clockwise rotation
    next_tile = mirror(original_tile)
    for i in range(4):
        orientations.append(next_tile)
        next_tile = rotate_clockwise(next_tile)

    return orientations

def rotate_clockwise(tile):
    '''
    Rotate a tile clockwise
    '''
    new_tile = []
    for square in tile:
        new_tile.append((square[1], -1*square[0]))
    return new_tile

def mirror(tile):
    '''
    Mirror a tile vertically
    '''
    new_tile = []
    for square in tile:
        new_tile.append((square[0], -1*square[1]))
    return new_tile 

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

