import pygame
import time
import random
                                                        ######pixel coordinates always have to be an int type. ######
pygame.init()

display_width = 800                 
display_height = 600

white = (255,255,255)
black = (0,0,0)
red = (155,0,0)
light_red = (255,0,0)
green = (0,155,0)
light_green = (0,255,0)
blue = (0,0,155)
light_blue = (0,0,255)


tankWidth = 40
tankHeight = 20
turretWidth = 4
wheelWidth = 5
barrier_width = 50
ground_height = 35

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks Roullette')

clock = pygame.time.Clock()
cannon_fire = pygame.mixer.Sound('cannon_fire.wav')
FPS = 15
def game_quit():
    pygame.quit()
    quit()

    
def game_intro():

    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf',115)
    textSurf,textRect = text_objects('Hogi Tank',largeText)
    textRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,textRect)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        

        button("Play",150,450,100,50,green,light_green,'play')
        button("Quit",550,450,100,50,green,light_green,'quit')
        pygame.display.update()


def destroy():


    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect = text_objects('Destroyed',largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again", 150,450,110,50,green,light_green,"play")            
        button("Quit",550,450,100,50,red,light_red,"quit")

        pygame.display.update()

        clock.tick(15)

def martyr():
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf',100)
    textSurf,textRect = text_objects('Martyrdom',largeText)
    textRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again", 150,450,110,50,green,light_green,"play")           
        button("Quit",550,450,100,50,red,light_red,"quit")

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

    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)



def tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x - 29,y - 2),                  #list of tuples.
                       (x - 27,y - 5),                  #Contains the end-coordinates of 
                       (x - 26,y - 8),                  #pygame.draw.line() which is being used as
                       (x - 24,y - 12),                 #the turret of the tank.
                       (x - 22,y - 14),                 #The starting coordinates of the line (turret) being (x,y).
                       (x - 20,y - 15),
                       (x - 18,y - 17),
                       (x - 16,y - 19),
                       (x - 15,y - 21)
                       ]

    pygame.draw.circle(gameDisplay,black,(x,y),int(tankHeight/2))                       #circle for the tank head.
    pygame.draw.rect(gameDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))           #rectangle for tank base.
    
    pygame.draw.line(gameDisplay,black,(x,y),possibleTurrets[turPos],turretWidth)       #tank turret.
    
    pygame.draw.circle(gameDisplay,black,(x - 15,y + 20),wheelWidth)                    #tank wheels.
    pygame.draw.circle(gameDisplay,black,(x - 10,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x - 5,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x + 5,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x + 10,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x + 15,y + 20),wheelWidth)

    return possibleTurrets[turPos]              #this function will return the tuple, depending on the turPos value, whenever tank() function is called.

def enemy_tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x + 29,y - 2),                  #list of tuples.
                       (x + 27,y - 5),                  #Contains the end-coordinates of 
                       (x + 26,y - 8),                  #pygame.draw.line() which is being used as
                       (x + 24,y - 12),                 #the turret of the tank.
                       (x + 22,y - 14),                 #The starting coordinates of the line (turret) being (x,y).
                       (x + 20,y - 15),
                       (x + 18,y - 17),
                       (x + 16,y - 19),
                       (x + 15,y - 21)
                       ]

    pygame.draw.circle(gameDisplay,black,(x,y),int(tankHeight/2))                       #circle for the tank head.
    pygame.draw.rect(gameDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))           #rectangle for tank base.
    
    pygame.draw.line(gameDisplay,black,(x,y),possibleTurrets[turPos],turretWidth)       #tank turret.
    
    pygame.draw.circle(gameDisplay,black,(x - 15,y + 20),wheelWidth)                    #tank wheels.
    pygame.draw.circle(gameDisplay,black,(x - 10,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x - 5,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x + 5,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x + 10,y + 20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x + 15,y + 20),wheelWidth)

    return possibleTurrets[turPos]              #this function will return the tuple, depending on the turPos value, whenever tank() function is called.


   
def barrier(xlocation,randomHeight):
    
    pygame.draw.rect(gameDisplay,black,(xlocation,display_height - randomHeight,barrier_width,randomHeight))



def fireShell(xy,tankX,tankY,turPos,gun_power,xlocation,barrier_width,randomHeight,enemyTankX,enemyTankY):
    pygame.mixer.Sound.play(cannon_fire)
    fire = True
    damage = 0
    startingShell = list(xy)
    print('Fire',xy)

    while fire:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay,red,(startingShell[0],startingShell[1]),5)

        startingShell[0] -= (10 - turPos)*2
        

        startingShell[1] += int(((startingShell[0] - xy[0])*0.009/(gun_power/50))**2 - (turPos + turPos/(12 - turPos)))
        if startingShell[1] > display_height:

            #print('last shell:',startingShell[0],startingShell[1])

            hit_x = int(((startingShell[0]*display_height - ground_height)/startingShell[1]))
            hit_y = int(display_height - ground_height)

            #print('Impact:',hit_x,hit_y)
            if enemyTankX + 15 > hit_x > enemyTankX - 15:
                damage = 25
            explosion(hit_x,hit_y)
            
            fire = False
        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2 :
           # print('last shell:',startingShell[0],startingShell[1])

            hit_x = int(startingShell[0])
            hit_y = int(startingShell[1])

            #print('Impact:',hit_x,hit_y)
            explosion(hit_x,hit_y)
            
            fire = False
            
        pygame.display.update()

        clock.tick(60)
    return damage
    pygame.display.update()
    clock.tick(15)
    

