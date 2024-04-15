'''
The volume of the fundamental 
domain is the magnitude of the determinant of A: Vol(F) = |det(A)| = |2*1 - 5*3| = |-13| = 13.
For the flag, calculate the volume of the fundamental 
domain with the basis vectors v1 = (6, 2, -3), v2 = (5, 1, 4), v3 = (2, 7, 1).
'''
import numpy as np
A=[np.array([6, 2, -3])
       ,np.array([5, 1, 4])
       ,np.array([2, 7, 1])
       ]
det_A = np.linalg.det(A)