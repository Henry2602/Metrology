import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_points = pd.read_excel("Roundness_Data.xlsx")
print("\n")
print(data_points)
print("\n")

# Todo-1: Create A matrix
a_matrix = np.ones((len(data_points), 3))
a_matrix[:, 0:2] = data_points[["X", "Y"]]
print(a_matrix.shape)
print("\n")
# Todo-2: Create B matrix
b_matrix = np.zeros((len(data_points), 1))
for data in range(0, len(data_points), 1):
    b_matrix[data] = data_points["X"][data]**2 + data_points["Y"][data]**2
print(b_matrix.shape)
print("\n")
# Todo-3: Calculate X matrix
x_matrix = np.dot(np.linalg.pinv(a_matrix), b_matrix)
print(x_matrix)
xc = x_matrix[0]/2
yc = x_matrix[1]/2
r = (np.sqrt(4*x_matrix[2] + x_matrix[0]**2 + x_matrix[1]**2)) / 2
print(xc)
print(yc)
print(r)
theta = np.linspace(0, 2 * np.pi, 150)

a = r * np.cos(theta)
b = r * np.sin(theta)
figure = plt.figure().add_subplot()
# plt.plot(data_points["X"], data_points["Y"], marker="o")
plt.scatter(data_points["X"], data_points["Y"], marker="o")
plt.plot(xc + a, yc + b)
plt.Circle((xc, yc), r, fill=False, color="black")
plt.show()