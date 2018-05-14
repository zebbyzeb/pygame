import pygame
import time
import random

pygame.init() #to initiate all pygame modules.

crash_sound = pygame.mixer.Sound("Crash.wav")           #sound to be played when the car crashes ie. when the crash() function is called.
                                                        #the 'S' in "pygame.mixer.Sound" has to be in caps. else, error!

pygame.mixer.music.load("background_music.wav")         #background music.


black = (0,0,0)                 #color definitions and respective variable assignments
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
dark_green = (0,155,0)
dark_red = (155,0,0)

display_width = 800             #dimension assignments
display_height = 600


gameDisplay = pygame.display.set_mode((800,600)) #to set the resolution of our game window. This is basically our game window.

pygame.display.set_caption('A Bit Racey') #to set the title bar of the game window.

clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')           #assigning the image's location to the variable carImg.
                                                #make sure, the size of the dimensions of png file is less than the game window dimensions/resolution
                                                #for the image to fit properly.
car_width = 63                                 #pixel width of our image

def car(x,y):                                   
    gameDisplay.blit(carImg,(x,y))              #puts the parameters specified, on the game window. 
                                                #parameters: (image_path,img_coordinates)


def crash():                                    #crash() function definition
    #message_display('You Crashed')              #message_display(text) function is called.


    pygame.mixer.music.stop()       #background music stop.

    pygame.mixer.Sound.play(crash_sound)        #crash music call.
    
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("You Crashed!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again", 150,450,100,50,green,dark_green,"play")            #function call to restart the gameloop all over again. ie. game restarts.
        button("Quit",550,450,100,50,red,dark_red,"quit")

        pygame.display.update()

        clock.tick(15)
        




def message_display(text):                      #message_display(text) function definition
    
    largeText = pygame.font.Font('freesansbold.ttf',115)                         
    TextSurf, TextRect = text_objects(text, largeText)                          #text_objects(text, largeText) function is called
                                                                                #and its return values (which are: textSurface and textSurface.get_rect() )
                                                                                #are assigned to the variables on the right.
                                                                                
    TextRect.center = ((display_width/2),(display_height/2))                    #coordinates of our text rectangle is defined
    gameDisplay.blit(TextSurf,TextRect)                                         #puts the parameters specified, on the game window.

    pygame.display.update()                                                     #if this statement is not written, the game state wont be updated and displayed
                                                                                #and the statements "time.sleep(2) and game_loop()" will be executed procedurely
                                                                                #making the game window pause for 2 seconds and then restarting the game without
                                                                                #displaying the message "You Crashed".
    time.sleep(2)

    game_loop()


def text_objects(text, font):  #the font in here is same as the font in                                                  #text_objects(text,font) function is defined.
                                #font.render(text, True, black)
    textSurface = font.render(text,True,black)                                  #parameters are : text, ie. You Crashed, Anti-Aliasing(for smoothness) boolean, color.
    return textSurface, textSurface.get_rect()                                  #textSurface.get_rect() creates a rectangle around our rendered text for its easy
                                                                                #coordinate positioning. (as done in message_display(text) function, ie.
                                                                                #TextRect.center assignment.


def things(thingx, thingy, thingw, thingh, color):                              #function declaration
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])               


def things_dodged(count):                                                       #function declaration.
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged:"+str(count),True,black)                         
    gameDisplay.blit(text,(0,0))                                                #puts the parameters specified on the screen.
                                                                                #the text can also be engulfed in a rectangle for easy positioning, as in text_objects()
                                                                                #function.
    

