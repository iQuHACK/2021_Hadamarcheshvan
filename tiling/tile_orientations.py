def get_orientations(tile):
    '''
    Generate all orientations of a tile
    '''
    dim = len(tile[0])
    orientations = []
    original_tile = tile[:]
    next_tile = tile
    
    if dim == 2:
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
    
    elif dim == 3:
        #8 x rotations
        orientations.append(None)
        for i in range(8):
            orientations.append(next_tile)
            next_tile = rotate3D_x(next_tile)
    
        #8 y rotations
        for i in range(8):
            orientations.append(next_tile)
            next_tile = rotate3D_y(next_tile)

        #8 z rotations
        for i in range(8):
            orientations.append(next_tile)
            next_tile = rotate3D_z(next_tile)

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

def rotate3D_x(tile):

    new_tile = []
    for cube in tile:
        new_tile.append((cube[0], cube[2], -1*cube[1]))
    return new_tile

def rotate3D_y(tile):

    new_tile = []
    for cube in tile:
        new_tile.append((-1*cube[2], cube[1], cube[0]))
    return new_tile


def rotate3D_z(tile):

    new_tile = []
    for cube in tile:
        new_tile.append((cube[1], -1*cube[0], cube[2]))
    return new_tile
