from vpython import*

G=6.673E-11
mass = {'Sun': 1.99E30, 'Mercury': 3.285E23, 'Venus': 4.87E24, 'Earth': 5.97E24, 'Mars': 6.39E23, 'Jupiter': 1.90E27, 'Saturn': 5.68E26, 'Uranus': 8.68E25, 'Neptune': 1.02E26}
radius = {'Sun': 6.95E8*50, 'Mercury': 2.439E6 * 1000, 'Venus': 6.051E6*1000, 'Earth': 6.371E6*1000, 'Mars': 3.389E6 * 1000, 'Jupiter': 6.991E7 * 500, 'Saturn': 5.823E7 * 500, 'Uranus': 2.536E7 * 1000, 'Neptune': 2.462E7 * 1000}     #many times larger for better view
orbit = {'Mercury': 5.8E10, 'Venus': 1.082E11, 'Earth': 1.496E11, 'Mars': 2.279E11, 'Jupiter': 7.785E11, 'Saturn': 1.429E12, 'Uranus': 2.871E12, 'Neptune': 4.504E12}
v = {'Mercury': 4.789E4, 'Venus': 3.5E4, 'Earth': 2.9783E4, 'Mars': 2.413E4, 'Jupiter': 1.306E4, 'Saturn': 9.69E3, 'Uranus': 6.81E3, 'Neptune': 5.43E3}
#angle = {'Mercury': , 'Venus': , 'Earth': , 'Mars': , 'Jupiter': , 'Saturn': , 'Uranus': , 'Neptune': }


scene = canvas(width = 1500, height = 1000, background = color.black)
Sun = sphere(m = mass['Sun'], radius = radius['Sun'], color = color.orange, pos = vector(0, 0, 0), emissive = True)
Mercury = sphere(m = mass['Mercury'], radius = radius['Mercury'], texture={'file':textures.stones}, pos = vector(orbit['Mercury'], 0, 0), v = vector(0, 0, -v['Mercury']), emissive = True)
Venus = sphere(m = mass['Venus'], radius = radius['Venus'], color = color.orange, pos = vector(orbit['Venus'], 0, 0), v = vector(0, 0, -v['Venus']), emissive = True)
Earth = sphere(m = mass['Earth'], radius = radius['Earth'], texture={'file':textures.earth}, pos = vector(orbit['Earth'], 0, 0), v = vector(0, 0, -v['Earth']), emissive = True)
Mars = sphere(m = mass['Mars'], radius = radius['Mars'], color = color.red, pos = vector(orbit['Mars'], 0, 0), v = vector(0, 0, -v['Mars']), emissive = True)
Jupiter = sphere(m = mass['Jupiter'], radius = radius['Jupiter'], texture={'file':textures.wood_old}, pos = vector(orbit['Jupiter'], 0, 0), v = vector(0, 0, -v['Jupiter']), emissive = True)
Saturn = sphere(m = mass['Saturn'], radius = radius['Saturn'], texture={'file':textures.wood}, pos = vector(orbit['Saturn'], 0, 0), v = vector(0, 0, -v['Saturn']), emissive = True)
Uranus = sphere(m = mass['Uranus'], radius = radius['Uranus'], color = color.cyan, pos = vector(orbit['Uranus'], 0, 0), v = vector(0, 0, -v['Uranus']), emissive = True)
Neptune = sphere(m = mass['Neptune'], radius = radius['Neptune'], color = color.blue, pos = vector(orbit['Neptune'], 0, 0), v = vector(0, 0, -v['Neptune']), emissive = True)
stars = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
def G_force(M, m, pos_M, pos_m):
    return -G * M * m / mag2(pos_m - pos_M) * norm(pos_m - pos_M)

t = 0
dt = 60 * 60 * 24

while True:
    rate(365 * 10)
    #scene.forward = vector(cos(2 * pi * t / (60 * 60)), 0, sin(2 * pi * t / (60 * 60)))
    for target in stars:
        target.a = G_force(Sun.m, target.m, Sun.pos, target.pos) / target.m
        for star in stars:
            if target != star:
                target.a += G_force(star.m, target.m, star.pos, target.pos) / target.m
    for target in stars:
        target.v += target.a * dt
        target.pos += target.v * dt
    t += dt / (365 * 86400)




              
