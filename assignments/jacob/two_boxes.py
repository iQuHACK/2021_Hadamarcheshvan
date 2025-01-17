import dimod
from dwave.system import LeapHybridSampler

exactsolver = dimod.ExactSolver()

Q = {(0, 0): -58, (1, 1): -54, (2,2): -56, (0,1): 50, (0,2): 50, (1,2): 50}

bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=100)

'''
results = exactsolver.sample(bqm)
# print the results
for sample, energy in results.data(['sample', 'energy']):
    print(sample, energy)
'''

sampler = LeapHybridSampler()
response = sampler.sample(bqm, time_limit=5)

print("Optimal value:", response.first.energy)
print("Optimal solution:", response.first.sample)