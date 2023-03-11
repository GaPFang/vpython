from vpython import*

G=6.673E-11
mass = {'Sun': 1.99E30, 'Mercury': 3.30E23, 'Venus': 4.87E24, 'Earth': 5.97E24, 'Mars': 6.42E23, 'Jupiter': 1.90E27, 'Saturn': 5.68E26, 'Uranus': 8.68E25, 'Neptune': 1.02E26}
radius = {'Sun': 6.95E8*50, 'Mercury': 2.439E6 * 1000, 'Venus': 6.051E6*1000, 'Earth': 6.371E6*1000, 'Mars': 3.389E6 * 1000, 'Jupiter': 6.991E7 * 500, 'Saturn': 5.823E7 * 500, 'Uranus': 2.536E7 * 800, 'Neptune': 2.462E7 * 1000}     #many times larger for better view
pos_x = {'Mercury': 2.277E+10, 'Venus': 6.289E+10, 'Earth': 1.300E+11, 'Mars': 1.623E+11, 'Jupiter': 1.301E+11, 'Saturn': -1.103E+12, 'Uranus': -2.157E+12, 'Neptune': -1.244E+12}
pos_y = {'Mercury': -5.729E+10, 'Venus': 8.991E+10, 'Earth': -7.644E+10, 'Mars': 1.565E+11, 'Jupiter': 7.562E+11, 'Saturn': 8.183E+11, 'Uranus': -1.737E+12, 'Neptune': -4.348E+12}
v_x = {'Mercury': 4.103E+04, 'Venus': -2.859E+04, 'Earth': 1.451E+04, 'Mars': -1.688E+04, 'Jupiter': -1.304E+04, 'Saturn': -5.970E+03, 'Uranus': 4.447E+03, 'Neptune': 5.247E+03}
v_y = {'Mercury': 1.631E+04, 'Venus': 2.000E+04, 'Earth': 2.579E+04, 'Mars': 1.750E+04, 'Jupiter': 2.244E+03, 'Saturn': -8.049E+03, 'Uranus': -5.523E+03, 'Neptune': -1.501E+03}
theta = 0.04608421379889
#angle = {'Mercury': , 'Venus': , 'Earth': , 'Mars': , 'Jupiter': , 'Saturn': , 'Uranus': , 'Neptune': }
#0.06, 38500
#0.04608, 38750
#0.4877, 39000

scene = canvas(width = 800, height = 800, background = color.black, align = 'left')
Sun = sphere(m = mass['Sun'], radius = radius['Sun'], color = color.orange, pos = vector(0, 0, 0), emissive = True)
Mercury = sphere(m = mass['Mercury'], radius = radius['Mercury'], texture={'file':textures.stones}, pos = vector(pos_x['Mercury'], pos_y['Mercury'], 0), v = vector(v_x['Mercury'], v_y['Mercury'], 0), emissive = True)
Venus = sphere(m = mass['Venus'], radius = radius['Venus'], color = color.orange, pos = vector(pos_x['Venus'], pos_y['Venus'], 0), v = vector(v_x['Venus'], v_y['Venus'], 0), emissive = True)
Earth = sphere(m = mass['Earth'], radius = radius['Earth'], texture={'file':textures.earth}, pos = vector(pos_x['Earth'], pos_y['Earth'], 0), v = vector(v_x['Earth'], v_y['Earth'], 0), emissive = True)
Mars = sphere(m = mass['Mars'], radius = radius['Mars'], color = color.red, pos = vector(pos_x['Mars'], pos_y['Mars'], 0), v = vector(v_x['Mars'], v_y['Mars'], 0), emissive = True)
Jupiter = sphere(m = mass['Jupiter'], radius = radius['Jupiter'], texture={'file':textures.wood_old}, pos = vector(pos_x['Jupiter'], pos_y['Jupiter'], 0), v = vector(v_x['Jupiter'], v_y['Jupiter'], 0), emissive = True)
Saturn = sphere(m = mass['Saturn'], radius = radius['Saturn'], texture={'file':textures.wood}, pos = vector(pos_x['Saturn'], pos_y['Saturn'], 0), v = vector(v_x['Saturn'], v_y['Saturn'], 0), emissive = True)
Uranus = sphere(m = mass['Uranus'], radius = radius['Uranus'], color = color.cyan, pos = vector(pos_x['Uranus'], pos_y['Uranus'], 0), v = vector(v_x['Uranus'], v_y['Uranus'], 0), emissive = True)
Neptune = sphere(m = mass['Neptune'], radius = radius['Neptune'], color = color.blue, pos = vector(pos_x['Neptune'], pos_y['Neptune'], 0), v = vector(v_x['Neptune'], v_y['Neptune'], 0), emissive = True)

voyager2_vi = 38750
voyager2 = sphere(m = 721.9, radius = 1E10, v = vector(voyager2_vi * (norm(Earth.v).x * cos(theta) - norm(Earth.v).y * sin(theta)), voyager2_vi * (norm(Earth.v).x * sin(theta) + norm(Earth.v).y * cos(theta)), 0))
stars = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, voyager2]
vxgraph = graph(title = 'vxgraph', width = 400, height = 400, align = 'left', xtitle = "distance from sun (AU)", ytitle = "velocity (km/s)")
c = gcurve(graph = vxgraph, color = color.blue, width = 4)
def G_force(M, m, pos_M, pos_m):
    return -G * M * m / mag2(pos_m - pos_M) * norm(pos_m - pos_M)

dt = 60 * 60 * 4

voyager2.pos = Earth.pos + voyager2.v * dt

while True:
    rate(10000)
    scene.center = voyager2.pos#可註解
    #scene.forward = norm(voyager2.v)#可註解
    for target in stars:
        target.a = G_force(Sun.m, target.m, Sun.pos, target.pos) / target.m
        for star in stars:
            if target != star:
                target.a += G_force(star.m, target.m, star.pos, target.pos) / target.m
    for target in stars:
        target.v += target.a * dt
        target.pos += target.v * dt
    c.plot(mag(voyager2.pos) / 149597870700, mag(voyager2.v) / 1000)




              
