import dimod

exactsolver = dimod.ExactSolver()

Q = {(0, 0): -58, (1, 1): -54, (2,2): -56, (0,1): 50, (0,2): 50, (1,2): 50}

results = exactsolver.sample_qubo(Q)

# print the results
for sample, energy in results.data(['sample', 'energy']):
    print(sample, energy)