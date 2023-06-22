from vpython import *

# constants
size =1 # block size
state=0
# gui setup
scene1 = canvas(width=1300, height=600, align='left', background=vec(0,0,0))
# scene2 = canvas(width=600, height=600, align='right', background=vec(0,0,0))

# list of Block objects
blocks = []
blocks2 = []
# class Block
class Block(box):
    def __init__(self, x=0, y=0, z=0, l=size, h=size, w=size, r=1, g=1, b=1, canvas=scene1):
        # containing the data of the block
        self.data = [x,y,z,l,h,w,r,g,b]
        self.data_const = [x,y,z,l,h,w,r,g,b]
        self.kw = {'x': 0, 'y': 1, 'z': 2, 'l': 3, 'h': 4, 'w': 5, 'r': 6, 'g': 7, 'b': 8}
        # constructing the physical object
        super().__init__(canvas=canvas, pos=vec(x,y,z), length=l, height=h, width=w, color=vec(r,g,b))

    # update data using keywords
    # ex: block.updateKw(x=0, y=1, b=5)
    def updateKw(self, **kwargs):
        for key in kwargs:
            index = self.kw[key]
            # check if need to update
            if self.data[index] != kwargs[key]:
                self.data[index] = kwargs[key]
                if index == 0: self.pos.x = kwargs[key]
                elif index == 1: self.pos.y = kwargs[key]
                elif index == 2: self.pos.z = kwargs[key]
                elif index == 3: self.length = kwargs[key]
                elif index == 4: self.height = kwargs[key]
                elif index == 5: self.width = kwargs[key]
                elif index == 6: self.color.x = kwargs[key]
                elif index == 7: self.color.y = kwargs[key]
                elif index == 8: self.color.z = kwargs[key]

    # update pos parameters using indecies
    def updatePos(self, x, y, z):
        self.updateKw(x=x, y=y, z=z)

    # update size parameters using indecies
    def updateSize(self, l, h, w):
        self.updateKw(l=l, h=h, w=w)

    # update color parameters using indecies
    def updateColor(self, r, g, b):
        self.updateKw(r=r, g=g, b=b)

    # update all parameters using indecies
    def updateAll(self,x,y,z,l,h,w,r,g,b):
        self.updateSize(x,y,z)
        self.updatePos(l,h,w)
        self.updateColor(r,g,b)

# functions

