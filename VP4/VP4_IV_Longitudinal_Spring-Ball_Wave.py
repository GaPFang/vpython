import numpy as np
from vpython import *
A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))
balls = [sphere(radius=size, color=color.red, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)] #3
springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)] #3
c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)#1
Unit_K, n = 2 * pi/(N*d), 10
Wavevector = n * Unit_K
phase = Wavevector * arange(N) * d
ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d #5
t, dt = 0, 0.0005
count = 0
t1 = t
while True:
    rate(2000)
    t += dt
    #4
    spring_len[:-1] = [ball_pos[i + 1] - ball_pos[i] for i in range(N - 1)]
    ball_v[1: N - 1] += [(k * (spring_len[i + 1] - d) - k * (spring_len[i] - d)) / m * dt for i in range(N - 2)]
    ball_v[0] += (k * (spring_len[0] - d) - k * ((ball_pos[0] - ball_orig[0]) - (ball_pos[N - 1] - ball_orig[N - 1]))) / m * dt
    ball_v[N - 1] += (k * ((ball_pos[0] - ball_orig[0]) - (ball_pos[N - 1] - ball_orig[N - 1])) - k * (spring_len[N - 2] - d)) / m * dt #6
    ball_pos += ball_v*dt
    for i in range(N): balls[i].pos.x = ball_pos[i] #3
    for i in range(N-1): #3
        springs[i].pos = balls[i].pos #3
        springs[i].axis = balls[i+1].pos - balls[i].pos #3
    ball_disp = ball_pos - ball_orig
    for i in range(N):
        c.modify(i, y = ball_disp[i]*4 + 1)
    if count == 0 and ball_disp[N - 1] > 0:
        t1 = t
        count += 1
    if count == 1 and ball_disp[N - 1] < 0:
        count += 1
    if count == 2 and ball_disp[N - 1] > 0:
        print(t - t1)
        t1 = t
        count = 1
    #2
