from vpython import *

""" CALCULATIONS

Equation: thrust = dm/dt*v_rel = m*a

const thrust = 2.31e6 N
let dm = 1 kg
let dt = 0.001

-> v_rel = thrust*dt/dm

"""

# parameters
G = 6.673E-11
AU = 149597870700

rocket_thrust = 1.06e7 # N -> 10586.8kg
dt = 0.001 # s
dm = 120*dt # kg -> Titan IIIE burns for 120 seconds
v_rel = rocket_thrust*dt/dm # m/s
fuel_radius = 2000 # m 
fuel_mass = 1.18e5 # kg -> 118300 kg
t_max = 3 # max loop time

earth_radius = 6.37e6 # m
earth_mass = 5.97e24 # kg
earth_period = 86400 # s

mass = {'Sun': 1.99E30, 'Mercury': 3.30E23, 'Venus': 4.87E24, 'Earth': 5.97E24, 'Mars': 6.42E23, 'Jupiter': 1.90E27, 'Saturn': 5.68E26, 'Uranus': 8.68E25, 'Neptune': 1.02E26}
radius = {'Sun': 6.95E8*50, 'Mercury': 2.439E6 * 1000, 'Venus': 6.051E6*1000, 'Earth': 6.371E6*1000, 'Mars': 3.389E6 * 1000, 'Jupiter': 6.991E7 * 500, 'Saturn': 5.823E7 * 500, 'Uranus': 2.536E7 * 800, 'Neptune': 2.462E7 * 1000}     #many times larger for better view
pos_x = {'Mercury': 2.277E+10, 'Venus': 6.289E+10, 'Earth': 1.300E+11, 'Mars': 1.623E+11, 'Jupiter': 1.301E+11, 'Saturn': -1.103E+12, 'Uranus': -2.157E+12, 'Neptune': -1.244E+12}
pos_y = {'Mercury': -5.729E+10, 'Venus': 8.991E+10, 'Earth': -7.644E+10, 'Mars': 1.565E+11, 'Jupiter': 7.562E+11, 'Saturn': 8.183E+11, 'Uranus': -1.737E+12, 'Neptune': -4.348E+12}
v_x = {'Mercury': 4.103E+04, 'Venus': -2.859E+04, 'Earth': 1.451E+04, 'Mars': -1.688E+04, 'Jupiter': -1.304E+04, 'Saturn': -5.970E+03, 'Uranus': 4.447E+03, 'Neptune': 5.247E+03}
v_y = {'Mercury': 1.631E+04, 'Venus': 2.000E+04, 'Earth': 2.579E+04, 'Mars': 1.750E+04, 'Jupiter': 2.244E+03, 'Saturn': -8.049E+03, 'Uranus': -5.523E+03, 'Neptune': -1.501E+03}

voyager2_vi = 38750
voyager2_theta = 0.04608421379889

# class rocket
class Rocket:
    def __init__(self):
        self.m = 6.32e5 # kg
        self.d = 3.05*10000 # m
        self.h = 48.8*10000 # m
        self.pos = vec(0,0,0)
        self.v = vec(0,0,0)
        self.v_init = vec(0,0,0)
        self.a = vec(0,0,0)
        self.el = arrow(canvas=scene_rocket, pos=self.pos+vec(0,0,0), axis=vec(self.h,0,0), color=vec(0.9,0.9,0.9), round=True, shaftwidth=self.d, headwidth=self.d)
        
    def change_pos(self, delta_pos):
        self.pos += delta_pos
        self.el.pos += delta_pos
    
    def change_v(self, delta_v):
        # set axis direction using v
        self.v += delta_v
        if mag(self.v) == 0:
            return
        self.el.axis = mag(self.el.axis)*norm(self.v)

# cunction G_force
def G_force(M, m, pos_M, pos_m):
    return -G * M * m / mag2(pos_m - pos_M) * norm(pos_m - pos_M)

# objects: rocket
scene_rocket = canvas(width=800, height=800, background=vec(0,0,0), align = 'left')
scene_rocket.range = 1e6
scene_rocket.up = vec(1,0,0)
scene_rocket.forward = vec(0,1,0)
distant_light(canvas=scene_rocket, direction=vec(1,0,0),color=color.white)

