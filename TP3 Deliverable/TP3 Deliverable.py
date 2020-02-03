from cmu_112_graphics import *
import tkinter as tk
import random
import math
import string
#the animation framework is from CMU 15-112 course website
class WelcomeMode(Mode):
    def appStarted(mode):
        mode.text1 = '''        You can pick your own course and
        difficulty in this game. The difficulty is also 
        determined by you weight.'''
        mode.clicks = 0
        mode.settingChosen = False
        mode.levelChosen = False
        mode.counter = 0
        mode.colors = ['lightblue']*6
        mode.enteringMass = False
        mode.inputMass = ''
        mode.boxColor = 'white'
        mode.randomStart = False
        #when it turns true, starter starts moving
        starterImage = 'https://static.boredpanda.com/blog/wp-content/uploads/2016/02/cute-baby-polar-bear-day-photography-191__880.jpg'
        mode.starterImage = mode.loadImage(starterImage)
        mode.starterImage = mode.scaleImage(mode.starterImage,1/8)
        mode.starterX,mode.starterY = mode.width//2,80
        mode.dx,mode.dy = 20,30
        #velocity of starter
        #draw a button and a snowflake would start moving across the screen, once 
        #the button gets hit, game starts
    
    def starterMove(mode):
        mode.starterX += mode.dx
        mode.starterY += mode.dy
        if mode.starterX >= mode.width or mode.starterX <= 0:
            mode.dx = -mode.dx
        elif mode.starterY >= mode.height or mode.starterY <= 0:
            mode.dy = -mode.dy

    def mousePressed(mode,event):
        #if clicked within x1,y1,x2,y2,change color
        if mode.width//4-50 < event.x < mode.width//4+50 and 230 < event.y < 300 and mode.settingChosen == False:
            data.setting = 'day'
            mode.clicks += 1
            mode.settingChosen = True
            mode.colors[0] = 'gold'
        elif mode.width//2-50 < event.x < mode.width//2+50 and 230 < event.y < 300 and mode.settingChosen == False:
            data.setting = 'evening'
            mode.clicks += 1
            mode.settingChosen = True
            mode.colors[1] = 'gold'
        elif 3*mode.width//4-50 < event.x < 3*mode.width//4+50 and 230 < event.y < 300 and mode.settingChosen == False:
            data.setting = 'night'
            mode.clicks += 1
            mode.settingChosen = True
            mode.colors[2] = 'gold'
        #can pick setting only once
        elif mode.width//4-50 < event.x < mode.width//4+50 and 370 < event.y < 440 and mode.levelChosen == False:
            data.level = 'begining'
            mode.clicks += 1
            mode.levelChosen = True
            mode.colors[3] = 'gold'
        elif mode.width//2-50 < event.x < mode.width//2+50 and 370 < event.y < 440 and mode.levelChosen == False:
            data.level = 'medium'
            mode.clicks += 1
            mode.levelChosen = True
            mode.colors[4] = 'gold'
        elif 3*mode.width//4-50 < event.x < 3*mode.width//4+50 and 370 < event.y < 440 and mode.levelChosen == False:
            data.level = 'spicy'
            mode.clicks += 1
            mode.levelChosen = True
            mode.colors[5] = 'gold'
        if mode.width//2-75 < event.x < mode.width//2+75 and 520 < event.y < 560:
            mode.enteringMass = True
            mode.boxColor = 'lightblue'
        if mode.width//2+80 < event.x < mode.width//2+120 and 520 < event.y < 560:
            data.mass = int(mode.inputMass)
            mode.enteringMass = False
            mode.randomStart = True
            #after hitting 'Done' button, trigger random starter
    
    def keyPressed(mode,event):
        if mode.enteringMass == True:
            if event.key == 'Delete':
                mode.inputMass = mode.inputMass[:-1]
            else:
                mode.inputMass += event.key
        if event.key == 'ENTER':
            mode.randomStart = True
            #after inputting mass, either press 'Enter' or hit the 'Done' button
        if event.key == 'h':
            mode.app.setActiveMode(mode.app.helpMode)
        if event.key == 's':
            mode.app.setActiveMode(mode.app.gameMode)
        if event.key == 'z':
            mode.mass = random.randint(20,100)
            mode.setting = random.choice(['day','evening','night'])
            data.level = random.choice(['begining','medium','spicy'])
            mode.app.setActiveMode(mode.app.gameMode)
        
    def timerFired(mode):
        if mode.randomStart == True:
            mode.starterMove()
        if mode.width//2-50 <= mode.starterX <= mode.width//2+50 and 590 <= mode.starterY <= 690:
            mode.app.setActiveMode(mode.app.gameMode)
    
    def redrawAll(mode,canvas):
        canvas.create_oval(mode.width//4-50,230,mode.width//4+50,300,
        fill=mode.colors[0])
        canvas.create_oval(mode.width//2-50,230,mode.width//2+50,300,
        fill=mode.colors[1])
        canvas.create_oval(3*mode.width//4-50,230,3*mode.width//4+50,300,
        fill=mode.colors[2])
        canvas.create_oval(mode.width//4-50,370,mode.width//4+50,440,
        fill=mode.colors[3])
        canvas.create_oval(mode.width//2-50,370,mode.width//2+50,440,
        fill=mode.colors[4])
        canvas.create_oval(3*mode.width//4-50,370,3*mode.width//4+50,440,
        fill=mode.colors[5])
        canvas.create_text(mode.width//2,mode.height/10,text='Welcome to Phyco-skiing!',
        font = 'Helvetica 24 bold',fill='gold')
        canvas.create_text(mode.width//2,mode.height/7,text=mode.text1,
        font = 'Helvetica 18 bold',fill='lightblue',anchor='n')
        canvas.create_text(mode.width//2,mode.height/4 + 15,
        text='Pick your course here',font = 'Helvetica 18 bold',fill='black',
        anchor='n')
        canvas.create_text(mode.width//4,265,text='Day',
        font='Helvetica 18 bold')
        canvas.create_text(mode.width//2,265,text='Evening',
        font='Helvetica 18 bold')
        canvas.create_text(3*mode.width//4,265,text='Night',
        font='Helvetica 18 bold')
        canvas.create_text(mode.width//2,350,text='Pick your diffculty level',
        font = 'Helvetica 18 bold')
        canvas.create_text(mode.width//4,405,text='Beginning',
        font='Helvetica 18 bold')
        canvas.create_text(mode.width//2,405,text='Medium',
        font='Helvetica 18 bold')
        canvas.create_text(3*mode.width//4,405,text='Spicy',
        font='Helvetica 18 bold')
        canvas.create_text(mode.width//2,480,text='Enter your mass (kg)',
        font='Helvetica 18 bold')
        canvas.create_rectangle(mode.width//2-75,520,mode.width//2+75,560,
        fill=mode.boxColor)
        canvas.create_text(mode.width//2-30,540,text=mode.inputMass)
        canvas.create_rectangle(mode.width//2+80,520,mode.width//2+120,560,
        fill='khaki')
        canvas.create_text(mode.width//2+100,540,text='Done',
        font='Helvetica 14 bold')
        canvas.create_text(mode.width//2+250,530,
        text='''
        Please press the Done button
        after you have put in mass''',
        font='Helvetica 16 bold',fill='lightblue')
        #press done after putting in mass
        canvas.create_oval(mode.width//2-50,590,mode.width//2+50,690,
        fill='Gold')
        canvas.create_text(mode.width//2,640,text='START',
        font='Helvetica 20 bold')
        if mode.randomStart == True:
            cx,cy = mode.starterX, mode.starterY
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(mode.starterImage))
        canvas.create_text(mode.width//5,90,text='Press h to see instructions',
        font='Hevletica 16 bold')
        canvas.create_text(mode.width//5,120,
        text='''
        After selecting settings, press s to start right away
        (or wait until the bear hits the start button)''',
        font='Helvetica 16 bold')
        canvas.create_text(mode.width//5,175,
        text='Press z to quick start with a random setting',
        font='Helvetica 16 bold')
        

