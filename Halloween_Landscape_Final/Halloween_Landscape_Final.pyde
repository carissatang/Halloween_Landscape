"""
Halloween Landscape

This is the group Halloween Landscape group project.
Group: Sridhar Sairam, Sarah Huang and Max Naegel

SRIDHAR
Program Overview:
Click the screen of the computer (white rectangle):
    enter the landcape of haunted corn maze...
    
SARAH
Program Overview:
(Admire the scernery then) Click the jackolantern for a surprise...

Max
Program Overview:

You will need the minim library to have this work which you can find here:
    http://code.compartmental.net/minim/distro/minim-2.2.2.zip

"""
#SRIDHAR
import random

#SARAH

x = 0
y = 0
slide = -1


def setup():
    #SRIDHAR
    size(900, 600)
    global do_once
    do_once = True
    global gametime
    gametime = False
    
    add_library('minim')
    global minim
    global player
    add_library('minim')
    minim = Minim(this)
    player = minim.loadFile("7_Days.mp3")
    
    global gametime
    
    global field_img
    field_img = loadImage("http://www.halloweennewengland.com/files/6714/6135/4833/Haunted_Corn_Maze_Halloween_New_England_850_2.jpg", "jpg")
    global img_x
    global car_img_x
    img_x = 0
    car_img_x = -200
    global static_img
    global car_img
    static_img = loadImage("https://cdn.wallpapersafari.com/37/41/QJVeW7.gif", "gif")
    car_img = loadImage("Car.png")
    
    #SARAH
    size(900, 600)
    global bush, pump1, star, pump, sunlight, hill, banner, witch, ghost, bat, pumpkin, mummy

    bush = loadImage ("bush.png")
    pump1 = loadImage("scarypump.png")
    star = loadImage ("star.png")
    pump = loadImage ("pump.png")
    sunlight = loadImage ("sunlight.png")
    hill = loadImage ("hill.png")
    banner = loadImage("halloween_banner.png")
    witch = loadImage("witch.png")
    ghost = loadImage("ghost.png")
    bat = loadImage("bat.png")
    pumpkin = loadImage("pumpkin.png")
    mummy = loadImage("mummy.png")
    
    global mummy_menu, dracula, franken
    
    mummy_menu = loadImage("mummy_menu.png")
    dracula = loadImage("dracula.png")
    franken = loadImage("franken.png")
        
    #MAX
    global haunted_house
    global pathway
    global cropfield
    global tree
    global tree_two
    global bush_max
    global red_eyes
    global crescent_moon
    global lightning
    size(900, 600)
    haunted_house = loadImage("Haunted_House.png")
    pathway = loadImage("Pathway.png")
    cropfield = loadImage("Cropfield.png")
    tree = loadImage("Tree.png")
    tree_two = loadImage("Tree_2.png")
    bush_max = loadImage("bush_max.png")
    red_eyes = loadImage("Red_Eyes.png")
    crescent_moon = loadImage("Crescent Moon.png")
    lightning = loadImage("Lightning.png")
    
global landscape
landscape = ""    

def draw():
    global landscape

    if landscape == "sridhar":
        game_time = False
        sridhar()
        game_time = True
    elif landscape == "sarah":
        sarah()
    elif landscape == "max":
        maximilian()
    else:
        line(width/3, 0, width/3, 600)
        line((width/3) * 2, 0, (width/3) * 2, 600)
        
        noStroke()    
        fill(0, 43, 127)
        rect(0, 0, width/3,600)
        fill(252, 209, 22)
        rect(300, 0, width/3, 600)
        fill(206, 17, 38)
        rect(600, 0, width/3*2, 600)
        
        image(franken, 25, 280, 250, 250)
        image(dracula, 380, 270, 125, 275)
        image(mummy_menu, 660, 300, 200, 230)
        
        fill(255)
        textSize(40)
        text("WELCOME TO", 25, 100)
        textSize(50)
        text("LANDSCAPES OF TRANSLYVANIA", 50, 400)

        textSize(36)
        fill(255)
        text("MAX", 100, 200)
        text("SARAH", 400, 250)
        text("&", 590, 275)
        text("SRIDHAR'S", 680, 300)
        
        if mousePressed and mouseX > (width/3) * 2:
            landscape = "sridhar"
        elif mousePressed and mouseX > (width/3):
            landscape = "sarah"
        elif mousePressed and mouseX < (width/3):
            landscape = "max"

#SRIDHAR
def sridhar():
    if not gametime:
        intro()
    elif gametime:
        scary_corn()

def scary_corn():
    background(0)
    global img_x
    global car_img_x
    image(field_img, img_x, 0, 1800, 600)
    image(car_img, car_img_x, 450, 150, 100)
    if keyPressed:
        img_x -= random.randint(1, 50)
        car_img_x += random.randint(1, 100)
    if img_x <= -850 or car_img_x >= 900:
        img_x = 0
        car_img_x = -200
        image(static_img, 0, 0, 900, 600)
        scream = str(random.randint(1, 7))
        scare = minim.loadFile(scream + ".wav")
        scare.play()

def mouseClicked():
    global gametime
    if (mouseX >= 220 and mouseX <= 670 and mouseY >= 130 and mouseY <= 380) and not gametime:
        gametime = True
        global player
        player.play()
        
