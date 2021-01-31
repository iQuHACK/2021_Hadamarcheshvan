from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler
from tile_orientations import get_orientations
from graphics import TileDisplay
import numpy as np
import time
dqm = DiscreteQuadraticModel()

#dimensions of grid
num_rows = 6
num_cols = 8

#generate rectangular grid
grid_points = []
for r in range(num_rows):
    for c in range(num_cols):
        grid_points.append((r,c))

#grid = set(grid_points)
grid = {(0,0),(0,1),(0,2),(0,3),(1,1)}

#lagrangean
gamma = 10*len(grid) + 1

#number of orientations of a 2D tile
num_orientations = 8

#define tiles
tiles = [[(0,0),(1,0),(2,0)], [(0,0),(-1,-1)], [(0,0),(1,1),(2,2)]]
num_tiles = len(tiles)
num_squares_in_tile = [len(tile) for tile in tiles]

#generate all orientations of tiles
tiles = [get_orientations(tile) for tile in tiles]

#determine invalid tile placements and orientations
location_log = {}
out_of_bounds_log = {}

for prime_location in grid:
    for t in range(num_tiles):
        for orientation in range(1,num_orientations+1):
            for tile_square_index in range(num_squares_in_tile[t]):
                offset = tiles[t][orientation][tile_square_index]

                #calculate locations covered by tile
                location = tuple([i+j for i,j in zip(prime_location, offset)])

                #check if off grid
                if location not in grid:
                    if prime_location in out_of_bounds_log:
                        out_of_bounds_log[prime_location].append((t, orientation))
                    else:
                        out_of_bounds_log[prime_location] = [(t, orientation)]
                else:
                    #log that this tile would hit this location
                    if location in location_log:
                        location_log[location].append((prime_location, t, orientation))
                    else:
                        location_log[location] = [(prime_location, t, orientation)]

#setting linear costs:
#-10 for a valid tile placement
#gamma for an invalid tile placement
#0 otherwise
for prime_location in grid:
    dqm.add_variable(num_tiles*num_orientations+1, label=prime_location)
for prime_location in grid:
    costs = [0] + [-10]*(num_tiles*num_orientations)
    if prime_location in out_of_bounds_log:
        for t, orientation in out_of_bounds_log[prime_location]:
            costs[orientation+t*num_orientations] = gamma
    dqm.set_linear(prime_location, costs)

#determine invalid pairs of tile placements
overlap_violations = {}
for location in grid:
    log = sorted(location_log[location])
    length = len(log)
    for i in range(length):
        prime_location0, t0, orientation0 = log[i]
        for j in range(i+1, length):
            prime_location1, t1, orientation1 = log[j]
            if prime_location0 != prime_location1:
                if (prime_location0, prime_location1) in overlap_violations:
                    overlap_violations[(prime_location0, prime_location1)].append((orientation0+t0*num_orientations, orientation1+t1*num_orientations))
                else:
                    overlap_violations[(prime_location0, prime_location1)] = [(orientation0+t0*num_orientations, orientation1+t1*num_orientations)]

#setting quadratic costs:
#gamma for an overlapping pair of placements
#0 otherwise
for prime_location0, prime_location1 in overlap_violations:
    dqm.set_quadratic(prime_location0, prime_location1, {elem: gamma for elem in overlap_violations[(prime_location0, prime_location1)]})

#solve problem
print("sending to leap")
start_time = time.time()
sampler = LeapHybridDQMSampler()
#note that the time limit may need to be increased for especially large grid sizes
sampleset = sampler.sample_dqm(dqm, time_limit=max(2*len(grid),5))
sample = sampleset.first.sample
energy = sampleset.first.energy
end_time = time.time()
print("took", end_time-start_time, "seconds")

#display optimal tiling
disp = TileDisplay(grid=grid)
for location in sample:
    val = sample[location]
    if val != 0:
        t = int(np.floor((val-1)/num_orientations))
        orientation = val - t*num_orientations
        tile = tiles[t]
        disp.add_tile(location, tile[orientation])
print(disp)
print(str(round(-energy/10)) + " tiles fit in the grid!")