# create 3d rectangle using unit blocks of size 'size'
def cuboid(x=0, y=0, z=0, l=size, h=size, w=size, r=1, g=1, b=1, canvas=scene1):
    for i in range(l//size):
        for j in range(h//size):
            for k in range(w//size):
                if state==0:
                    blocks.append(Block(x+i*size, y+j*size, z+k*size, size, size, size, r, g, b, canvas))
                else:
                    blocks2.append(Block(x+i*size, y+j*size, z+k*size, size, size, size, r, g, b, canvas))

# create a 3d circle using unit blocks of size 'size'
# specify: upper-half: 1, lower-half: -1
# inverse: 0, 1
def circleXY(x=0, y=0, z=0, radius=size, w=size, r=1, g=1, b=1, canvas=scene1, specify=0, inverse=0):
    for i in range(-radius//size, radius//size):
        for j in range((-radius//size)*(specify!=1), (radius//size)*(specify!=-1)):
            for k in range(w//size):
                if (((i+0.5)*size)**2 + ((j+0.5)*size)**2 <= radius**2)^inverse:
                    if state==0:
                        blocks.append(Block(x+i*size, y+j*size, z+k*size, size, size, size, r, g, b, canvas))
                    else:
                        blocks2.append(Block(x+i*size, y+j*size, z+k*size, size, size, size, r, g, b, canvas))

# create a 3d triangle using unit blocks of size 'size'
def triangleXY(x=0, y=0, z=0, base=size, height=size, w=size, r=1, g=1, b=1, canvas=scene1):
    for i in range(base//size):
        for j in range(height//size):
            for k in range(w//size):
                if (base/2/height*j*size < i*size < base/2/height*(2*height-j*size)):
                    if state==0:
                        blocks.append(Block(x+i*size, y+j*size, z+k*size, size, size, size, r, g, b, canvas))
                    else:
                        blocks2.append(Block(x+i*size, y+j*size, z+k*size, size, size, size, r, g, b, canvas))

# create NTU Library
def libraryNTU(canvas=scene1, x=0, y=0, z=0):
    r = 0.66
    g = 0.375
    b = 0.246
    # front triangle+semicircle+rectangle
    cuboid(x-20, y, z+15, 10, 30, 1, r, g, b, canvas)
    cuboid(x+10, y, z+15, 10, 30, 1, r, g, b, canvas)
    cuboid(x-10, y, z+15, 20, 30, 1, 0.2, 0.2, 0.2, canvas)
    cuboid(x-20, y+30, z+14, 40, 15, 1, 1, 1,0.9, canvas)
    circleXY(x, y+30, z+15, 10, 1, 0.2, 0.2, 0.2, canvas)
    triangleXY(x-20, y+45, z+14, 40, 10, 1, 1, 1,0.9, canvas)

    # back triangle+circle+rectangle
    cuboid(x-30, y, z, 10, 45, 1, r, g, b, canvas)
    cuboid(x+20, y, z, 10, 45, 1, r, g, b, canvas)
    cuboid(x-30, y+45, z, 60, 15, 1, r, g, b, canvas)
    circleXY(x, y+62, z+1, 3, 1, 0.2, 0.2, 0.2, canvas)
    triangleXY(x-30, y+60, z, 60, 15, 1, r, g, b, canvas)

    # side rectangles
    for x0 in (x-80, x+30):
        cuboid(x0, y, z+5, 10, 55, 1, r, g, b, canvas)
        cuboid(x0+40, y, z+5, 10, 55, 1, r, g, b, canvas)
        cuboid(x0+10, y, z+10, 30, 65, 1, r, g, b, canvas)
        cuboid(x0+18, y+15, z+11, 14, 10, 1, 1, 1,0.9, canvas)
        cuboid(x0+20, y+25, z+11, 10, 10, 1, 1, 1,0.9, canvas)
        circleXY(x0+25, y+35, z+11, 7, 1, 1, 1,0.9, canvas, 1)
        cuboid(x0+18, y+55, z+11, 14, 10, 1, 1, 1,0.9, canvas)

    # arcs below
    for x0 in list(range(x-88, x-24, 16))+list(range(x+24, x+88, 16)):
        cuboid(x0, y-30, z+20, 1, 23, 1, 1, 1,0.9, canvas)
        cuboid(x0+15, y-30, z+20, 1, 23, 1, 1, 1,0.9, canvas)
        circleXY(x0+8, y-14, z+20, 7, 1, 1, 1,0.9, canvas, 1, 1)
        cuboid(x0, y-8, z+20, 16, 8, 1, 1, 1,0.9, canvas)

    # arcs middle
    for x0 in range(x-24, x+24, 16):
        cuboid(x0, y-30, z+22, 1, 23, 1, r, g, b, canvas)
        cuboid(x0+15, y-30, z+22, 1, 23, 1, r, g, b, canvas)
        circleXY(x0+8, y-14, z+22, 7, 1, r, g, b, canvas, 1, 1)
        cuboid(x0, y-8, z+22, 16, 10, 1, r, g, b, canvas)
        
# model initialization

libraryNTU(scene1)
state=1
# libraryNTU(scene2)

# main simulation
def posi(i):
    return vec(i,i,0)
ball=sphere(pos=vec(0,0,0),radius=0.1,canvas=scene1,v=vec(0,0,0))

betaX=0
betaY=0
betaZ=0
gammaX=0
gammaY=0
gammaZ=0

betap=0

vprime=vec(0,0,0)
c=2
t=0
dt=0.01

temp_color=vec(0,0,0)
new_color=vec(0,0,0)

def keyInput(evt):
    global c
    if evt.key=='left':
        if ball.v.x<=0.95 and ball.v.x>= -0.95:
            ball.v.x-=0.05
        else:
            if ball.v.x<0:
                ball.v.x=-1
            else:
                ball.v.x=1
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='right':
        if ball.v.x<=0.95 and ball.v.x>= -0.95:
            ball.v.x+=0.05
        else:
            if ball.v.x<0:
                ball.v.x=-1
            else:
                ball.v.x=1
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='up':
        if ball.v.y<=0.95 and ball.v.y>= -0.95:
            ball.v.y+=0.05
        else:
            if ball.v.y<0:
                ball.v.y=-1
            else:
                ball.v.y=1 
        print('velocity:',ball.v,' ','light speed:', c )
        # ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='down':
        if ball.v.y<=0.95 and ball.v.y>= -0.95:
            ball.v.y-=0.05
        else:
            if ball.v.y<0:
                ball.v.y=-1
            else:
                ball.v.y=1
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='w':
        if ball.v.z<=0.95 and ball.v.z>= -0.95:
            ball.v.z+=0.05
        else:
            if ball.v.z<0:
                ball.v.z=-1
            else:
                ball.v.z=1        
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='s':
        if ball.v.z<=0.95 and ball.v.z>= -0.95:
            ball.v.z-=0.05
        else:
            if ball.v.z<0:
                ball.v.z=-1
            else:
                ball.v.z=1 
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='+':
        c+=0.1
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='-':
        if c>=1.9:
            c-=0.1
        else:
            c=1.8
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    if evt.key=='r':
        ball.v=vec(0,0,0)
        c=2
        print('velocity:',ball.v,' ','light speed:', c )
        ChangePosSize(ball.v)
        ChangeColor(ball.v)
        return
    

def ChangePosSize(v):
    betaX=v.x/c
    betaY=v.y/c
    betaZ=v.z/c
    gammaX=1/(1-betaX**2)**(1/2)
    gammaY=1/(1-betaY**2)**(1/2)
    gammaZ=1/(1-betaZ**2)**(1/2)
    for el in blocks:
        el.updatePos(el.data_const[0]*gammaX , el.data_const[1]*gammaY , el.data_const[2]*gammaZ)
    return
el=blocks[0]
def ChangeColor(v):
    global el
    for el in blocks:
        if dot(v,el.pos-ball.pos) !=0:
            vprime=proj(v,el.pos-ball.pos)
            betap=( mag(vprime)*dot(v,el.pos-ball.pos)/abs(dot(v,el.pos-ball.pos)) )/ c
            temp_color=color.rgb_to_hsv(vec(el.data_const[6],el.data_const[7],el.data_const[8]))
            temp_color.x=((3*temp_color.x+4)*((1+betap)/(1-betap))**(1/2)-4)/3
            if temp_color.x>=1:
                temp_color.z=0
            if temp_color.x<=0:
                temp_color.z=0
            new_color=color.hsv_to_rgb(temp_color)
            el.updateColor(new_color.x,new_color.y,new_color.z)
        else:
            el.updateColor(el.data_const[6],el.data_const[7],el.data_const[8])
    return

scene1.bind('keydown',keyInput)
temp_color=vec(0,0,0)

while True:
    rate(1)