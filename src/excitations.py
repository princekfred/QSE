import functions
#Create the all possible excitations
num_spartial_orbital = 4
num_spin_orbitals = num_spartial_orbital * 2

# Initialize the mapper
mapper = JordanWignerMapper()
#Create an identity operator
I = FermionicOp({'': 1.0}, num_spin_orbitals =num_spin_orbitals)
I = mapper.map(I)

 #list of occupied orbitals
occupied = []
for i in range(num_spin_orbitals//4):
    occupied.append(i)
    occupied.append(i+num_spin_orbitals//2)
    
# Generate all possible single excitations
excitations = []
def all_excitations(num_spin_orbitals):
    for i in range(num_spin_orbitals):
        for j in range(i+1, num_spin_orbitals):
            # Prevent electrons from moving from alpha spin to beta spin and beta spin to alpha
            if i != j and ((i < num_spin_orbitals // 2 and j < num_spin_orbitals // 2) or (i >= num_spin_orbitals // 2 and j >= num_spin_orbitals // 2)):
                # Only consider excitations where the first two alpha and beta spins are filled with electrons
                if (i in occupied and j not in occupied): 
                    excitation = FermionicOp({f'+_{j} -_{i}': 1.0}, num_spin_orbitals=num_spin_orbitals)
                    excitations.append(excitation)
    
        #Generate possible double excitations
        #Double excitations all from alpha or beta orbitals
            for k in range(j+1, num_spin_orbitals):
                for l in range(k+1, num_spin_orbitals):
                    if i != j and k != l and ((i < num_spin_orbitals // 2 and j < num_spin_orbitals // 2 and k < num_spin_orbitals // 2 and l < num_spin_orbitals // 2) or (i >= num_spin_orbitals // 2 and j >= num_spin_orbitals // 2 and k >= num_spin_orbitals // 2 and l >= num_spin_orbitals // 2)):
                        # Only consider excitations where the first two alpha and beta spins are filled with electrons
                        if (i in occupied and k not in occupied and j in occupied and l not in occupied): 
                            excitation = FermionicOp({f'+_{l} +_{k} -_{i} -_{j}': 1.0}, num_spin_orbitals=num_spin_orbitals)
                            excitations.append(excitation)
  
    for i in range(num_spin_orbitals // 2):
        for j in range(num_spin_orbitals // 2, num_spin_orbitals):
            for k in range(num_spin_orbitals // 2):
                for l in range(num_spin_orbitals // 2, num_spin_orbitals):
                    if i != k and j != l and i < k and j < l:
                        # Condition to ensure one alpha and one beta excitation
                        if (i in occupied and k not in occupied and j in occupied and l not in occupied): 
                           # Create the FermionicOp and add to double_exc list
                            exc = FermionicOp({f'+_{l} +_{k} -_{i} -_{j}': 1.0}, num_spin_orbitals=num_spin_orbitals)
                            excitations.append(exc)

    return excitations
excitations = all_excitations(num_spin_orbitals)