def game_intro():                                                               

    intro = True

    while intro:                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                       #this is to ensure that if the user hits the cross button
                pygame.quit()                                                   #on the game window, the game window must close. else, it will become unresponsive.
                quit()

        gameDisplay.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf',25)             #when we encapsulate text in a rectangle, then we must use the .center method 
        TextSurf, TextRect = text_objects('Intro' , largeText)          #to specify its coordinates. else error. OR dont encapsulate the text in a rectangle,
        TextRect.center = ((display_width/2),(display_height/2))        #and specify its coordinates in gameDisplay.blit(text,(0,0)) function. like we 
                                                                        #did in 'things_dodged(count)' function.    
        gameDisplay.blit(TextSurf,TextRect)

        button("Go",150,450,100,50,green,dark_green,"play")             #button(msg,x,y,w,h,ic,ac,action=None) function call.
        button("Quit",550,450,100,50,red,dark_red,"quit")               #these coordinates have been grabbed using pygame.mouse.get_pos().
                                                                        #(see button() function definition.

        
        pygame.display.update()
        clock.tick(15)
        #game_loop() this is the game_loop() function call. after the intro displays for 5 seconds, the game loop will start because of this call.
        #this hasnt been coded as of LECTURE-10.
        

def button(msg,x,y,w,h,ic,ac,action=None):                      #the x,y have nothing to do with the position of the car.
                                                                #we can have parameter representators as any variable.

    pygame.draw.rect(gameDisplay,ic,(x,y,w,h))                  #a rectangle is drawn using the parameters passsed in the button() function call.
    
    mouse = pygame.mouse.get_pos()                              #mouse position coordinates are fetched. mouse coordinates are fetched as a list of two elements.
                                                                #thus the variable 'mouse' here, is a list of two elements. x-coordinate and y-coordinate.

    click = pygame.mouse.get_pressed()                          #similarly, 'click' variable is a list of two elements.
                                                                #click[0] is for left mouse button.
                                                                #click[1] is for right mouse button.
##    smallText = pygame.font.Font("freesansbold.ttf",25)       
##    textSurf,textRect = text_objects(msg,smallText)
##    textRect.center = ((x+(w/2)),(y+(h/2)))
##    gameDisplay.blit(textSurf,textRect)
    

    if x+w > mouse[0] > x and y+h > mouse[1] > y:               #this to check if the mouse pointer is in the rectangle boundary.  
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))              #if true, then a new rectangle is drawn over the existing one(see the fisrt statement is this declaration.
        if click[0]==1 and action != None:                      
            if action == "play":
                game_loop()                                     #game_loop() function call.
            if action == "unpause":
                unpause()               #unpause() function call. this causes the global variable 'pause' to change to False.
            elif action == "quit":
                pygame.quit()
                quit()

    smallText = pygame.font.Font("freesansbold.ttf",25)         #if this text were to be above the if block,
    textSurf,textRect = text_objects(msg,smallText)             #on hovering, the new rectangle wud have formed on the text, making the text disappear on hovering.
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)



pause = False                                                   #global variable declaration.

def paused():                                                   #we can see that this function is in itself a bare minimum gameloop code.

    pygame.mixer.music.pause() #background music pause.

##    largeText = pygame.font.Font('freesansbold.ttf',25)       #this is currently executed in while loop which runs over and over again.
##    TextSurf, TextRect = text_objects('Intro' , largeText)    #ie. the text is being pasted over and over again, causing it to look rough and a lil pixeled.
                                                                #Same story with the buttons and the text in them. Since, they(the button and the text over it) are
                                                                #in  while loop, the button and the text are getting overlapped continuously. hence the roughness.
##    TextRect.center = ((display_width/2),(display_height/2))  #The advantage of executing the text before the while loop is, it wont get pasted over and over
##                                                              #again. Hence the text "Paused" will appear smooth. 
##    gameDisplay.blit(TextSurf,TextRect)

    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)                 #we can remove this statement, so as to keep the blocks and the car not disappear wen the game is paused.(cheat bug)
        largeText = pygame.font.Font('freesansbold.ttf',25) 
        TextSurf, TextRect = text_objects('Paused' , largeText)
        TextRect.center = ((display_width/2),(display_height/2))

        gameDisplay.blit(TextSurf,TextRect)

        button("Continue",150,450,100,50,green,dark_green,"unpause")

        button("Quit",550,450,100,50,red,dark_red,"quit")

        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause                #global variable 'pause' is called.

    pygame.mixer.music.unpause() #background music plays again.
    
    pause = False


