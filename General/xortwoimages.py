from PIL import Image
import numpy as np

# Open the two images
image1 = Image.open("C:\\Users\\DELL\\Python\\crypto\\flag.png")
image2 = Image.open("C:\\Users\\DELL\\Python\\crypto\\lemur.png")

# Convert images to NumPy arrays
array1 = np.array(image1)
array2 = np.array(image2)

xor_result = np.bitwise_xor(array1, array2)
xor_image = Image.fromarray(xor_result)
xor_image.save("xor_image.png")
# Alternatively, display the XORed image
xor_image.show()