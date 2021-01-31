from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler
from tile_orientations import get_orientations
dqm = DiscreteQuadraticModel()

num_rows = 4
num_cols = 4

grid_points = []
for r in range(num_rows):
    for c in range(num_cols):
        grid_points.append((r,c))

grid = set(grid_points)

gamma = len(grid) + 1

num_orientations = 8
num_squares_in_tile = 3
tile = [(0,0),(1,0),(1,1)]
tiles = get_orientations(tile) #... all the orientation

location_log = {}
out_of_bounds_log = {}

for prime_location in grid:
    for orientation in range(1,num_orientations+1):
        for tile_square_index in range(num_squares_in_tile):
            offset = tiles[orientation][tile_square_index] #orientation may be off by one

            #calculate location of new tile
            location = tuple([i+j for i,j in zip(prime_location, offset)])

            if location != prime_location:

                #check if off grid
                if location not in grid:
                    if prime_location in out_of_bounds_log:
                        out_of_bounds_log[prime_location].append(orientation)
                    else:
                        out_of_bounds_log[prime_location] = [orientation]
                    #no need to log these - just set coefficient here
                else:
                    #log that this tile would hit this location
                    if location in location_log:
                        location_log[location].append((prime_location, orientation))
                    else:
                        location_log[location] = [(prime_location, orientation)]

#Setting linear costs
for prime_location in grid:
    dqm.add_variable(num_orientations+1, label=prime_location)
for prime_location in grid:
    costs = [0] + [-1]*num_orientations
    if prime_location in out_of_bounds_log:
        for orientation in out_of_bounds_log[prime_location]:
            costs[orientation] = gamma
    dqm.set_linear(prime_location, costs)

overlap_violations = {}

for location in grid:
    log = sorted(location_log[location])
    length = len(log)
    for i in range(length):
        prime_location0, orientation0 = log[i]
        for j in range(i+1, length):
            prime_location1, orientation1 = log[j]
            if (prime_location0, prime_location1) in overlap_violations:
                overlap_violations[(prime_location0, prime_location1)].append((orientation0, orientation1))
            else:
                overlap_violations[(prime_location0, prime_location1)] = [(orientation0, orientation1)]

for prime_location0, prime_location1 in overlap_violations:
    dqm.set_quadratic(prime_location0, prime_location1, {elem: gamma for elem in overlap_violations[(prime_location0, prime_location1)]})

sampler = LeapHybridDQMSampler()
sampleset = sampler.sample_dqm(dqm)
sample = sampleset.first.sample
energy = sampleset.first.energy

# locations_Log {tuple:[(tuple, int)]}