from vpython import *
pos, angle = vector(0, 0, 0), 0

def right(b): #callback function
    global pos, angle
    pos = pos + vector(0.1, 0, 0)
    
def left(b):
    global pos, angle
    pos = pos + vector(-0.1, 0, 0)
    
scene = canvas(width=400, height=400, range = 5, background=color.white)
ball = sphere(radius = 2.0, texture=textures.earth )
button(text='right', pos=scene.title_anchor, bind = right)
button(text='left', pos=scene.title_anchor, bind = left)

while True:
    rate(1000)
    ball.rotate(angle=pi/600, axis= vector(sin(angle),cos(angle),0), origin=pos)
    ball.pos = pos