# rocket: initialize
rocket = Rocket()

# earth: initialize
earth = sphere(canvas=scene_rocket, pos=vec(0,0,0), radius=earth_radius, texture={"file":textures.earth})
earth.rotate(angle=240, axis=vec(0,1,0), origin=vec(0,0,0))

# rocket: move to earth edge
rocket.change_pos(vec(earth_radius, 0, 0))

# earth spin
rocket.v_init = vec(0,0,-earth_radius*4*pi**2/earth_period/earth_period)

#plot
v_graph = graph(width = 500, height = 250, align = 'right', title='<b>Rocket Velocity</b>', xtitle='<i>t</i>', ytitle='<i>v</i>')
v_curve = gcurve(graph=v_graph, color=color.blue)
a_graph = graph(width = 500, height = 250, align = 'right', title='<b>Rocket Acceleration</b>', xtitle='<i>t</i>', ytitle='<i>a</i>')
a_curve = gcurve(graph=a_graph, color=color.blue)
m_graph = graph(width = 500, height = 250, align = 'right', title='<b>Rocket Mass</b>', xtitle='<i>t</i>', ytitle='<i>m</i>')
m_curve = gcurve(graph=m_graph, color=color.blue)

# rocket countdown
for i in [3,2,1]:
    scene_rocket.center = rocket.pos
    countdown = text(canvas=scene_rocket, text=str(i), pos=rocket.pos + vec(0, 0, rocket.h), height=rocket.d*10, color=color.yellow)
    countdown.rotate(angle=pi/2, axis=vec(1,0,0), origin=countdown.pos)
    countdown.rotate(angle=pi/2, axis=vec(0,1,0), origin=countdown.pos)
    sleep(1)
    countdown.pos = vec(0,0,0)

