import functions
# Initialize the driver and problem
driver = PySCFDriver(atom="........",  basis="sto-3g")
problem = driver.run()

seed = 170
algorithm_globals.random_seed = seed
mapper = JordanWignerMapper()
        
# Map the electronic problem to a qubit operator
qubit_op = mapper.map(problem.hamiltonian.second_q_op())
        
# Initialize the UCCSD ansatz with Hartree-Fock initial state
ansatz = UCCSD(
    problem.num_spatial_orbitals,
    problem.num_particles,
    mapper,
    initial_state=HartreeFock(
        problem.num_spatial_orbitals,
        problem.num_particles,
        mapper
    ),
)
vqe = VQE(Estimator(), ansatz, SLSQP())
vqe.initial_point = np.zeros(ansatz.num_parameters)
nr = problem.nuclear_repulsion_energy 

#creating a ground state eigensolver(vqe)      
solver = GroundStateEigensolver(mapper, vqe)
result = solver.solve(problem)
print(f"Total ground state energy = {result.total_energies}")