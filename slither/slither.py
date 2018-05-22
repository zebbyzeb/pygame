import pygame
import random
import time
##import os
##os.getcwd() # Log this line.
##pygame.mixer.pre_init(44100, 16, 2, 4096)

pygame.init()       #returns a tuple (6,0) ie. 6 successes and 0 failures.

bite_sound = pygame.mixer.Sound('apple_bite.wav')
pygame.mixer.music.load('jungle_night.wav')
crash_sound = pygame.mixer.Sound('snake_hit.wav')

black = (0,0,0)                 
white = (255,255,255)
red = (255,0,0)
dark_red = (155,0,0)
green = (0,255,0)
light_yellow = (255,255,51)
dark_green = (0,155,0)
blue = (0,0,255)
dark_blue = (0,0,155)

##lead_x = 300    
##lead_y = 300
##lead_x_change = 0
##lead_y_change = 0

display_width = 800
display_height = 600

block_size = 10         #as per LEC-13 (fixing the hardcode)
FPS = 15

gameDisplay = pygame.display.set_mode((display_width,display_height))        
pygame.display.set_caption('Slither')

img = pygame.image.load('snake.png')
appleimg = pygame.image.load('apple.png')

clock = pygame.time.Clock()


direction = 'right'                 #initial direction is set to right.

def snake(block_size,snakelist):    #parameters : block_size and list.
    if direction == 'right':
        head = pygame.transform.rotate(img,270)             #image rotated is then saved in the variable 'head'. 
    if direction == 'left':                                 #our snake sprite is, originally, made in the 'facing-up' direction.
        head = pygame.transform.rotate(img,90)              #so, we specify the degrees for rotation accordingly.
    if direction == 'up':
        head = pygame.transform.rotate(img,0)
    if direction == 'down':
        head = pygame.transform.rotate(img,180)    
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,black,(XnY[0],XnY[1],block_size,block_size))
    
def after_crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect = text_objects('Snake Dies',largeText)
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

##    pygame.display.update()
##
##    time.sleep(2)


def text_objects(msg,font):
    textSurface = font.render(msg,True,black)
    return textSurface, textSurface.get_rect()

def score(count):
    
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("Sinned:"+str(count),True,blue)
    gameDisplay.blit(text,(0,0))


pause = False

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf,TextRect = text_objects('Spit Those Seeds',largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
        
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
##
##        largeText = pygame.font.Font('freesansbold.ttf',75)
##        TextSurf,TextRect = text_objects('Spit Those Seeds',largeText)
##        TextRect.center = ((display_width/2),(display_height/2))
##        gameDisplay.blit(TextSurf,TextRect)

        button('GetUP!',150,450,100,50,light_yellow,green,'unpause')
        button('Quit',550,450,100,50,light_yellow,green,'quit')
        pygame.display.update()

        
def unpause():
    
    global pause
    pause = False
    pygame.mixer.music.unpause()
    
def game_intro():
    
    gameDisplay.fill(white)
    LargeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects('Slitherrrr...',LargeText)
    TextRect.center = ((display_width/2),(display_height/2))

    gameDisplay.blit(TextSurf,TextRect)


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

##        LargeText = pygame.font.Font('freesansbold.ttf',115)
##        TextSurf,TextRect = text_objects('Slitherrrr...',LargeText)
##        TextRect.center = ((display_width/2),(display_height/2))
##
##        gameDisplay.blit(TextSurf,TextRect)

        button("Sin",150,450,100,50,green,dark_green,'play')
        button("Quit",550,450,100,50,blue,dark_blue,'quit')

        pygame.display.update()

        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action = None):

    pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'play':
                game_loop()
            if action == 'quit':
                pygame.quit()
                quit()
            if action == 'unpause':
                unpause()

    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
            
            

def game_loop():

    pygame.mixer.music.play(-1)

    global direction
    global pause
    
    lead_x = 300    
    lead_y = 300
    lead_x_change = 10 #this will make the snake move left as soon as the game starts.(lead_x += lead_x_change)
    lead_y_change = 0

    count = 0
    
    randAppleX = round(random.randrange(0,display_width - block_size)/10)*10   #round function is used here so as to make randAppleX a multiple of 10
    randAppleY = round(random.randrange(0,display_height - block_size)/10)*10  #since lead_x will always be a multiple of 10 due to assignment.

    snakeList = []              #empty list declaration. eg: snakeList[ snakeHead[lead_x,lead_y] , snakeHead[lead_x,lead_y] ]. 
    snakeLength = 1             #these elements are being deleted according to the decision block
                                #  if len(snakeList) > snakeLength:
                                #       del snakeList[0] 
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0               #this statement is added, so that only 1 coordinate of the snake position changes,
                if event.key == pygame.K_RIGHT:     #so as to avoid any diagonal movements.
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change =0
                if event.key == pygame.K_UP:                #up and down movement functionality is added.
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                if event.key == pygame.K_p:
                    pause = True
                    paused()
    ##        if event.type == pygame.KEYUP:
    ##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    ##                lead_x_change = 0
    ##                lead_y_change = 0


        if lead_x > display_width - block_size or lead_x < 0 or lead_y > display_height - block_size or lead_y < 0:       #boundaries added.

            after_crash()
##            pygame.quit()
##            quit()

        
        lead_x += lead_x_change            
        lead_y += lead_y_change    

        gameDisplay.fill(white)
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))

        #pygame.draw.rect(gameDisplay,red,(randAppleX,randAppleY,block_size,block_size))    #the apple : red
##        pygame.draw.rect(gameDisplay,black,(lead_x,lead_y,block_size,block_size))           #the snake : black

    ##    if lead_x_change < 0:
    ##        for event in pygame.event.get():
    ##            if event.type == pygame.KEYDOWN:
    ##                if event.key == pygame.K_RIGHT:
    ##                    pygame.quit()
    ##                    quit()
        #gameDisplay.fill(red,rect=(200,200,50,50))                  #another way of drawing a rectangle in the game window.

        snakeHead = []                                  #empty list declaration. this list contains all the lead_x and lead_y of the 
        snakeHead.append(lead_x)                        #of the snake position. with latest changes in lead_x and lead_y added as last in the list.
        snakeHead.append(lead_y)                        #eg. snakeHead[lead_x, lead_y, lead_x, lead_y].
        snakeList.append(snakeHead)                     #In turn, snakeHead[] list is appended to snakeList[] list.
        if len(snakeList) > snakeLength:
            del snakeList[0] 

        for eachSegment in snakeList[:-1]:              #this solves the problem of the crossover snake and snake moving back on itself.
            if eachSegment == snakeHead:                #refer notes (LEC-21) for detailed explanation.
##                pygame.quit()
##                quit()
                after_crash()            
        snake(block_size,snakeList)
        
##        pygame.display.update()


        if lead_x == randAppleX and lead_y == randAppleY :                                  ##This 'if' statement can be written just above or below
            #print('om nom nom')                                                            ##the pygame.display.update() statement. 
            randAppleX = round(random.randrange(0,display_width - block_size)/10)*10        ##Try and think the logic execution proceedings for both
            randAppleY = round(random.randrange(0,display_height - block_size)/10)*10       ##cases.
            snakeLength += 1
            count += 1
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(bite_sound)

        pygame.mixer.music.unpause()
    
            
        score(count)

        pygame.display.update()
        clock.tick(FPS)

game_intro()
game_loop()
pygame.quit()

quit()

    
            
