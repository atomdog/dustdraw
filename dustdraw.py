import tkinter
import time
import random
import keyboard
# width of the animation window
animation_window_width=1000
# height of the animation window
animation_window_height=1000
# initial x position of the ball
animation_ball_start_xpos = 50
# initial y position of the ball
animation_ball_start_ypos = 50
# radius of the ball
animation_ball_radius = 5
# the pixel movement of ball for each iteration
animation_ball_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 0.001
Alist = [[0,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10, 10],[20, 20],[30, 30], [40,40], [50,50], [20,30],[10,30]]
Blist = [[0,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10,0],[20,0],[20,10],[20,20],[20,20],[10,20],[10,30],[20,30],[30,30],[30,40],[30,50],[20,50],[10,50]]
Clist = [[0,0],[10,0],[20,0],[30,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10,50],[20,50],[30,50]]
Dlist = [[0,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10,0],[20,10],[30,20],[30,30],[20,40],[10,50]]
Elist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50],[10,0],[20,0],[30,0],[10,20],[20,20],[10,50],[20,50],[30,50]]
Flist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50],[10,0],[20,0],[30,0],[10,20],[20,20]]
Glist = [[0,0],[10,0],[20,0],[30,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10,50],[20,50],[30,50],[30,30],[30,30],[40,30]]
Hlist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50],[40,0],[40,10], [40,20],[40,30],[40,40], [40,50],[10,30],[20,30],[30,30]]
Ilist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50]]
Jlist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50], [10,50], [20,50], [20,40]]
Klist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50], [10,30],[20,20], [30,10], [20,40],[30,50]]
Llist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50],[10,50],[20,50], [30,50]]
Mlist = [[0,10], [0,20],[0,30],[0,40], [0,50],[20,10], [20,20],[20,30],[20,40], [20,50],[40,10], [40,20],[40,30],[40,40], [40,50],[10,10],[30,10]]
Nlist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50],[40,0],[40,10], [40,20],[40,30],[40,40], [40,50],[10,10],[20,20],[30,30],[40,40]]
Olist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50],[20,0],[20,10], [20,20],[20,30],[20,40], [20,50],[10,50],[10,0]]
Plist = [[0,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10,0],[20,0],[30,0],[30,10],[30,20],[20,20],[10,20]]
Qlist = [[0,0],[0,10], [0,20],[0,30],[0,40], [0,50],[20,0],[20,10], [20,20],[20,30],[20,40], [20,50],[10,50],[10,0], [30,40]]
Rlist = [[0,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10,0],[20,0],[30,0],[30,10],[30,20],[20,20],[10,20],[30,30],[40,40]]
Slist = [[0,0],[0,10],[10,0],[20,0],[30,0],[0,20],[10,20],[20,20],[30,20],[30,30], [30,40], [20,40], [10,40],[0,40]]
Tlist = [[0,0],[10,10], [10,0],[10,20],[10,30],[10,40], [10,50],[20,0]]
Ulist = [[0,0],[0,10],[0,20],[0,30],[0,40],[0,50],[10,50], [20,50],[30,50],[40,50],[40,40],[40,30],[40,20],[40,10],[40,0]]
Vlist = [[0,0],[0,10],[0,20],[10,30],[20,40],[30,30],[40,20],[40,10],[40,0]]
Wlist = [[0,0],[0,10],[0,20],[10,10],[20,0],[30,10],[40,20],[40,10],[40,0]]
Ylist = [[0,0]]
Zlist = []
zerolist = []
onelist = []
twolist = []
threelist = []
fourlist = []
fivelist = []
sixlist = []
sevenlist = []
eightlist = []
ninelist = []

