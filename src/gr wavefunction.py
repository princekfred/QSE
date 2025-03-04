import vqe

# Extract the ground state wavefunction parameters
psi_vqe = result.raw_result.optimal_point
    
# Create the ansatz circuit with optimized parameters
ansatz.assign_parameters(psi_vqe, inplace=True) 
 
simulator = AerSimulator(method='statevector')
qc = transpile(ansatz, simulator)
qc.save_statevector()
    
# Execute the circuit on the simulator
result = simulator.run(qc).result()
statevector = result.get_statevector()