class HelpMode(Mode):
    def appStarted(mode):
        aichenImage = 'ME.jpeg'
        mode.aichenImage = mode.loadImage(aichenImage)
        mode.aichenImage = mode.scaleImage(mode.aichenImage,0.3)
        snowmanImage = 'snowman.jpg'
        mode.snowmanImage = mode.loadImage(snowmanImage)
        mode.textCounter = 0
        mode.text1 = '''Do you realize it's December, officially winter time now!'''
        mode.text2 = '''I know, I know. I have hot chocolate ready.'''
        mode.text3 = '''Ummm... and what else?'''
        mode.text4 = '''
        Actually, also term project. In fact, my term project has to do with 
        snow. It's called Phyco-skiing.
        '''
        mode.text5 = '''Phyco, not Psycho, right?'''
        mode.text6 = '''
        Well, I hope not. The goal of phyco-skiing is to finish
        the course as fast as possible. Before starting, players can choose the 
        setting (day,evening,night background), difficulty level, as well as 
        inputting their mass which will influence the game.
        '''
        mode.text7 = '''
        There are so many skiing games, what's special about yours?
        '''
        mode.text8 = '''
        In Phyco-skiing, all motions are physics-simulated. The player
        is always influenced by gravity, friction (determined by the chosen 
        difficulty level), and the shape of the curve it is on.
        '''
        mode.text9 = '''Interesting, tell me more.'''
        mode.text10 = '''
        One of the hardest part of the game comes from the steep uphills. 
        When the velocity is not high enough to get over the hill, player will start
        moving to the opposite direction due to gravity. And the steeper the hill
        is, the harder it is to make, which will cost more time. Also, during 
        the game, there would be bears appearing onto the curve. If collided, 
        they will drag people down from an uphill. They can also
        help you speed up if the collision happens on a downhill. After dragging 
        for a certain time, the bear will free fall off the screen.
        '''
        mode.text11 = 'Oh no, that sounds hella hard!'
        mode.text12 = '''
        Don't worry. There are things to help! Most easily, you can press
        the right arrow to speed up for a certain number of times. When you have used
        all the accelerators(that's what these are called), you will be noticed.
        There would also be skateboards falling off the screen, you have to drag 
        them to the player. Once you are on it, you would not run into any new bears
        and will move super fast for a certain period of time. After board time is up,
        the board will free fall off the screen, and there will be another one coming
        up soon.
        '''
        mode.text13 = '''
        Great, that made me feel better. Are there any other things I 
        should know?
        '''
        mode.text14 = '''
        You can press 'p' to pause during the game. It won't stop the timer,
        but you might want to do that so the board could be dragged to the player
        more easily. Your current time, velocity are printed on the upperleft corner.
        You can hit 'j' to jump. Jump is also influenced by gravity and the curve
        you are on. When you finished, you would see a really cute image in the 
        middle followed by a win screen. If unfortunately you didn't finish on 
        time, an end screen will appear. In either case, you can check history,
        which keeps track of your PR and press 'k' to restart.
        '''
        mode.texts = [mode.text1,mode.text2,mode.text3,mode.text4,mode.text5,
        mode.text6,mode.text7,mode.text8,mode.text9,mode.text10,mode.text11,
        mode.text12,mode.text13,mode.text14]
    
        speakerImageLeft = 'speaker.jpeg'
        mode.speakerImageLeft = mode.loadImage(speakerImageLeft)
        mode.speakerImageLeft = mode.scaleImage(mode.speakerImageLeft,0.3)
        speakerImageRight = 'speakerRR.jpeg'
        mode.speakerImageRight = mode.loadImage(speakerImageRight)
        mode.speakerImageRight = mode.scaleImage(mode.speakerImageRight,0.3)

    def keyPressed(mode,event):
        if event.key == 'Right':
            mode.textCounter += 1
        elif event.key == 'Left':
            mode.textCounter -= 1
        elif event.key == 's':
            mode.app.setActiveMode(mode.app.welcomeMode)
            #press the right arrow or enter to go onward
            #the speaking person will have a different image
    
    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/8,550,image=ImageTk.PhotoImage(mode.aichenImage))
        canvas.create_image(7*mode.width/8,550,image=ImageTk.PhotoImage(mode.snowmanImage))
        if mode.textCounter >= 14:
            canvas.create_text(mode.width//2,mode.height//2,text='press s to start',
            font = 'Helvetica 18 bold')
        else:
            if mode.textCounter % 2 == 0: #snowman
                canvas.create_text(2*mode.width//3,mode.height//3,text=mode.texts[mode.textCounter]
                ,font = 'Helvetica 18 bold')
                canvas.create_image(7*mode.width/8-100,380,image=ImageTk.PhotoImage(mode.speakerImageRight))
            else:
                canvas.create_text(mode.width//3,mode.height//3,text=mode.texts[mode.textCounter]
                ,font = 'Helvetica 18 bold')
                canvas.create_image(mode.width/8+130,350,image=ImageTk.PhotoImage(mode.speakerImageLeft))
        canvas.create_text(mode.width//2,mode.height//7,
        text='Press the right arrow to move along the conversation',
        font = 'Helvetica 18 bold',fill='lightblue')

