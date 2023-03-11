from vpython import *

g = 9.8
size = 0.25    # ball radius = 0.25 m
airDrag = 0.1

scene = canvas(width = 1000, height = 600, center = vec(0, 5, 0), background = vec(0.5, 0.5, 0))
floor = box(length = 30, height = 0.01, width = 4, color = color.blue)
ball = sphere(radius = size, color = color.red, make_trail = True, trail_radius = size/3)

ball.pos = vec(-15.0, size, 0.0)
ball.v = vec(2.0, 5.0, 0.0)
dt = 0.001

while ball.pos.y < 15.0:
    rate(1000)
    ball.pos += ball.v * dt
    ball.v -= ball.v * airDrag * dt
    ball.v.y += -g * dt

    if ball.pos.y <= size and ball.v.y < 0:
        ball.v.y = -ball.v.y * 0.9
