import vqe
import excitations
import gr_wavefunction 

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
            M[i, j] = Statevector(statevector).expectation_value(qubit_op)
            S[i, j] = 1.0
        elif i==0 and j > 0:
            M[i, j] = Statevector(statevector).expectation_value(oj)
            S[i, j] = Statevector(statevector).expectation_value(op_j)
        elif i>0 and j==0:
            M[i, j] = Statevector(statevector).expectation_value(oi)
            S[i, j] = Statevector(statevector).expectation_value(op_i.adjoint())
        else:
            M[i, j] = Statevector(statevector).expectation_value(op)
            S[i, j] = Statevector(statevector).expectation_value(op_i.adjoint()@op_j)                      
cond_num = np.linalg.cond(S)
print("condition number:\n", cond_num)

eigval_exact, ev = scipy.linalg.eigh(M, S) 
total_energy = eigval_exact + nr
print(total_energy)