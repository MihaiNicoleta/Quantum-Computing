# -*- coding: utf-8 -*-
"""TemaQC


!pip install qiskit qiskit-aer
!pip install pylatexenc

#  1)Scrieţi o funcţie în Python care având ca input o matrice pătratică A cu elemente complexe, returnează A†
#Exercitiul 1

import numpy as np

def ex1():
  R = int(input("Numar de linii: "))
  C = int(input("Numar de coloane: "))
  A= []

  for i in range (R):
    row = []
    for j in range (C):
      row.append(complex(input()))
    A.append(row)

  print()
  print("Matrice: ")
  for i in range(R):
    for j in range(C):
      if(A[i][j].imag == 0):
        print(A[i][j].real)
      else:
        print(A[i][j], end= " ")
    print()

  print()
  print("A dagger=")
  for j in range(C):
    for i in range(R):
      if(A[i][j].imag == 0):
        print(A[i][j].real, end= " ")
      else:
        print(np.conjugate(A[i][j]), end= " ")
    print()

ex1()

# 2. (10p) Scrieţi o funcţie în Python care primeşte ca input trei vectori |a>,|b>,|c> ∈ C 
#şi returnează expresia |ab> <ca|, unde prin |ab> întelegem |a> ⊗ |b>
from numpy import *
from numpy import tensordot

A = array([complex(1,2),complex(2,3)])
B = array([complex(3),complex(4,1)])
C =array([complex(2,4),complex(2,2)])
def ex2(A,B,C):
    D = tensordot(A, B, axes=0) #|a> ⊗ |b>=|ab>
    X= tensordot(C, A, axes=0) #|c> ⊗ |a>=|ca>
    X=X.transpose().conjugate()# <ca|
    # D*X
    print(D)
    print(X)
    R=outer(D,X)
    print(R)
ex2(A,B,C)

##ex 3
from numpy import *
from qiskit import Aer
from qiskit import QuantumCircuit
from qiskit.providers.aer import QasmSimulator
circuit=QuantumCircuit(2) #creeaza circuit de 2 qubiti
circuit.cx(0,1)
circuit.h(0)
circuit.draw(output="mpl") #a

#b
import numpy as np 
from numpy import *
from numpy import linalg
backend=Aer.get_backend('unitary_simulator')
job=backend.run(circuit)
results=job.result()
U=results.get_unitary(circuit,decimals=10)
print(U)
U_t=U.transpose().conjugate()
print(U_t) #transpusa lui U conjugata = U†
I4=[[1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]]
#U unitara daca U·U† = U†·U=I4
P1=np.dot(U,U_t) #U·U†
P2=np.dot(U_t,U) # U†·U np.dot face produsul a 2 matrici
DIF1=np.subtract(P1, I4) #U·U†-I4
DIF2=np.subtract(P2, I4) #U·U†·U-I4
#print(DIF1)

norma1 = np.linalg.norm(DIF1)
norma2 = np.linalg.norm(DIF2) 
print(norma1)
print(norma2)
if(norma1<=0.00005 and norma2<=0.00005):
  print("U e unitara")
else:
  print("U nu e unitara")

#c Rulaţi circuitul urmator pe simulatorul ’qasmsimulator’ de 1000 de ori şi afişati rezultatele. Reprezentaţi şi
#histograma corespunzătoare pentru a vizualiza rezultatele
#afisez circuit
from numpy import *
from qiskit import Aer
from qiskit import QuantumCircuit
#Masurare
circuit.measure_all()
circuit.draw(output="mpl") #a
print(circuit)
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit,shots=1000)
results=job.result()
counts=results.get_counts()
print(counts)
"""Afisarea histogramei""" 
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)

#3d

from numpy import *
from qiskit import Aer
from qiskit import QuantumCircuit
from qiskit.providers.aer import QasmSimulator
circuit=QuantumCircuit(2) #creeaza circuit de 2 qubiti
circuit.initialize('01')
circuit.h(0)
circuit.cx(0,1)
circuit.barrier()
circuit.cx(0,1)
circuit.h(0)
circuit.measure_all()

circuit.draw(output="mpl")

import matplotlib.pyplot as plt
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit, shots=1000)
results=job.result()
count=results.get_counts()
print(count)
from qiskit.tools.visualization import plot_histogram
plot_histogram(count)
#rulez pe simulator

# EX 4  
from qiskit import *
from qiskit import Aer
from qiskit import QuantumCircuit
circ=QuantumCircuit(2)
def ex4():
  circ.x(0)
  circ.h(0)
  circ.cx(0,1)
  circ.h(1)
  circ.x(1)
ex4()
circ.draw(output="mpl")

# EX 5
from qiskit import Aer
#input= vector
A=array([complex(0.707,0),complex(0),complex(0),complex(0.707)])
print(A)
def ex5(A):
  M=[[0,0],[0,0]]
  M[0][0]=A[0]
  M[0][1]=A[1]
  M[1][0]=A[2]
  M[1][1]=A[3] # partea reala la a 2 a + imaginara la a 2 a
  P_q0_0=M[0][0].real*M[0][0].real+M[0][0].imag*M[0][0].imag+M[0][1].real*M[0][1].real+M[0][1].imag*M[0][1].imag
  P_q0_1=M[1][0].real*M[1][0].real+M[1][0].imag*M[1][0].imag+ M[1][1].real*M[1][1].real+M[1][1].imag*M[1][1].imag
  P_q1_0=M[0][0].real*M[0][0].real+M[0][0].imag*M[0][0].imag+ M[1][0].real*M[1][0].real+ M[1][0].imag*M[1][0].imag
  P_q1_1=M[1][1].real*M[1][1].real+M[1][1].imag*M[1][1].imag+M[0][1].real*M[0][1].real+M[0][1].imag*M[0][1].imag
  P_00=M[0][0].real*M[0][0].real+M[0][0].imag*M[0][0].imag
  P_01=M[0][1].real*M[0][1].real+M[0][1].imag*M[0][1].imag
  P_10=M[1][0].real*M[1][0].real+M[1][0].imag*M[1][0].imag
  P_11=M[1][1].real*M[1][1].real+M[1][1].imag*M[1][1].imag
  print(P_11)
  if((P_00==P_q0_0*P_q1_0) and (P_01==P_q0_0*P_q1_1) and (P_10==P_q0_1*P_q1_0) and (P_11==P_q0_1*P_q1_1)):
     print("E separabila")
  else: 
     print("entangled")
ex5(A)

#Ex 6
import matplotlib.pyplot as plt
import numpy as np
from math import *
import math
import numpy
from qiskit.qasm import pi
from qiskit.circuit.controlledgate import ControlledGate
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import QuantumRegister
psi_zero=QuantumCircuit(3)
phi=2*acos((1/sqrt(3))) 
psi_zero.ry(phi,0)
psi_zero.ch(0,1)
psi_zero.cx(1,2)
psi_zero.cx(0,1)
psi_zero.x(0)
#psi 0
psi_zero.p(2*pi/3, 2)
psi_zero.p(4*pi/3, 1)
psi_zero.draw(output="mpl")

psi_unu=QuantumCircuit(3)
phi=2*acos((1/sqrt(3)))
psi_unu.ry(phi,0)
psi_unu.ch(0,1)
psi_unu.cx(1,2)
psi_unu.cx(0,1)
psi_unu.x(0)
#psi 1
psi_unu.p(2*pi/3, 1)
psi_unu.p(4*pi/3, 2)
psi_unu.draw(output="mpl")
