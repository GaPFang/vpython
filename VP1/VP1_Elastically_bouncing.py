from vpython import *

g = 9.8
size = 0.25
C_drag = 0.9
count = 0
theta = pi/4

scene = canvas(align = 'left', width = 800, height = 600, center = vec(0, 5, 0), background = vec(0.5, 0.5, 0))
floor = box(length = 30, width = 4, height = 0.01, color = color.blue)
ball = sphere(radius = size, color = color.red, make_trail = True, trail_radius = size/3)
a = arrow(shaftwidth = size/3, color = color.red)
vtgraph = graph(width = 450, align = 'right')
funct1 = gcurve(graph =  vtgraph, color = color.red, width = 4)

ball.pos = vec(-15, size, 0)
ball.v = vec(20 * cos(theta), 20 * sin(theta), 0)
t = 0
dt = 0.001
total_distance = 0
highest = 0

while count < 3:
    rate(1000)
    a.pos = ball.pos
    a.axis = ball.v
    total_distance += ball.v.mag * dt
    funct1.plot(pos = (t, ball.v.mag))
    ball.pos += ball.v * dt
    ball.v += vec(0, -g, 0) * dt - ball.v * C_drag * dt
    if ball.pos.y > highest:
        highest = ball.pos.y
    if  ball.pos.y <= size:
        ball.v.y = -ball.v.y
        count += 1
    t += dt
msg = text(text = 'displacement = ' + str(ball.pos.x + 15), pos = vec(-10, 16, 0))
msg = text(text = 'total distance = ' + str(total_distance), pos = vec(-10, 13, 0))
msg = text(text = 'largest height = ' + str(highest), pos = vec(-10, 10, 0))