alpha = {"A": Alist, "I": Ilist, "B": Blist, "C": Clist, "D": Dlist,"E": Elist, "F": Flist, "G": Glist, "H":Hlist,"I":Ilist,"J":Jlist,"K":Klist,"L":Llist,"M":Mlist,"N":Nlist,
"O":Olist,"P": Plist, "Q": Qlist, "R": Rlist, "S": Slist, "T":Tlist, "U": Ulist, "V": Vlist, "W": Wlist, "Y": Ylist}
class node:
    def __init__(self, window, canvas,xpos, ypos, conscripted, xvel, yvel):
        self.xpos = xpos
        self.ypos = ypos
        self.rx = None
        self.ry = None
        self.xvel=random.randint(-5,5)
        self.yvel=random.randint(-5,5)
        self.conscripted = False
        self.star = canvas.create_oval(self.xpos,self.ypos, self.xpos+4, self.ypos+4,fill="black", outline="black", width=1)
    def getxvel(self):
        return(self.xvel)
    def getyvel(self):
        return(self.yvel)
    def getStar(self):
        return(self.star)
    def getConscripted(self):
        return(self.conscripted)
    def release(self):
        self.conscripted=False
        self.changeColor(animation_window,animation_canvas,"black")
        #self.changeSize(animation_window,animation_canvas, 1)
        self.rx=None
        self.ry=None
        self.xvel=random.randint(-5,5)
        self.yvel=random.randint(-5,5)
    def changeColor(self, window, canvas, color):
        canvas.itemconfig(self.star, fill=color)
    def changeSize(self, window, canvas, width2):
        canvas.itemconfig(self.star, width=width2)




# The main window of the animation
def create_animation_window():
  window = tkinter.Tk()
  window.title("Tkinter Animation Demo")
  # Uses python 3.6+ string interpolation
  window.geometry(f'{animation_window_width}x{animation_window_height}')
  return window

def conscript(window,canvas, nodelist, letter, xdest ,ydest):

    for p in range(0, len(alpha[letter])):
        F = node(animation_window, animation_canvas,random.randrange(50, 1000),random.randrange(50, 1000),False,0,0)
        nodelist.append(F)
    for x in range(0, len(alpha[letter])):

        #assign random node to be pixel in letter
        randomnodeindex = random.randint(0,len(nodelist)-1)
        while(nodelist[randomnodeindex].getConscripted()==True):
            randomnodeindex = random.randint(0,len(nodelist)-1)
        #verify conscription
        currentnode = nodelist[randomnodeindex]
        currentnode.conscripted=True
        #calculate destination
        destinationx = xdest+ alpha[letter][x][0]/2
        destinationy = ydest+ alpha[letter][x][1]/2
        currentnode.changeColor(animation_window,animation_canvas,"white")
        #currentnode.changeSize(animation_window, animation_canvas, 10)
        currentnode.rx = destinationx
        currentnode.ry = destinationy
        nodePos = canvas.coords(currentnode.getStar())
        xl,yl,xr,yr = nodePos
        rise = destinationy - ((yl+yr)/2)
        run = destinationx -  ((xl+xr)/2)
        rise=rise*0.1
        run=run*0.1
        currentnode.yvel=rise
        currentnode.xvel=run
def resetConscriptVelocities(window, canvas, nodelist, nodeindex):
    currentnode=nodelist[nodeindex]
    nodePos = canvas.coords(currentnode.getStar())
    xl,yl,xr,yr = nodePos
    rise = currentnode.ry - ((yl+yr)/2)
    run = currentnode.rx -  ((xl+xr)/2)
    rise=rise*0.2
    run=run*0.2
    currentnode.yvel=rise
    currentnode.xvel=run


# Create a canvas for animation and add it to main window
def create_animation_canvas(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg="black")
  canvas.pack(fill="both", expand=True)
  return canvas