# run rocket simulation
t = 0
dm_array = []
while t < t_max: # Titan IIIE burned fuel for 985 seconds
    rate(1//dt)

    # rocket thrust
    if fuel_mass > 0:
        dm_ball = sphere(canvas=scene_rocket, pos=rocket.pos+vec(0,(random()-0.5)*rocket.d,(random()-0.5)*rocket.d), radius=fuel_radius, color=vec(1,0.3,0))
        dm_ball.v = rocket.v - v_rel*rocket.v.norm()
        dm_array.append(dm_ball)
        if len(dm_array) > 10000: # prevent program crash
            dm_array.pop(0)
        for dm_el in dm_array:
            dm_el.pos += dm_el.v*dt

    # rocket movement
    rocket.m -= dm
    fuel_mass -= dm
    a_t = rocket_thrust*v_rel*rocket.el.axis.norm()/rocket.m # thrust
    a_g = -G*earth_mass/mag2(rocket.pos)*rocket.pos.norm() # gravity
    rocket.a = a_t + a_g
    rocket.change_v(rocket.a*dt)
    rocket.change_pos(rocket.v*dt+rocket.v_init*dt)

    v_curve.plot(pos=(t,mag(rocket.v+rocket.v_init)))
    a_curve.plot(pos=(t,mag(rocket.a)))
    m_curve.plot(pos=(t,rocket.m))

    t += dt
    scene_rocket.center = rocket.pos

# objects: voyager 2
scene_voyager2 = canvas(width = 800, height = 800, background = color.black, align = 'left')
Sun = sphere(canvas=scene_voyager2, m = mass['Sun'], radius = radius['Sun'], color = color.orange, pos = vector(0, 0, 0), emissive = True)
Mercury = sphere(canvas=scene_voyager2, m = mass['Mercury'], radius = radius['Mercury'], texture={'file':textures.stones}, pos = vector(pos_x['Mercury'], pos_y['Mercury'], 0), v = vector(v_x['Mercury'], v_y['Mercury'], 0), emissive = True, make_trail = True, trail_radius = radius['Mercury'] / 3, trail_color = vector(94 / 255, 94 / 255, 94 / 255))
Venus = sphere(canvas=scene_voyager2, m = mass['Venus'], radius = radius['Venus'], color = vector(248 / 255, 183 / 255, 83 / 255), pos = vector(pos_x['Venus'], pos_y['Venus'], 0), v = vector(v_x['Venus'], v_y['Venus'], 0), emissive = True, make_trail = True, trail_radius = radius['Venus'] / 3)
Earth = sphere(canvas=scene_voyager2, m = mass['Earth'], radius = radius['Earth'], texture={'file':textures.earth}, pos = vector(pos_x['Earth'], pos_y['Earth'], 0), v = vector(v_x['Earth'], v_y['Earth'], 0), emissive = True, make_trail = True, trail_radius = radius['Earth'] / 3, trail_color = vector(15 / 255, 76 / 255, 129 / 255))
Mars = sphere(canvas=scene_voyager2, m = mass['Mars'], radius = radius['Mars'], color = color.red, pos = vector(pos_x['Mars'], pos_y['Mars'], 0), v = vector(v_x['Mars'], v_y['Mars'], 0), emissive = True, make_trail = True, trail_radius = radius['Mars'] / 3)
Jupiter = sphere(canvas=scene_voyager2, m = mass['Jupiter'], radius = radius['Jupiter'], texture={'file':textures.wood_old}, pos = vector(pos_x['Jupiter'], pos_y['Jupiter'], 0), v = vector(v_x['Jupiter'], v_y['Jupiter'], 0), emissive = True, make_trail = True, trail_radius = radius['Jupiter'] / 3, trail_color = vector(170 / 255, 115 / 255, 94 / 255))
Saturn = sphere(canvas=scene_voyager2, m = mass['Saturn'], radius = radius['Saturn'], texture={'file':textures.wood}, pos = vector(pos_x['Saturn'], pos_y['Saturn'], 0), v = vector(v_x['Saturn'], v_y['Saturn'], 0), emissive = True, make_trail =  True, trail_radius = radius['Saturn'] / 3, trail_color = vector(184 / 255, 158 / 255, 131 / 255))
Uranus = sphere(canvas=scene_voyager2, m = mass['Uranus'], radius = radius['Uranus'], color = color.cyan, pos = vector(pos_x['Uranus'], pos_y['Uranus'], 0), v = vector(v_x['Uranus'], v_y['Uranus'], 0), emissive = True, make_trail = True, trail_radius = radius['Uranus'] / 3)
Neptune = sphere(canvas=scene_voyager2, m = mass['Neptune'], radius = radius['Neptune'], color = color.blue, pos = vector(pos_x['Neptune'], pos_y['Neptune'], 0), v = vector(v_x['Neptune'], v_y['Neptune'], 0), emissive = True, make_trail = True, trail_radius = radius['Neptune'] / 3)

vx_graph = graph(title = '<b>v-x graph</b>', width = 500, height = 500, align = 'right', xtitle = "distance from sun (<i>AU</i>)", ytitle = "velocity (<i>km/s</i>)")
vx_curve = gcurve(graph = vx_graph, color = color.blue, width = 4)

voyager2 = sphere(canvas=scene_voyager2, m = 721.9, radius = 1E10, v = vector(voyager2_vi * (norm(Earth.v).x * cos(voyager2_theta) - norm(Earth.v).y * sin(voyager2_theta)), voyager2_vi * (norm(Earth.v).x * sin(voyager2_theta) + norm(Earth.v).y * cos(voyager2_theta)), 0), make_trail=True)
stars = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, voyager2]

# Run voyager 2 simulation
dt = 60 * 60 * 4
voyager2.pos = Earth.pos + voyager2.v * dt

while True:
    rate(5000)
    # scene.center = voyager2.pos # center at the position of the voyager 2
    # scene.forward = norm(voyager2.v) # watch in the direction of the voyager 2
    for target in stars:
        target.a = G_force(Sun.m, target.m, Sun.pos, target.pos) / target.m
        for star in stars:
            if target != star:
                target.a += G_force(star.m, target.m, star.pos, target.pos) / target.m
    for target in stars:
        target.v += target.a * dt
        target.pos += target.v * dt
    vx_curve.plot(mag(voyager2.pos) / AU, mag(voyager2.v) / 1000)