def game_loop():                                               
    x = display_width*0.4
    y = display_height*0.6

    x_change = 0                            #variable for keystroke changes
    gameExit = False

    thing_width = 100
    thing_startx = random.randrange(0,display_width)                #this are the block movement parameters.
    thing_starty = -600
    thing_speed = 10
    
    thing_height = 100
    dodged = 0                                      #variable for the score.

                                                    #main game loop starts
    global pause

    pygame.mixer.music.play(-1)         #background music plays indefinitely.
    
    while not gameExit:                             #while true
        for event in pygame.event.get():            #pygame.event.get() grabs all events such as mouse-click, key-stroke etc.
            if event.type == pygame.QUIT:           #pygame.QUIT() means the cross button on the game window is clicked by user.
                pygame.quit()                                   
                quit()                              #quits the game window
            print(event)
            
            if event.type == pygame.KEYDOWN:        #event handling. 
                if event.key == pygame.K_LEFT:      #consult copy to clear any doubts.
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:         #if p is pressed, global variable 'pause' is set to true and the paused() function is called.
                    pause = True                    #which is in itself a bare minimum game loop code. As long as we dont get out of this bare miniimum code,
                    paused()                        #proceeding statements wont execute.

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        
        gameDisplay.fill(white)                     #filling the background. This can be done out of the while loop also, since its just the background color
                                                    #that needs to be there everytime. (lec-9)

        things(thing_startx,thing_starty, thing_width, thing_height, red)             #things() funciton call along with specified parameters.

        thing_starty += thing_speed                             #practically, the block isnt moving. Its y-coordinate is changed everytime
                                                                #the while loop runs. this gives us the illusion of movement. 

        if thing_starty > display_height:                       #this if statement ensures that the block gets a new y-coordinate, once the
                                                                #block has moved past the game window. Also, we need to specify the X coordinate,
                                                                #for the reason being, thing_startx variable becomes a constant as soon as it enters the while loop
                                                                #because it is declared above the while loop (the main game loop).
            thing_starty = 0-thing_height
            thing_startx = random.randrange(0,display_width)

            dodged += 1                                         #if the block traverses out of the window, this means that the car has dodged it ie. no crash.

        if thing_starty + thing_height == y:
            
            if x > thing_startx and x + car_width > thing_startx and x + car_width < thing_startx + thing_width:

                crash()
                

        if y < thing_starty + thing_height:                     #crash sequence with blocks. try to take in account all the cases of block crashing with car.
                                                                #or else the bug will show up.
            print('y-crossover')

##            if x > thing_startx and x < thing_startx + thing_width and x + car_width > thing_startx or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
            print('x-crossover')
            if x < thing_startx and x + car_width < thing_startx + thing_width and x + car_width > thing_startx or x > thing_startx and x < thing_startx + thing_width and x + car_width > thing_startx + thing_width:
                
                crash()
                
        
        car(x,y)                                    #function call


                                                    #after the event handling, the x coordinate is changed by 'x += x_change' . 
                                                    #and the car(x,y) function is called which, in turn, puts the parameters specified, on the game window.
                                                    #then the x-coordinate is checked to whether or not it passes the condition. If not, the game loop exits,
                                                    #to execute pygame.quit() and quit() functions.

        things_dodged(dodged)                       #function call.
        

        if x < 0 or x > display_width - car_width:
            crash()                                 #crash() function is called.
                                                    
        pygame.display.update()                     #game state is updated and new refreshed screen is drawn
        clock.tick(60)                              #fps

                                                #main game loop ends
        

game_intro()
game_loop()                                     #dont forget to call this the main gameloop function. or else, its just another function definition.
pygame.quit()                                   
 
quit()

#xxxx-----------------------------------------xxxx-----------------------xxxxx--------------------------xxxx--------------------------------------xxxx---------------------------------------------xxxx-------------------------------xxxx