# Create and animate ball in an infinite loop
def animatefunc(window, canvas,xinc,yinc):
  #ball = canvas.create_oval(animation_ball_start_xpos-animation_ball_radius,
    #        animation_ball_start_ypos-animation_ball_radius,
    #        animation_ball_start_xpos+animation_ball_radius,
    #        animation_ball_start_ypos+animation_ball_radius,
    #        fill="black", outline="white", width=1)

  nodelist =[]
  Timer = True
  while True:
    for y in range(0, len(nodelist)):
        canvas.move(nodelist[y].getStar(),nodelist[y].getxvel(),nodelist[y].getyvel())
        #nodelist[y].nodeMove(random.randrange(-1, 1), random.randrange(-1, 1))
    window.update()
    time.sleep(animation_refresh_seconds)
    for y in range(0, len(nodelist)):
        nodePos = canvas.coords(nodelist[y].getStar())
    #ball_pos = canvas.coords(nodelist[0])
    # unpack array to variables

        xl,yl,xr,yr = nodePos
        #print("======")
        #print((xl+xr)/2)
        #print((yl+yr)/2)
        #print("-----")
        #print(nodelist[y].rx)
        #print(nodelist[y].ry)
        #print("======")
        if xl < abs(xinc) or xr > animation_window_width-abs(xinc):
            nodelist[y].xvel = -nodelist[y].getxvel()
        if yl < abs(yinc) or yr > animation_window_height-abs(yinc):
          nodelist[y].yvel = -nodelist[y].getyvel()

          #conscripted attendance check
        if(nodelist[y].conscripted==True):
            #print("GOT CONSCRIPTED NODE")
            #print("DESTINATION: "+ str(nodelist[y].ry))
            #print(xl)
            resetConscriptVelocities(animation_window,animation_canvas,nodelist,y)
            if(int((xl+xr)/2)==nodelist[y].rx and int((yl+yr)/2)==nodelist[y].ry):
                nodelist[y].yvel=0
                nodelist[y].xvel=0

        if keyboard.is_pressed('q'):
            for it in range(0, len(nodelist)):
                nodelist[it].release()
            Timer = True
            nodelist = []
            break

    if keyboard.is_pressed('a') and Timer == True:

        conscript(animation_window, animation_canvas, nodelist, "A",250,250)
        conscript(animation_window, animation_canvas, nodelist, "B",310,250)
        conscript(animation_window, animation_canvas, nodelist, "C",360,250)
        conscript(animation_window, animation_canvas, nodelist, "D",410,250)
        conscript(animation_window, animation_canvas, nodelist, "E",460,250)
        conscript(animation_window, animation_canvas, nodelist, "F",510,250)
        conscript(animation_window, animation_canvas, nodelist, "G",560,250)
        conscript(animation_window, animation_canvas, nodelist, "H",610,250)
        conscript(animation_window, animation_canvas, nodelist, "I",660,250)
        conscript(animation_window, animation_canvas, nodelist, "J",680,250)
        conscript(animation_window, animation_canvas, nodelist, "K",720,250)
        conscript(animation_window, animation_canvas, nodelist, "L",770,250)
        conscript(animation_window, animation_canvas, nodelist, "M",820,250)
        conscript(animation_window, animation_canvas, nodelist, "N",880,250)
        conscript(animation_window, animation_canvas, nodelist, "O",250,350)
        conscript(animation_window, animation_canvas, nodelist, "P",300,350)
        conscript(animation_window, animation_canvas, nodelist, "Q",350,350)
        conscript(animation_window, animation_canvas, nodelist, "R",400,350)
        conscript(animation_window, animation_canvas, nodelist, "S",450,350)
        conscript(animation_window, animation_canvas, nodelist, "T",500,350)
        conscript(animation_window, animation_canvas, nodelist, "U",550,350)
        conscript(animation_window, animation_canvas, nodelist, "V",600,350)
        conscript(animation_window, animation_canvas, nodelist, "W",650,350)
        conscript(animation_window, animation_canvas, nodelist, "Y",700,350)
        print(len(nodelist))
        Timer = False








# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)



Timer = True

animatefunc(animation_window,animation_canvas, animation_ball_min_movement, animation_ball_min_movement)
