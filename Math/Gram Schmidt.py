import numpy as np
from scipy.linalg import orth

# Define the basis vectors
v1 = np.array([4, 1, 3, -1])
v2 = np.array([2, 1, -3, 4])
v3 = np.array([1, 0, -2, 7])
v4 = np.array([6, 2, 9, -5])

# Create a matrix with the basis vectors as rows
V = np.vstack((v1, v2, v3, v4))

# Apply Gram-Schmidt orthogonalization
orthogonal_basis = orth(V.T).T

# Print the orthogonal basis
for i, u in enumerate(orthogonal_basis, start=1):
    print(f"u{i}: {u}")

# Extract the second component of u4 and round it to 5 significant figures
second_component_u4 = round(orthogonal_basis[3, 1], 5)
print("The flag is the float value of the second component of u4 to 5 significant figures:", second_component_u4)
