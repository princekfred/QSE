import numpy as np
import scipy
from qiskit import transpile
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.second_q.circuit.library import UCCSD, HartreeFock
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import SLSQP
from qiskit.primitives import Estimator
from qiskit_algorithms.utils import algorithm_globals
from qiskit_nature.second_q.algorithms import GroundStateEigensolver
from qiskit.quantum_info import Statevector
from qiskit_aer.primitives import Estimator as AerEstimator
from qiskit_nature.second_q.operators import FermionicOp
from qiskit_aer import AerSimulator