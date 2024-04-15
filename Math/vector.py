import numpy as np
v = np.array([4, 6, 2, 5])
# Cộng hai vector
inner_product = np.matmul(v,v)
size_of_v = np.sqrt(inner_product)
print(size_of_v)
