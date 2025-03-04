import vqe
import excitations
import gr_wavefunction 

estimator = AerEstimator(
            run_options={"shots": shots},
            transpile_options={"seed_transpiler": 42},
        approximation=True)

eigenvalues_shots = []
# Initialize the matrix M
num_excitations = len(excitations)
M = np.zeros((num_excitations +1, num_excitations +1), dtype=complex)
S = np.zeros((num_excitations +1, num_excitations +1), dtype=complex)

# Compute the matrix elements  
for i in range(len(excitations) +1):
    for j in range(len(excitations)+1):
        G_i = excitations[i-1]
        G_j = excitations[j-1]
        op_i = mapper.map(G_i)
        op_j = mapper.map(G_j)
        op = op_i.adjoint()@qubit_op@op_j
        oj = qubit_op@op_j
        oi = op_i.adjoint()@qubit_op
                
        if i == j == 0:
            M[i, j] =  estimator.run(ansatz, qubit_op).result().values[0]
            S[i, j] = estimator.run(ansatz, I).result().values[0]
        elif i==0 and j > 0:
            M[i, j] = estimator.run(ansatz, oj).result().values[0]
            S[i, j] = estimator.run(ansatz, op_j).result().values[0]
        elif i>0 and j==0:
            M[i, j] = estimator.run(ansatz, oi).result().values[0]
            S[i, j] = estimator.run(ansatz, op_i.adjoint()).result().values[0]
        else:
            M[i, j] = estimator.run(ansatz, op).result().values[0]
            S[i, j] = estimator.run(ansatz, op_i.adjoint()@op_j).result().values[0]
                        
eigval, ev = scipy.linalg.eigh(M, S) 
eigval = eigval + nr
eigenvalues_shots.append(eigval)
print("shots\n", eigenvalues_shots)
    