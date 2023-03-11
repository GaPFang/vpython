import numpy as np
from vpython import *

A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4

g = graph(title = 'Dispersion Relationship', width = 800, height = 600, align = 'left', xtitle = "Wavevector", ytitle = "Angular Frequency")
c = gcurve(graph = g, color = color.blue, width = 4)

class obj: pass

balls = [obj() for i in range(N)]
springs = [obj() for i in range(N-1)]

for n in range(1, 25):
    Unit_K = 2 * pi / (N * d)
    Wavevector = n * Unit_K
    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d #5
    t, dt = 0, 0.0003
    count = 0
    t1 = t
    while count < 3:
        t += dt
        spring_len[:-1] = [ball_pos[i + 1] - ball_pos[i] for i in range(N - 1)]
        ball_v[1: N - 1] += [(k * (spring_len[i + 1] - d) - k * (spring_len[i] - d)) / m * dt for i in range(N - 2)]
        ball_v[0] += (k * (spring_len[0] - d) - k * ((ball_pos[0] - ball_orig[0]) - (ball_pos[N - 1] - ball_orig[N - 1]))) / m * dt
        ball_v[N - 1] += (k * ((ball_pos[0] - ball_orig[0]) - (ball_pos[N - 1] - ball_orig[N - 1])) - k * (spring_len[N - 2] - d)) / m * dt 
        ball_pos += ball_v*dt
        ball_disp = ball_pos - ball_orig
        if count == 0 and ball_disp[N - 1] > 0:
            t1 = t
            count += 1
        if count == 1 and ball_disp[N - 1] < 0:
            count += 1
        if count == 2 and ball_disp[N - 1] > 0:
            T = t - t1
            c.plot(Wavevector, 2 * pi / T)
            print(n, 2.0 * pi / T)
            count += 1
            
    
