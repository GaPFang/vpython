from vpython import*
import math

fd = 120
T = 1 / fd
wd = 120 * 2 * math.pi
R = 30
C = 20 * pow(10, -6)
L = 0.2
Zc = 1 / (wd * C)
Zl = wd * L
Z = sqrt(R * R + pow(Zl - Zc, 2))
phi = -atan((Zl - Zc) / R)
# i"+(R/L)i'+i/(LC)=(72*pi*fd/L)cos(2*pi*fa*t)
# i"+150i'+250000i=(43200pi)cos(240pi)

t=0
dt = 1.0/(fd * 1000)

scene1 = graph(align = 'left', xtitle='t', ytitle='i (A) blue, v (100V) red,', background=vector(0.2, 0.6, 0.2))
scene2 = graph(align = 'left', xtitle='t', ytitle='Energy (J)', background=vector(0.2, 0.6, 0.2))

i_t = gcurve(color=color.blue, graph = scene1)
v_t = gcurve(color=color.red, graph = scene1)
E_t = gcurve(color=color.red, graph = scene2)

i = 0
di = 0
ddi = 0

flag = True
count = 0
start = False
while t <= 12 * T:
    if di > 0:
        flag = True
    if di < 0 and flag == True:
        flag = False
        count += 1
        if count == 9:
            print("I(9-th period): " + str(i) + " A")
            print("phi(9-th period): " + str(360 * (((8 + 1 / 4) * T - t) / T)) + " °")
            print("theoretical I: " + str(36 / Z) + " A")
            print("theoretical phi: " + str(phi * 180 / pi) + " °")
    i += di * dt
    di += ddi * dt
    ddi = 43200 * math.pi * cos(2 * math.pi * fd * t) - 250000 * i - 150 * di
    v = 36 * sin(2 * pi * fd * t)
    v_t.plot(pos = (t, v / 100))
    i_t.plot(pos = (t, i))
    E_12T = (C * pow(v - R * i - L * di, 2) + L * i * i) / 2
    E_t.plot(pos = (t, E_12T))
    t += dt
flag = True
while t <= 20 * T:
    ddi = - 250000 * i - 150 * di
    di += ddi * dt
    i += di * dt
    E = (C * pow(- R * i - L * di, 2) + L * i * i) / 2
    if (flag == True and 10 * E <= E_12T):
        print("t(0.1E): ", str(t / T) + " T")
        flag = False
    v_t.plot(pos = (t, 0))
    i_t.plot(pos = (t, i))
    E_t.plot(pos = (t, E))
    t += dt


