from vpython import *
size, m = 0.02, 0.2
L, k = 0.2, 20
#amplitude = 0.03
b = 0.05 * m * sqrt(k/m)
fa = 0.1
wd = sqrt(k/m)
T = 2 * pi / wd

scene = canvas(width=600, height=400, range = 0.3, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue)
ball = sphere(radius = size, color=color.red)
spring = helix(radius=0.015, thickness =0.01)
oscillation1 = graph(width = 400, align = 'right', xtitle='t',ytitle='x',background=vec(0.5,0.5,0))
x = gcurve(color=color.red,graph = oscillation1)
oscillation2 = graph(width = 400, align = 'right', xtitle='t',ytitle='W',background=vec(0.5,0.5,0))
averagePower = gdots(color=color.green,graph = oscillation2)

ball.pos = vector(L, 0, 0)
ball.v = vector(0, 0, 0)
ball.m = m
spring.pos = vector(0, 0, 0)
t, dt = 0, 0.001
count = 0
totalPower = 0

while True:
    rate(1000)
    spring.axis = ball.pos - spring.pos
    force_ext = fa * sin(wd * t) * vector(1, 0, 0)
    spring_force = -k * (spring.axis.x - L) * norm(spring.axis)
    airDrag_force = -b * ball.v
    ball.a = (force_ext + spring_force + airDrag_force) / m
    ball.v += ball.a * dt
    ball.pos += ball.v * dt
    totalPower += dot(force_ext, ball.v) * dt
    t += dt
    x.plot(pos = (t, ball.pos.x - L))
    if (t / T > count):
        averagePower.plot(pos = (t, totalPower / T))
        totalPower = 0
        count += 1
