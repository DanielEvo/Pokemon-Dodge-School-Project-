import pygame
import time
import random
from ClassSpriteSheet import SpriteSheet


'''inicia Python, define tamanho da tela, define nome da tela e seta clock'''
pygame.init()
display_w = 900
display_h = 600
gameDisplay = pygame.display.set_mode((display_w,display_h))       
pygame.display.set_caption('Pokemon Dodge')                        
clock = pygame.time.Clock()                                        
'''cores baseadas em RGB'''
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
'''seta listas'''
pikalist=[]
diglist=[]
'''carregando imagem de diglet'''
def diglet(thing_startx,thing_starty):
    diglet = pygame.image.load('Diglet_Appear.png')
    gameDisplay.blit(diglet,(thing_startx, thing_starty))


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
    TextRect.center = ((display_w/2),(display_h/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)                                                           #tempo em segundos

    game_loop()

def crash():
    message_display('YOU CRASHED')

def game_loop():

    x = (411)
    y = (display_h * 0.7)   
    
    x_change = [311,411,511]
    '''foram levadas em consideração a largura do bloco e a largura da tela'''
    thing_startx = random.choice([300, 400, 500])                           
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    score=0
    
    delay = 0

    i = 0
    gameExit = False 
    clock = pygame.time.Clock()

        
    '''Define pikalist e sprites'''
    sprite = SpriteSheet('Pikachu.png')
    image = sprite.get_image(422,3,41,71,0)
    pikalist.append(image)
    image = sprite.get_image(473,10,49,65,0)
    pikalist.append(image)
    image = sprite.get_image(531,3,57,71,0)
    pikalist.append(image)
    image = sprite.get_image(596,13,53,62,0)
    pikalist.append(image)

    '''Define diglist e sprites'''
    sprite = SpriteSheet('Pikachu.png')
    image = sprite.get_image(422,3,41,71,0)
    diglist.append(image)
    image = sprite.get_image(473,10,49,65,0)
    diglist.append(image)
    image = sprite.get_image(531,3,57,71,0)
    diglist.append(image)
    image = sprite.get_image(596,13,53,62,0)
    diglist.append(image)

    
    while not gameExit:
        
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            '''Faz as imagens se movimentarem para a esquerda ou para a direita'''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > 411:
                    x = x_change[1]
                elif event.key == pygame.K_LEFT and x == 411:
                    x = x_change[0]
                elif event.key == pygame.K_RIGHT and x < 411:
                    x = x_change[1]
                elif event.key == pygame.K_RIGHT and x == 411:
                    x = x_change[2]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x = x

        '''Faz as imagens do pikachu serem trocadas'''
        '''Fazendo Digletts descerem na tela '''
        if delay > 30/len(pikalist):
            delay = 0
            '''pinta tala de branco'''
            gameDisplay.fill(white)
            gameDisplay.blit(pikalist[i],(x,y))
            gameDisplay.blit(diglist[i],(thing_startx,thing_starty))
            thing_starty = thing_starty + 20
            if i >= len(pikalist)-1:
                i = 0
            else:
                i += 1
        else:
            print(delay)
            delay += 1

        
        '''Aparece contagem de pontos'''
        score_count(score)

        if x > display_w - 78 or x < 0:                                     #fazendo as "bordas" do jogo
            crash()

        if thing_starty > display_h:                                       #calculando batida de carro em bloco
            thing_starty = 0 - thing_height
            thing_startx = random.choice([300, 400, 500])                       #condiciona o bloco a aparecer somente em 3 posições aleatoriamente
            score += 1
        
        if y < thing_starty+thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x+78 > thing_startx and x+78 < thing_startx + thing_width:
                print('x crossover')
                crash()

            
        clock.tick(60)
        pygame.display.flip()
        
game_loop()
