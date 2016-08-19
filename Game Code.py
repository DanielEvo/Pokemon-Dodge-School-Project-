import pygame
import time
import random

pygame.init()

display_width = 900
display_height = 600

black = (0,0,0)                                                             #cores baseadas em RGB
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))       #define comprimento e altura da tela
pygame.display.set_caption('Speed Blocks')                                  #troca o nome do documento
clock = pygame.time.Clock()                                                 #define Clock para o jogo

carImg = pygame.image.load('Car_top_view.png')
car_width = 78                                                              #largura em pixels

def car(x,y):
    gameDisplay.blit(carImg,(x,y))                                          #troca a imagem de uma superfícia à outra

def score_count(count):
    font = pygame.font.Font(None, 25)
    text = font.render("Dodges: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingX, thingY, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])

def text_objects(text,font):
    textSurface = font.render(text,True,red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',110) 
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)                                                           #tempo em segundos

    game_loop()
       
def crash():
    message_display('YOU CRASHED')

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Speed Blocks", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.7)                                              #há um problem no dimensionamento de imagem e corrigi diminuindo a localização do carro em y

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    score = 0
    
    gameExit = False                                 

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                elif event.key == pygame.K_RIGHT:
                    x_change = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x = x + x_change
       
        #print(event)                                                           #imprime cada evento ocorrido em uma tela separada
        gameDisplay.fill(white)

        #things(thingX, thingY, thingW, thingH, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty = thing_starty + thing_speed
        car(x,y)
        score_count(score)
        
        if x > display_width - car_width or x < 0:                              #fazendo as "bordas" do jogo
            crash()

        if thing_starty > display_height:                                       #calculando batida de carro em bloco
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            score += 1
        
        if y < thing_starty+thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        if score > 10 and score < 20 and thing_speed < 15 :                     #lógica de velocidade dos blocos
            thing_speed += 0.25  
        elif score > 30 and score < 40 and thing_speed < 15 :
            thing_speed += 0.25
        else:
            thing_speed = thing_speed
            
        pygame.display.update()                                                 #ou pygame.display.flip()
        clock.tick(60)

#game_intro()
game_loop()
