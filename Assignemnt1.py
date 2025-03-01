# Question 3
import numpy as np
import matplotlib.pyplot as plt

# 3a
F = np.array([[2, 1],
              [1, 2]])
#Matrix F using the numpy array

eValues, eVectors = np.linalg.eig(F)

print("Eigenvalues:")
print(eValues)
print("\nEigenvectors:")
print(eVectors)

# 3b
v1 = np.array([1, 0])
v2 = np.array([0, 1])
Fv1 = F @ v1
Fv2 = F @ v2

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1 (original)')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='green', label='v2 (original)')
plt.quiver(0, 0, Fv1[0], Fv1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Fv1 (transformed)')
plt.quiver(0, 0, Fv2[0], Fv2[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Fv2 (transformed)')

plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Original Vectors and Transformed Vectors')
plt.legend()
plt.grid()
plt.show()

# 3b
print("\nDiscussion:")
print("The transformation matrix F has eigenvalues", eValues, "and eigenvectors:")
print(eVectors)
print("Eigenvectors are directions that remain even through transformations.")
print("The eigenvalues indicate the scalar for those factors.")