def intro():
    global do_once
    if do_once:
        intro_background()
        do_once = False
    if frameCount % 60 == 0:
        intro_background()
    elif frameCount % 60 != 0:
        #crazy text (made it by mistake)
        fill(0, 150, 153, 90)
        textSize(10)
        text_x = random.randint(225, 550)
        text_y = random.randint(150, 350)
        text("CLICK THE SCREEN", text_x, text_y)

def intro_background():
    background(125, 156, 8)
    fill(0)
    rect(width/2 - 260, height/2 - 200, 500, 300) #besel
    fill(255)
    rect(width/2 - 232.5, height/2 - 175, 450, 250) #screen
    quad(width/2 - 260, 400, width/2 + 240, 400, 900, 600, 0, 600) #keyboard
    
    stroke(0)
    for i in range(10): #horizontal lines for keys
        line(190 + 50 * i, 400, 0 + 90 * i, 600)
        print("here")
    for i in range(0, 10, 2): #vertical lines for keys
        line(0 + 19 * i, 600 - 20 * i, 900 - 21 * i, 600 - 20 * i)
        print("there")
        
#SARAH
def sarah():
    global x
    global y

    if slide == 0:
        if x >= 1650:
            x = 0
                
        else:
            x += 2
    
        background(0, 51, 102)
        noStroke()
        
        #hill
        image(hill, -100, 250, 1200, 300)
        
        #light
        image(sunlight, 150, 200, 600, 600)
            
        #pumpkin
        image(pump, 0, 450, 100, 85)
        image(pump, 170, 450, 100, 85)
        image(pump, 630, 450, 100, 85)
        image(pump, 800, 450, 100, 85)
        
        #bushes
        fill(51, 73, 20)
        rect(0, 560, width, height)
        tint(100)
        image(bush, -170, 460, 400, 200)
        image(bush, 60, 460, 400, 200)
        image(bush, 290, 460, 400, 200)
        image(bush, 510, 460, 400, 200)
    
        
        #cresent moon
        fill(245, 227, 135)
        ellipse(width/3, height/4, 225,225)
        fill(0, 51, 102)
        ellipse(width/2.5, height/3.9, 150, 150)
        
        #pumpkin
        tint(255)
        image(pump, 10, 515, 100, 85)
        image(pump, 110, 515, 100, 85)
        image(pump, 600, 515, 100, 85)
        image(pump, 850, 515, 100, 85)
        
        #jackolantern
        image(pump1, 250, 260, 400, 350)
        
        #enter button
        fill(23,113,32)
        rect(340, 260, 200, 40,17)
        fill(255)
        stroke(255,45,234)
        textSize(20)
        text("Click to enter", 370, 285)    
        
        #stars
        image(star, x-50, height/12, 50, 50)
        image(star, x-100, height/4, 50, 50)
        image(star, x-200, height/8, 50, 50)
        image(star, x-300 , height/3, 50, 50)
        image(star, x-400, height/12.5, 50, 50)
        image(star, x-500, height/4.3, 50, 50)
        image(star, x-600, height/8, 50, 50)
        image(star, x-700 , height/3.7, 50, 50)
        
    elif slide == 1:
        if y >= 700:
            y = 35
            
        else:
            y += 3.5
        image(pumpkin, 0, 0, width, height)
        
        #bats
        image(bat, 300, 0, 150, 50)
        
        #ghost
        image(ghost, 540, y+35, 100, 100)
        image(ghost, 600, y+35*3, 100, 100)
        image(ghost, 660, y+35, 100, 100)
        
        #mummy
        image(mummy, 300, 200, 300, 400)
    
        #banner
        image(banner, 50, 25, 800, 200)
        
        #witch
        image(witch, 25, 300, 270, 280)
            
        textSize(18)
        text("Click twice to go back", 0, 590)

def mousePressed():
    global slide
    slide +=1
    if slide >= 3:
        slide = 0
#MAX
def maximilian():
    background(20)
    #terrain
    fill(6, 35, 7)
    ellipse(width, height, 3000, 500)
    #pathway
    image(pathway, 475, 320, 200, 300)
    #crops
    #front treeline
    image(tree, -135, 130, 400, 440)
    image(tree_two, -20, 170, 400, 440)
    image(tree, 100, 150, 400, 440)
    image(tree_two, 240, 150, 400, 440)
    #back treeline
    image(tree_two, -60, 120, 300, 310)
    image(tree, 120, 100, 300, 310)
    image(tree, 200, 100, 300, 310)
    #bushes
    image(bush_max, 0, 510, 124, 90)
    image(bush_max, 80, 510, 124, 90)
    image(bush_max, 164, 510, 124, 90)
    image(bush_max, 205, 510, 124, 90)
    image(bush_max, 273, 510, 124, 90)
    image(bush_max, 360, 510, 124, 90)
    #dilapidated house
    image(haunted_house, 500, 25, 380, 380)
    #mysterious moon
    image(crescent_moon, 25, 25, 125, 125)
    #spooky red eyes
    if frameCount % 50 != 0:
        image(red_eyes, 110, 550, 25, 25)
    if frameCount % (60) != 0:
        image(red_eyes, 230, 540, 25, 25)
    #scary lightning
    if frameCount % (60) == 0:
        image(lightning, 500, 25, 500, 500)
