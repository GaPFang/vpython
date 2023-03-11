from vpython import*

G=6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} #10 times larger for better view
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0

scene.forward = vector(0, -1, 0)
scene = canvas(width = 800, height = 800, background = color.black, align = 'left')
scene.lights = []
earth = sphere(m = mass['earth'], radius = radius['earth'], texture={'file':textures.earth})
moon = sphere(m = mass['moon'], radius = radius['moon'])
sun = sphere(m = mass['sun'], radius = radius['sun'], color = color.orange, pos = vector(0, 0, 0))
local_light(pos = sun.pos)
earth.pos = vector(earth_orbit['r'] + cos(theta) * moon_orbit['r'] * (-moon.m / (earth.m + moon.m)), sin(theta) * moon_orbit['r'] * (-moon.m / (earth.m + moon.m)), 0)
earth.v = vector(0, 0, -earth_orbit['v'] + moon_orbit['v'] * (moon.m / (earth.m + moon.m)))
moon.pos = vector(earth_orbit['r'] + cos(theta) * moon_orbit['r'] * (earth.m / (earth.m + moon.m)), sin(theta) * moon_orbit['r'] * (earth.m / (earth.m + moon.m)), 0)
moon.v = vector(0, 0, -earth_orbit['v'] + -moon_orbit['v'] * (earth.m / (earth.m + moon.m)))
precessionGraph = graph(width = 400, align = 'right')
precession = gcurve(graph = precessionGraph, color = color.blue, width = 4)


def G_force(M, m, pos_M, pos_m):
    return -G * M * m / mag2(pos_m - pos_M) * norm(pos_m - pos_M)

t = 0
dt = 60 * 60
n = 0

while True:
    rate(365 * 24)
    scene.center = earth.pos
    #scene.forward = vector(cos(2 * pi * t / (60 * 60)), 0, sin(2 * pi * t / (60 * 60)))
    moon.a = (G_force(earth.m, moon.m, earth.pos, moon.pos) + G_force(sun.m, moon.m, sun.pos, moon.pos)) / moon.m
    earth.a = (G_force(moon.m, earth.m, moon.pos, earth.pos) + G_force(sun.m, earth.m, sun.pos, earth.pos))/ earth.m
    moon.v += moon.a * dt
    moon.pos += moon.v * dt
    earth.v += earth.a * dt
    earth.pos += earth.v * dt
    normalVecter = cross(moon.pos - earth.pos, moon.v - earth.v)
    norm_z = norm(normalVecter).z
    precession.plot(pos = (t, norm_z))
    if n == 0 and  norm_z > 0:
        n = 1
    if n == 1 and  norm_z < 0:
        n = 2
        print("The period of precession is " + str(t) + " years.")
    t += dt / (365 * 86400)




              
