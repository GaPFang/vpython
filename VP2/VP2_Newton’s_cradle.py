from vpython import *

g = 9.8
size = 0.2
m = 1
L = 2
k = 150000
N = int(input(''))

scene = canvas(width = 800, height = 800, center = vec(0, -1, 0), align = 'left', background = vec(0.5, 0.5, 0))
energyGraph = graph(width = 400, align = 'right')
averageEnergyGraph = graph(width = 400, align = 'right')
kinetic = gcurve(graph = energyGraph, color = color.blue, width = 4)
potential = gcurve(graph = energyGraph, color = color.red, width = 4)
averageKinetic = gcurve(graph = averageEnergyGraph, color = color.blue, width = 4)
averagePotential = gcurve(graph = averageEnergyGraph, color = color.red, width = 4)
def af_col_v(m1, m2, v1, v2, x1, x2):
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)

points = []
heights = []
side = [-1, -1, -1, -1, -1]
balls = []
ropes = []
for i in range(5):
    point = sphere(radius = size/3, pos = vec(2 * size * (i - 2), 0, 0))
    points.append(point)
    
    if (i < N):
        heights.append(-1.95)
    else:
        heights.append(-2)
        
    ball = sphere(radius = size, pos = vec(points[i].pos.x + side[i] * ((-L - m * g * (-heights[i] / L)/k)**2 - (heights[i] - m * g * (-heights[i] / L)/k)**2)**0.5, (heights[i] - m * g * (-heights[i] / L)/k), 0), v = vec(0, 0, 0))
    balls.append(ball)
    
    rope = cylinder(radius = size/4, pos = points[i].pos)
    ropes.append(rope)

dt = 0.0005
t = 0
TEk = 0
TU = 0
while True:
    rate(5000)    
    Ek = 0
    U = 0
    for i in range(5):
        ropes[i].axis = balls[i].pos - points[i].pos
        balls[i].v += (vec(0, -g, 0) - k * (mag(ropes[i].axis) - L) / m * ropes[i].axis.norm()) * dt
        balls[i].pos += balls[i].v * dt
        Ek += 1/2 * m * mag(balls[i].v)**2
        U += m * g * (2 + balls[i].pos.y)

    TEk += Ek * dt
    TU += U * dt

    t += dt
    kinetic.plot(pos = (t, Ek))
    potential.plot(pos = (t, U))
    averageKinetic.plot(pos = (t, TEk/t))
    averagePotential.plot(pos = (t, TU/t))
    
    for i in range(4):
        if (mag(balls[i].pos - balls[i + 1].pos) <= 2 * size and  dot (balls[i].v - balls[i + 1].v, balls[i].pos - balls[i + 1].pos) < 0):
            (balls[i].v, balls[i + 1].v) = af_col_v(m, m, balls[i].v, balls[i + 1].v, balls[i].pos, balls[i + 1].pos)
      
        
        
        


        