class GameMode(Mode):
    def appStarted(mode):
        data.counter = 0
        mode.i = 0
        mode.curveList = []
        mode.x_increment = 1
        #x gets incremented by 1 each time
        mode.x_factor = 0.03
        # height stretch
        mode.y_amplitude = 180
        mode.center = mode.height//2
        for x in range(120):
            mode.curveList.append((x * mode.x_increment,
            int((x * mode.x_factor) * mode.y_amplitude)*0.6 + 20))
        
        for x in range(120,180):
            mode.curveList.append((x * mode.x_increment,
            int(math.cos(x * mode.x_factor + 140) * mode.y_amplitude)
            * 0.3 + mode.center + 26))
        
        for x in range(180,350):
            mode.curveList.append((x * mode.x_increment,
            int(math.sin(x * mode.x_factor + 210) * mode.y_amplitude)
            * 0.7 + mode.center - 63))
        
        for x in range(350,420):
            mode.curveList.append((x * mode.x_increment,
            int(math.sin(x * mode.x_factor + 160) * mode.y_amplitude)
            * 0.3 + mode.center - 38))
        
        for x in range(420,580):
            mode.curveList.append((x * mode.x_increment,
            int(math.cos(x * mode.x_factor + 110) * mode.y_amplitude) 
            * 0.5 + mode.center + 55))

        for x in range(580,790):
            mode.curveList.append((x * mode.x_increment,
            int(math.cos(x * mode.x_factor + 110) * mode.y_amplitude)
            * 0.3 + mode.center + 51))
       
        for x in range(790,1300):
            mode.curveList.append((x * mode.x_increment,393))
    
        mode.Player = Player(mode)
        mode.dt = 1
        mode.distanceLeft = mode.width
        mode.distanceBar = 0 
        #length of the distance bar, growing as player moves forward 

        mode.bearOut = 10 #frequency a new bear appears
        mode.frictionC = 0
        
        bearImage = 'Polar_Bear_-_Alaska_(cropped).png'
        mode.bearImage = mode.loadImage(bearImage)
        monsterBearImage = 'monster bear.png'
        mode.monsterBearImage = mode.loadImage(monsterBearImage)
        cubBearImage = 'cubBear.png'
        mode.cubBearImage = mode.loadImage(cubBearImage)
        
        mode.velocitySet = False
        mode.dragCounter = 0
        mode.dragging = False
    
        nightbackgroundurl = 'snowing_night.jpeg'
        mode.nightbackground = mode.loadImage(nightbackgroundurl)
        mode.nightbackground = mode.scaleImage(mode.nightbackground,2.5)
        eveningbackgroundurl = 'snowing evening.jpg'
        mode.eveningbackground = mode.loadImage(eveningbackgroundurl)
        mode.eveningbackground = mode.scaleImage(mode.eveningbackground,2.8)
        daybackgroundurl = 'snowing day.jpeg'
        mode.daybackground = mode.loadImage(daybackgroundurl)
        mode.daybackground = mode.scaleImage(mode.daybackground,2.2)

        bearHugUrl = 'https://image.shutterstock.com/image-vector/bear-vector-polar-logo-icon-260nw-1095791282.jpg'
        mode.bearHugImage = mode.loadImage(bearHugUrl)
        mode.bearHugImage = mode.scaleImage(mode.bearHugImage,0.75)
        mode.sprites = [ ]
        for i in range(4):
            sprite = mode.bearHugImage.crop((90*i, 0, 90*(i+1), 150))
            mode.sprites.append(sprite)
        mode.spriteCounter = 0
        
        mode.accelerators = 3
        mode.error = False
        mode.jumpers = 3
        mode.error1 = False
        winHugImage = 'winning hug.jpeg'
        mode.winHugImage = mode.loadImage(winHugImage)
        mode.winCounter = 0
        mode.win = False
        mode.freeze = False
        mode.freezers = 6
        #can use the freezer three times

        boardImage = 'board.jpg'
        mode.boardImage = mode.loadImage(boardImage)
        mode.boardImage = mode.scaleImage(mode.boardImage,0.1)
        mode.boardX,mode.boardY = mode.width//2,80
        mode.boardMass = 50 #3kg
        mode.onDrag = False
        mode.onBoard = False
        mode.boardCounter =  0
        mode.dy = 0
        mode.i = 0
        #there would be only one board on the course at one time
        #after getting on the board, player changes to another color and gets larger

    def boardFreeFall(mode):
        mode.dy += 9.8
        mode.boardY += mode.dy
        mode.boardX = mode.boardX

    def getAcceleration(mode):
        #dt is constant (0.1s), the distance moved will be different
        #mode.Player.theta is the tangent angle of the previous section
        #I am using acceleration and the consequent velocity from that section 
        #to project the distance it would move within the next time interval.
        #And that is represented by newV
        if mode.Player.x1 == mode.Player.x0:
            mode.Player.x1 = mode.Player.x1 + 1
        mode.Player.theta = math.atan((mode.Player.y1 - mode.Player.y0)/
        (mode.Player.x1 - mode.Player.x0))
        a = 9.8 * math.sin(mode.Player.theta)
        mode.Player.velocity += a * mode.dt
        mode.move()
    
    def move(mode):
        #x1,y1 are the current location of the ball, x0,y0 are what it is at the
        #end of the last time interval
        #take newV as the input, this is the velocity the ball should be moved
        #during the next time interval
        mode.Player.x0 = mode.Player.x1 
        mode.Player.y0 = mode.Player.y1
        #the old x1 and y1 become the new x0 and y0
        mode.Player.x1 = (mode.Player.x0 
        + mode.Player.velocity * math.cos(mode.Player.theta))
        if int(mode.Player.x1) == int(mode.Player.x0):
            (mode.Player.x1) = (mode.Player.x0) + 3
        #if x1 and x0 are so close together that their integers equal, in which
        #case will cause a divison by zero error, move x1 three points forward to
        #avoid that (four points on the curve should be trivial enough)
        if mode.Player.x1 < 1000:
            mode.Player.x1 = mode.curveList[int(mode.Player.x1)][0]
            mode.Player.y1 = mode.curveList[mode.Player.x1][1]
        mode.distanceBar = (int(mode.Player.x1)/1000) * 80
        #convert the absolute coordinate to a point in the curveList
    
    def moveOnBoard(mode):
        mode.i = mode.Player.x1 + 30
        if mode.i >= 1000:
            mode.i = 999
        mode.Player.x1 = mode.curveList[int(mode.i)][0]
        mode.Player.y1 = mode.curveList[int(mode.i)][1]
        mode.distanceBar = (int(mode.Player.x1)/1000) * 80
        #when player is on board, adopt a different method of moving

    def hitBearMove(mode,bear):
        #this function is to create the effect that the bear will be thrown 
        #away if hit by a board, some parts are not physics simulated
        #take in the bear (mass,position,etc)
        newV = mode.dy * mode.boardMass / (mode.boardMass + bear.mass)
        #the initial velocity of the bear after being hit
        #assuming the board and bear will stick together for a brief period
        indexNum = int(bear.x)
        #get the slope where the bear is
        if indexNum <= 10:
            indexNum = 9
        elif indexNum >= 990:
            indexNum = 989
        #avoid indexing error
        x1,x2 = mode.curveList[indexNum-10][0],mode.curveList[indexNum+10][0]
        y1,y2 = mode.curveList[indexNum-10][1],mode.curveList[indexNum+10][1]
        theta = math.atan(y2-y1)/(x2-x1)
        newVx = newV * math.cos(theta)
        newVy = random.randint(-50,-40)
        newVy += 9.8
        bear.x += newVx
        bear.y += newVy

    def timerFired(mode):
        if data.level == 'beginning':
            mode.frictionC = 0.15
            mode.bearOut = 10 #appear every one second
        elif data.level == 'medium':
            mode.frictionC = 0.2
            mode.bearOut = 8
        elif data.level == 'spicy':
            mode.bearOut = 6
            mode.frictionC = 0.25
        mode.spriteCounter = (1+mode.spriteCounter) % len(mode.sprites)
        mode.distanceLeft = mode.width - mode.Player.x1
        if mode.Player.x1 >= 1000:
            if data.counter < data.pr:
                data.pr = data.counter
            mode.win = True
            mode.winCounter += 1
            if mode.winCounter >= 15:
                mode.app.setActiveMode(mode.app.winMode)

        if data.counter >= 150:
            mode.app.setActiveMode(mode.app.endMode)
        if not mode.win:
            data.counter += 1
        if mode.Player.jumping == True:
            if not mode.Player.jumpUp:
                mode.Player.jump()
                mode.Player.jumpUp = True
            #only jump upward once
            #check if the player is still above the curve
            if mode.Player.x1 >= 1000:
                mode.Player.x1 = 999
            if mode.Player.y1 < mode.curveList[int(mode.Player.x1)][1]:
                mode.Player.freeFall()
            elif mode.Player.y1 >= mode.curveList[int(mode.Player.x1)][1]:
                mode.Player.y1 = mode.curveList[int(mode.Player.x1)][1]
                mode.Player.jumping = False
                mode.Player.jumpUp = False
        
        if data.counter % 1 == 0 and mode.Player.isPaused == False and mode.Player.jumping == False and mode.onBoard == False:
            mode.getAcceleration()
        if data.counter % mode.bearOut == 0:
            Bears.addToBears()
        for bear in Bears.bears:
            if bear.image == 2:
                bear.freeFall()
            indexNum = int(bear.x)
            if indexNum >= 1000:
                indexNum = 999
            matchY = mode.curveList[indexNum][1]
            while bear.y < matchY:
                bear.freeFall()  #always fall on the curve
        for bear in Bears.bears:
            distance = mode.Player.distance(bear.x,bear.y)
            #the ball and bear is close enough
            #can only be dragged by one bear each time
            #before dragging starts
            if (distance < mode.Player.r + 30 and bear.image == 0 and mode.dragging == False and not mode.onBoard):
                #bears cannot drag the player when he is on board
                mode.dragging = True
                bear.image = 1
                #only regular bears can drag
            if mode.dragging == True and bear.image == 1:
                if mode.velocitySet == False:
                    #momentum during collision will change the speed, but only once
                    mode.Player.velocity = bear.drag(mode.Player.mass,mode.Player.velocity)
                    mode.velocitySet = True
                mode.dragCounter += 1
                bear.x,bear.y = mode.Player.x1,mode.Player.y1
                #during dragging, the bear moves along with the player
                if mode.dragCounter >= 10:
                    mode.dragging = False
                    mode.velocitySet = False
                    mode.dragCounter = 0
                    bear.image = 2
        
        if mode.Player.x1 - 40 <= mode.boardX <= mode.Player.x1 + 40 and mode.Player.y1 - 40 <= mode.boardY <= mode.Player.y1 + 40:
            mode.onBoard = True
            mode.onDrag = False
            mode.Player.isPaused = False
            #don't drag anymore
        if mode.onBoard:
            mode.Player.r = 35
            mode.Player.color = 'green'
            if data.counter % 1 == 0:
                mode.moveOnBoard()
            mode.boardCounter += 1
            mode.boardX,mode.boardY = mode.Player.x1,mode.Player.y1
            if mode.boardCounter >= 10:
                # can stay on board for one second
                mode.boardCounter = 0
                mode.onBoard = False
                mode.Player.r = 20
                mode.Player.color = 'gold'
                mode.boardFreeFall()
                if mode.boardY - 40 > mode.width:
                    mode.boardX,mode.boardY = random.randint(1/4*mode.width,3/4*mode.width),random.randint(0,200)
        if not mode.onBoard and not mode.freeze:
            mode.boardFreeFall()
            if mode.boardY - 40 > mode.width:
                mode.boardX,mode.boardY = random.randint(0,mode.width),random.randint(0,400)
                mode.dy = 0
            #getting rid of the old board by changing the position
            #let board free fall after counter is up
            #when it moves off the screen, add a new one
        
        for bear in Bears.bears:
            if mode.boardX - 30 <= bear.x <= mode.boardX + 30 and mode.boardY - 30 <= bear.y <= mode.boardY + 30:
                bear.hit = True
                bear.image = 2
            if bear.hit == True:
                mode.hitBearMove(bear)

    def mousePressed(mode,event):
        for bear in Bears.bears:
            if abs(event.x - bear.x) <= 20 and abs(event.y - bear.y) <= 20:
                bear.image = 2
        if mode.boardX - 30 <= event.x <= mode.boardX + 30 and mode.boardY - 30 <= event.y <= mode.boardY + 30:
            mode.onDrag = True
        if 800 < event.x < 880 and 100 < event.y < 180:
            mode.freezers -= 1
            mode.freeze = not mode.freeze
    
    def mouseDragged(mode,event):
        if mode.onDrag == True:
            mode.boardX,mode.boardY = event.x, event.y

    def keyPressed(mode,event):
        if event.key == 'p':
            mode.Player.isPaused = not mode.Player.isPaused
        elif event.key == 'Up':
            if mode.accelerators > 0:
                mode.accelerators -= 1
                mode.Player.velocity += 3
            elif mode.accelerators <= 0:
                mode.error = True
        elif event.key == 'j':
            if mode.jumpers > 0:
                mode.Player.jumping = True
                mode.jumpers -= 1
            elif mode.jumpers <= 0:
                mode.error1 = True
        elif event.key == 'Right':
            mode.boardX += 10
        elif event.key == 'Left':
            mode.boardX -= 10


    def redrawAll(mode,canvas):
        canvas.create_image(mode.width//2,mode.height//2,image=ImageTk.PhotoImage(mode.bearHugImage))
        if data.setting == 'night':
            canvas.create_image(mode.width//2,mode.height//2,image=ImageTk.PhotoImage(mode.nightbackground))
        elif data.setting == 'day':
            canvas.create_image(mode.width//2,mode.height//2,image=ImageTk.PhotoImage(mode.daybackground))
        elif data.setting == 'evening':
            canvas.create_image(mode.width//2,mode.height//2,image=ImageTk.PhotoImage(mode.eveningbackground))
        if mode.freezers > 0:
            if not mode.freeze:
                canvas.create_oval(800,100,880,180,fill='gold')
            else:
                canvas.create_oval(800,100,880,180,fill='maroon')
            canvas.create_text(840,140,text='FREEZE',font='Helvetica 15 bold')
        canvas.create_text(80,20,text='Distance Left:',font='Helvetica 16 bold')
        canvas.create_rectangle(150,10,225,30,fill='white') #an empty bar
        canvas.create_rectangle(150,10,145+mode.distanceBar,30,fill='maroon')
        canvas.create_text(80,60,text='Current Velocity:',
        font='Helvetica 16 bold')
        canvas.create_text(220,60,text=f'{mode.Player.velocity}',
        font='Helvetica 16 bold')
        canvas.create_text(90,40,text='Time Elapsed(0.1s):',
        font='Helvetica 16 bold')
        canvas.create_text(180,40,text=f'{data.counter}',
        font='Helvetica 16 bold')
        canvas.create_line(mode.curveList,fill='lightblue',width=5)
        #here is the velocity vector
        mode.Player.draw(canvas)
        canvas.create_line(mode.Player.x1, mode.Player.y1, 
        mode.Player.x1 + mode.Player.velocity + math.cos(mode.Player.theta),
        mode.Player.y1 + mode.Player.velocity + math.sin(mode.Player.theta),
        width=3)
        for bear in Bears.bears: #initialized
            cx,cy = bear.x,bear.y
            #scaleFactor = (bear.mass/100) * (1/20)
            if bear.image == 0:
                scaleFactor = (bear.mass/100) * (1/15)
                image = mode.scaleImage(mode.bearImage,scaleFactor)
                canvas.create_image(cx,cy,image=ImageTk.PhotoImage(image))
            elif bear.image == 1:
                scaleFactor = (bear.mass/100) * (1/15)
                image = mode.scaleImage(mode.monsterBearImage,scaleFactor)
                canvas.create_image(cx,cy,image=ImageTk.PhotoImage(image))
            elif bear.image == 2:
                scaleFactor = (bear.mass/100) * (1/10)
                image = mode.scaleImage(mode.cubBearImage,scaleFactor)
                canvas.create_image(cx,cy,image=ImageTk.PhotoImage(image))
        sprite = mode.sprites[mode.spriteCounter]
        canvas.create_image(1050,393,image=ImageTk.PhotoImage(sprite))
        if mode.win == True:
            canvas.create_image(mode.width//2,mode.height//2,image=ImageTk.PhotoImage(mode.winHugImage))
        if mode.error == True:
            canvas.create_text(mode.width//2,80,text='No more accelerators left',
            font = 'Helvetica 24 bold',fill='red')
        if mode.error1 == True:
            canvas.create_text(mode.width//2,130,text='No more jumpers left',
            font = 'Helvetica 24 bold',fill='red')
        canvas.create_image(mode.boardX,mode.boardY,image=ImageTk.PhotoImage(mode.boardImage))
        
class Player(object):
    def __init__(self,app):
        self.x0 = 0
        self.y0 = 0
        self.x1 = 10
        self.y1 = 10
        self.theta = 0
        self.Vx = 0
        self.Vy = 0
        #these might be changed later
        #not sure about the start state
        self.r = 20
        self.color = 'gold'
        self.dragged = False
        self.mass = int(data.mass)#depending on user input
        self.velocity = 5
        self.isPaused = False
        self.jumping = False
        self.jumpUp = False

    def distance(self,x,y):
        return ((self.x1-x)**2 + (self.y1-y)**2)**0.5
    
    def freeFall(self):
        #the jump's angle and initial velocity depend on the curve the player
        #is on
        #dt = 0.1 #this function is called every 0.1 second
        dVy = 9.8 #pure gravity
        self.Vy = self.velocity * math.cos(self.theta)
        self.Vx = self.velocity * math.sin(self.theta)
        self.y1 += self.Vy + 0.5 * dVy ** 2
        self.x1 += self.Vx
        self.Vy += dVy

    def jump(self):
        self.y1 -= 70 * math.sin(self.theta)
        #70 is the maximum height the player can jump on a horizontal surface
        self.x1 = self.x1

    def draw(self,canvas):
        cx,cy = self.x1,self.y1
        r = self.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=self.color)

class Bears(object):
    bears = set()
    @staticmethod
    def addToBears():
        newBear = Bears(random.randint(0,1000),random.randint(200,400),
            random.randint(100,300),0,False)
        #create a new instance of the Bears class
        #0 is a symbol for the regular bear image
        #all bears start with the regular image
        #if collided, turn to monster bear (image=1)
        #if clicked, turn to cub bear(image=2)
        Bears.bears.add((newBear))
    
    def drag(self,mass,oldV):
        newV = (mass * oldV)/(self.mass+mass)
        return newV
    
    def freeFall(self):
        #all bears should be in free fall if higher than the curve
        self.x = self.x
        dt = 0.1 #this function is called every 0.1 second
        dVy = 9.8 #pure gravity
        self.y += self.Vy + 0.5 * dVy * 0.1 ** 2
        self.Vy += dVy * 0.1
        
    def __init__(self,x,y,mass,image,hit):
        self.x = x
        self.y = y
        self.mass = mass
        self.image = image
        self.Vy = 0
        self.hit = hit
        #(x,y,mass,image) are the four attributes of bears
    def __eq__(self,other):
        return (isinstance(other,Bears) and self.x == other.x and 
        self.y == other.y and self.mass == other.mass and 
        self.image == other.image)
    def __hash__(self):
        return hash((self.x,self.y))
    def draw(self,canvas,bearImage):
        cx,cy = bear.x,bear.y
        canvas.create_image(cx,cy,image=ImageTk.PhotoImage(bearImage))

class WinMode(Mode):
    def appStarted(mode):
        mode.Player = Player(mode)
    
    def keyPressed(mode,event):
        if event.key == 'k':
            mode.app.setActiveMode(mode.app.gameMode)
            mode.app.gameMode.appStarted()
            Bears.bears = set()

    def mousePressed(mode,event):
        if (mode.width//2 - 40 <= event.x <= mode.width//2 + 40 and 
        3*mode.height//4 - 40 <= event.y <= 3*mode.height//4 + 40):
            mode.app.setActiveMode(mode.app.recordMode)
            mode.app.recordMode.appStarted()
    
    def redrawAll(mode,canvas):
        time = data.counter / 10
        canvas.create_text(mode.width//2,mode.height//2,
        text=f'Congrats! Your time is {time} seconds.',font ='Helvetica 16 bold')
        canvas.create_text(mode.width//2,3*mode.height//4,
        text="Click here to check history",font ='Helvetica 16 bold')
        canvas.create_text(mode.width//2,4*mode.height//5,
        text="Press 'k' to restart",font ='Helvetica 16 bold')

class EndMode(Mode):
    def appStarted(mode):
        mode.Player = Player(mode)
    
    def keyPressed(mode,event):
        if event.key == 'k':
            mode.app.setActiveMode(mode.app.gameMode)
            mode.app.gameMode.appStarted()
            Bears.bears = set()
    
    def mousePressed(mode,event):
        if (mode.width//2 - 40 <= event.x <= mode.width//2 + 40 and 
        3*mode.height//4 - 40 <= event.y <= 3*mode.height//4 + 40):
            mode.app.setActiveMode(mode.app.recordMode)
            mode.app.recordMode.appStarted()

    def redrawAll(mode,canvas):
        canvas.create_text(mode.width//2,mode.height//2,text='Game Over',
        font = 'Helvetica 26 bold',fill='red')
        canvas.create_text(mode.width//2,3*mode.height//4,
        text="Click here to check history",font='Helvetica 18 bold',fill='black')
        canvas.create_text(mode.width//2,4*mode.height//5,
        text="Press 'k' to restart",font='Helvetica 18 bold',fill='black')

class RecordMode(Mode):
    def appStarted(mode):
        mode.time = data.pr
        mode.time = mode.time/10
    
    def keyPressed(mode,event):
        if event.key == 'k':
            mode.app.setActiveMode(mode.app.gameMode)
            mode.app.gameMode.appStarted()
            Bears.bears = set()

    def redrawAll(mode,canvas):
        canvas.create_text(mode.width//2,mode.height//2,
        text='Your PR is ' f'{mode.time}' ' seconds',font='Helvetica 20 bold')
        canvas.create_text(mode.width//2,mode.height//2 + 100,
        text='Press k to restart',font='Helvetica 18 bold')

class Data(object):
    def __init__(self):
        self.counter = 0
        self.setting = 'evening'
        self.level = None
        self.pr = 200
        self.mass = 0
data = Data()

class MyModalApp(ModalApp):
    def appStarted(app):
        app.gameMode = GameMode()
        app.welcomeMode = WelcomeMode()
        app.helpMode = HelpMode()
        app.endMode = EndMode()
        app.winMode = WinMode()
        app.recordMode = RecordMode()
        app.setActiveMode(app.welcomeMode)

def runPlayer():
    MyModalApp(width = 1400, height = 700)

runPlayer()
