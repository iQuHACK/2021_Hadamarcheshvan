import dimod

exactsolver = dimod.ExactSolver()

Q_objective = {(0,0): 17, (1,1): 21, (2,2): 19}
Q_constraint = {}
for i in range(0,3):
    Q_constraint[(i,i)] = -3 #squared terms and linear terms add to be linear
    for j in range(i+1,3):
        Q_constraint[(i,j)] = 2 #cross terms

lagrange = 25
c = 4

Q = dict(Q_objective)

#combine QUBOs
for key in Q_constraint:
    if key in Q:
        Q[key] += lagrange * Q_constraint[key]
    else:
        Q[key] = lagrange * Q_constraint[key]

print(Q)

results = exactsolver.sample_qubo(Q)

bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=c*lagrange)
results = exactsolver.sample(bqm)

# print the results
for sample, energy in results.data(['sample', 'energy']):
    print(sample, energy)
