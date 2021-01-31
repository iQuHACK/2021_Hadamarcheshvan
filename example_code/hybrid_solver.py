from dwave.system import LeapHybridSampler
bqm = dimod.AdjVectorBQM(dimod.Vartype.BINARY)
bqm.offset = gamma * ((N/2) ** 2)
bqm.add_variable(...)
bqm.add_interaction(...) 
…
sampler = LeapHybridSampler()
response = sampler.sample(bqm, time_limit=5)

