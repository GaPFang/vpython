from vpython import *
import numpy as np
import math

R1, R2 = 0.06, 0.12
I = 1
d = 0.001

#initialization
scene = canvas(width=600, height=600,align = 'left', background=vector(0.2,0.2,0))
loop1 = ring(pos=vector(0, 0, 0.1), axis=vector(0, 0, 1), radius=0.06, thickness=0.001)
loop2 = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.12, thickness=0.001)

def mag(x): 
    return math.sqrt(sum(i**2 for i in x))

def BiotSavart(x1, y1, z1, x2, y2, z2):
    distance = np.array([x2 - x1, y2 - y1, z2 - z1])
    dl = d * np.array([0, 1, 0])
    return (1e-7 * I * np.cross(dl, distance)) / pow(mag(distance), 3)

# part 1
phi_B = 0
x = -R1
y = -R1
while x <= R1:
    y = -R1
    while y <= R1:
        if (mag((x, y, 0)) <= R1):
            phi_B += np.dot(BiotSavart(R2, 0, 0, x, y, 0.1), (0, 0, 1)) * d * d
        y += d
    x += d
phi_B *= 2 * math.pi * R2 / d
M_12 = phi_B
print("M_12: " + str(M_12) + " H")

# part 2
phi_B = 0
x = -R2
y = -R2
while x <= R2:
    y = -R2
    while y <= R2:
        if (mag((x, y, 0)) <= R2):
            phi_B += np.dot(BiotSavart(R1, 0, 0.1, x, y, 0), (0, 0, 1)) * d * d
        y += d
    x += d
phi_B *= 2 * math.pi * R1 / d
M_21 = phi_B
print("M_21: " + str(M_21) + " H")