import numpy as np
import matplotlib.pyplot as plt

DIAMETER = 1
UPPER_DEVIATION_SHAFT = +0.001
LOWER_DEVIATION_SHAFT = -0.001
UPPER_DEVIATION_HOLE = +0.00
LOWER_DEVIATION_HOLE = -0.008


mean_shaft = (UPPER_DEVIATION_SHAFT + LOWER_DEVIATION_SHAFT)/2 + DIAMETER
standard_deviation_shaft = (UPPER_DEVIATION_SHAFT-LOWER_DEVIATION_SHAFT)/6

mean_hole = (UPPER_DEVIATION_HOLE + LOWER_DEVIATION_HOLE)/2 + DIAMETER
standard_deviation_hole = (UPPER_DEVIATION_HOLE-LOWER_DEVIATION_HOLE)/6

def Data(mean, standard_deviation):
    data_range = np.arange(mean-3*standard_deviation, mean+3*standard_deviation, 0.00001)
    return data_range

def NormalDistribution(mean, standard_deviation):
    f_diameter = (1/(standard_deviation*np.sqrt(2*np.pi))) * np.exp(-0.5*((Data(mean, standard_deviation)-mean)/standard_deviation)**2)
    return f_diameter


figure = plt.figure().add_subplot()
plt.plot(Data(mean_shaft, standard_deviation_shaft), NormalDistribution(mean_shaft, standard_deviation_shaft), color="blue")
plt.plot(Data(mean_hole, standard_deviation_hole), NormalDistribution(mean_hole, standard_deviation_hole), color = "orange")
plt.legend(["Shaft Tolerancing Distribution", "Hole Tolerancing Distribution"])
plt.xlabel("Diameter (inch)")
plt.ylabel("Probability Density")
plt.show()

