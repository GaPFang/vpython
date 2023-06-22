from vpython import *
from numpy import *

N = 100
R, lamda = 1.0, 500E-9
d = 100E-6

dx, dy = d/N, d/N
scene1 = canvas(align = 'left', height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene2 = canvas(align = 'right', x=600, height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene1.lights, scene2.lights = [], []
scene1.ambient, scene2.ambient = color.gray(0.99), color.gray(0.99)
side = linspace(-0.01*pi, 0.01*pi, N)
x,y = meshgrid(side,side)

k = 2 * pi / lamda
k_x = k * x / R
k_y = k * y / R

aperture_side = linspace(-d / 2, d / 2, N)
X, Y = meshgrid(aperture_side, aperture_side)

# change this to calculate the electric field of diffraction of the aperture

# E_field = cos(10000*((x-0.005)**2 + (y- 0.002)**2 ))

# E_field = X ** 2 + Y ** 2 < (d / 2) ** 2

E_field = zeros((N, N))
for i in range(N):
    for j in range(N):
        E_field[i][j] = sum(cos(k_x[i, j] * X + k_y[i, j] * Y) * (X ** 2 + Y ** 2 < (d / 2) ** 2) * dx * dy)
E_field / R

Inte = abs(E_field) ** 2
maxI = amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas = scene1, pos=vector(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
        color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))

Inte = abs(E_field)
maxI = amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas = scene2, pos=vector(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
        color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))

last = 100000
for i in range(50, N):
    if E_field[i, 50] ** 2 > last:
        Rayleigh = 2 * (i - 50) * 0.01 * pi / N
        break
    last = E_field[i, 50] ** 2

print('Theorerical Rayleigh: ' + str(1.22 * lamda / d) + ' rad')
print('Simulated Rayleigh: ' + str(Rayleigh) + ' rad')