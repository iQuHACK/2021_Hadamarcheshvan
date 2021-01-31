import dimod

exactsolver = dimod.ExactSolver()

Q = {(0, 0): -1, (1, 1): -1, (2, 2): -1, (0,2): 2, (0,1): 2, (1,2): 2}

results = exactsolver.sample_qubo(Q)

bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=1)
results = exactsolver.sample(bqm)

# print the results
for sample, energy in results.data(['sample', 'energy']):
    print(sample, energy)