def e_fireShell(xy,tankX,tankY,turPos,gun_power,xlocation,barrier_width,randomHeight,pTankX,pTankY):
    pygame.mixer.Sound.stop(cannon_fire)
    damage = 0
    
    power_found = False
    
    while not power_found:
        #currentPower += 1
        gun_power += 1
        print('GUN_POWER:',gun_power)
        if gun_power >= 100:
            power_found = True

        fire = True
        startingShell = list(xy)
        #print('Fire',xy)
        while fire:                                                                               #correct
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            #pygame.draw.circle(gameDisplay,red,(startingShell[0],startingShell[1]),5)

            startingShell[0] += (10 - turPos)*2
            

            startingShell[1] += int(((startingShell[0] - xy[0])*0.009/(gun_power/50))**2 - (turPos + turPos/(12 - turPos)))
            if startingShell[1] > display_height - ground_height:

                #print('last shell:',startingShell[0],startingShell[1])

                hit_x = int(((startingShell[0]*display_height - ground_height)/startingShell[1]))
                hit_y = int(display_height - ground_height)

                #print('Impact:',hit_x,hit_y)
                #explosion(hit_x,hit_y)
                if pTankX + 15 > hit_x > pTankX - 15:
                    print('critical')
                    damage = 25
                    print('target acquired')
                    print('NOW POWER:',gun_power)
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2 :
                #print('last shell:',startingShell[0],startingShell[1])

                hit_x = int(startingShell[0])
                hit_y = int(startingShell[1])

                #print('Impact:',hit_x,hit_y)
                #explosion(hit_x,hit_y)
                
                fire = False                                                #correct
                
    fire = True
    startingShell = list(xy)
    print('Fire',xy)
    pygame.mixer.Sound.play(cannon_fire)
    while fire:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay,red,(startingShell[0],startingShell[1]),5)

        startingShell[0] += (10 - turPos)*2
        

        startingShell[1] += int(((startingShell[0] - xy[0])*0.009/(gun_power/50))**2 - (turPos + turPos/(12 - turPos)))
        if startingShell[1] > display_height - ground_height:

            print('last shell:',startingShell[0],startingShell[1])

            hit_x = int(((startingShell[0]*display_height - ground_height)/startingShell[1]))
            hit_y = int(display_height - ground_height)

                            
            explosion(hit_x,hit_y)
            
            fire = False
        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2 :
            #print('last shell:',startingShell[0],startingShell[1])

            hit_x = int(startingShell[0])
            hit_y = int(startingShell[1])

            #print('Impact:',hit_x,hit_y)
            
            
            fire = False
            
        pygame.display.update()

        clock.tick(100)
    pygame.mixer.Sound.stop(cannon_fire)
    return damage




def explosion(x,y):

    explode = True
    while explode:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #startPoint = x,y
        colorChoices = [red,blue,light_blue,green,light_green]
        magnitude = 1
        while magnitude < 50:
            exploding_bit_x = x + random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay,colorChoices[random.randrange(0,5)],(exploding_bit_x,exploding_bit_y),random.randrange(1,5))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)
        explode = False
                



def power(level):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect = text_objects('power:'+str(level),smallText)
    textRect.center = (display_width/2,15)
    gameDisplay.blit(textSurf,textRect)

def text_objects(msg,font):
    textSurface = font.render(msg,True,black)
    return textSurface,textSurface.get_rect()


def health_bars(player_health,enemy_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = red
    else:
        player_health_color = blue

    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = red
    else:
        enemy_health_color = blue

    pygame.draw.rect(gameDisplay,player_health_color,(680,25,player_health,25))
    pygame.draw.rect(gameDisplay,enemy_health_color,(20,25,enemy_health,25))
        



def game_loop():

    player_health = 100
    enemy_health = 100
    
    currentTurPos = 0                   
    changeTur = 0
    
    mainTankX = display_width * 0.9
    mainTankY = display_height *0.9
    tankMove = 0

    fire_power = 50
    power_change = 0

    xlocation = (display_width/2) + random.randint(-0.2*display_width,0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)

    enemyTankX = display_width * 0.1
    enemyTankY = display_height *0.9
    
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                if event.key == pygame.K_RIGHT:
                    tankMove = 5
                if event.key == pygame.K_UP:
                    changeTur = 1
                if event.key == pygame.K_DOWN:
                    changeTur = -1
                if event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,barrier_width,randomHeight,enemyTankX,enemyTankY)
##                    print(damage)
                    enemy_health -= damage
                    if enemy_health <=0:
                        
                        destroy()
                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,0,xlocation,barrier_width,randomHeight,mainTankX,mainTankY)
                    player_health -= damage
                if event.key == pygame.K_a:
                    power_change = -1
                if event.key == pygame.K_d:
                    power_change = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    changeTur = 0
                if event.key == pygame.K_a or pygame.K_d:
                    power_change = 0


            if player_health <= 0:
                martyr()
            if enemy_health <=0:
                destroy()
        
        mainTankX += tankMove
        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        if currentTurPos < 0:
            currentTurPos = 0
        if mainTankX - (tankWidth/2) < xlocation + barrier_width:
            mainTankX += 5
        
        fire_power += power_change
        


        gameDisplay.fill(white)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX,enemyTankY,8)

        power(fire_power)
        barrier(xlocation,randomHeight)
        gameDisplay.fill(light_green,rect = (0,display_height - ground_height,display_width,ground_height))

        pygame.display.update()

        clock.tick(FPS)
game_intro()
game_loop()
pygame.quit()
quit()
