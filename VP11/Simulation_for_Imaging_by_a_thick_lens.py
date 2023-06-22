from vpython import *

scene = canvas(background=vec(0.8, 0.8, 0.8), width=1200, height=300, center=vec(3, 0, 10), fov=0.004)

lens_surface1 = shapes.arc(radius=0.15, angle1=0, angle2=pi)
circle1 = paths.arc(pos=vec(0, 0, 0), radius=0.0000001, angle2=2 * pi, up=vec(1, 0, 0))
lens_surface2 = shapes.arc(radius=0.15, angle1=-pi, angle2=0)
circle2 = paths.arc(pos=vec(0, 0, 0), radius=0.0000001, angle2=2 * pi, up=vec(1, 0, 0))
extrusion(path=circle1, shape=lens_surface1, color=color.yellow, opacity=0.6)
extrusion(path=circle2, shape=lens_surface2, color=color.yellow, opacity=0.6)
curve(pos=[vec(-7, 0, 0), vec(13, 0, 0)], color=color.red, radius=0.02)
arrow(pos=vec(-6, 0, 0), axis=vec(0, 0.5, 0), shaftwidth=0.1)
arrow(pos=vec(12, 0, 0), axis=vec(0, -1, 0), shaftwidth=0.1)


def refraction_vector(n1, n2, v_in, normal_v):
    # find the unit vector of velocity of the outgoing ray
    sin2 = n1 / n2 * sin(diff_angle(v_in, normal_v))
    cos2 = sqrt(1 - sin2 ** 2)
    dir = cross(v_in, normal_v).z
    dir = -dir / abs(dir)
    sin2 *= dir
    v_out = vec(normal_v.x * cos2 - normal_v.y * sin2, normal_v.x * sin2 + normal_v.y * cos2, 0)
    return norm(v_out)

R = 4.0
thickness = 0.3
g1center = vec(-R + thickness / 2, 0, 0)
g2center = vec(R - thickness / 2, 0, 0)
nair = 1
nglass = 1.5

for angle in range(-7, 2):
    ray = sphere(pos=vec(-6, 0.5, 0), color=color.blue, radius=0.01, make_trail=True)
    ray.v = vector(cos(angle / 40.0), sin(angle / 40.0), 0)

    dt = 0.002

    count = 0
    while True:
        rate(1000)
        ray.pos = ray.pos + ray.v * dt

        # your code here
        if count == 0 and mag(ray.pos - g2center) < 4:
            ray.v = refraction_vector(nair, nglass, ray.v, norm(g2center - ray.pos))
            count += 1
        if count == 1 and mag(ray.pos - g1center) > 4:
            ray.v = refraction_vector(nglass, nair, ray.v, norm(ray.pos - g1center))
            count += 1

        if ray.pos.x >= 12:
            print(ray.pos.y)
            break