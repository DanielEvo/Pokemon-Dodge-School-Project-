import pygame
import time
import random
from ClassSpriteSheet import SpriteSheet


'''inicia Python, define tamanho da tela, define nome da tela e seta clock'''
pygame.init()
display_w = 1000
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

    
def score_count(count):
    font = pygame.font.Font(None, 25)
    text = font.render("Dodges: "+str(count), True, white)
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
    pikafainted = pygame.image.load('pika_fainted.png')
    image = pygame.transform.scale(pikafainted, (1000, 600))
    gameDisplay.blit(image,(0,0))
    message_display('You are Fainted')

def inicial():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',110) 
        TextSurf, TextRect = text_objects("Pokemon Dodge", largeText)
        TextRect.center = ((display_w/2),(display_h/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
    
        
def game_loop():

    x = (481)
    y = (display_h * 0.7)   
    
    x_change = [410,481,552]
    '''foram levadas em consideração a largura do bloco e a largura da tela'''
    thing_startx = random.choice([400, 471, 542])                           
    thing_starty = -600
    thing_speed = 30
    thing_width = 71
    thing_height = 66
    '''coordenadas das duas imagens de background'''
    gnd1_x = 0
    gnd1_y = -5801
    gnd2_x = 0
    gnd2_y = -12201

    score = 0
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
    sprite = SpriteSheet('Diglett.png')
    image = sprite.get_image(150,1,71,66,0)
    diglist.append(image)
    image = sprite.get_image(225,12,71,54,0)
    diglist.append(image)
    image = sprite.get_image(76,294,71,38,0)
    diglist.append(image)
    image = sprite.get_image(150,293,71,38,0)
    diglist.append(image)

    '''Define background'''
    sprite = SpriteSheet('Background.png')
    image = sprite.get_image(1588,510,832,6401,0)
    backgnd1 = pygame.transform.scale(image, (1000, 6400))
    backgnd2 = pygame.transform.scale(image, (1000, 6400))

   

    # Inicializa o joystick
    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

 
    while not gameExit:

        if pygame.joystick.get_count() > 0:
            # Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo horizontal, onde (0) é parado
            axis_lh = joystick.get_axis(0)
            # Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo vertical, onde (0) é parado
            axis_lv = joystick.get_axis(1)
                    
            # Recebe valor inteiro de (-1) e (1) para os botões direcionais, onde (0) é parado
            hat = joystick.get_hat(0)
                    
            # Mapa de botões, recebem valor booleano quando pressionados
            button_square = joystick.get_button(3)
            button_x = joystick.get_button(2)
            button_circle = joystick.get_button(1)
            button_triangle = joystick.get_button(0)
            button_L1 = joystick.get_button(4)
            button_R1 = joystick.get_button(5)
            button_L2 = joystick.get_button(6)
            button_R2 = joystick.get_button(7)
            button_start = joystick.get_button(9)


        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if button_L1 and x > 481:
                    x = x_change[1]
                elif button_L1 and x == 481:
                    x = x_change[0]
                elif button_R1 and x < 481:
                    x = x_change[1]
                elif button_R1 and x == 481:
                    x = x_change[2]

                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            '''Faz as imagens se movimentarem para a esquerda ou para a direita'''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > 481:
                    x = x_change[1]
                elif event.key == pygame.K_LEFT and x == 481:
                    x = x_change[0]
                elif event.key == pygame.K_RIGHT and x < 481:
                    x = x_change[1]
                elif event.key == pygame.K_RIGHT and x == 481:
                    x = x_change[2]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x = x

        
        '''Faz Pikachu correr'''
        '''Fazendo Digletts descerem na tela '''
        '''Fazendo Background descer'''
        if delay > 30/len(pikalist):
            delay = 0
            '''pinta tela de branco'''
            gameDisplay.fill(white)
            '''coloca background'''
            '''NECESSÁRIO MODIFICAR IMAGEM DE BACKGROUND PARA ACRESCENTAR
            MAIS LUGARES E NECESSARIO ARRUMAR POSIÇÕES DE SPRITES'''
            gameDisplay.blit(backgnd1,(gnd1_x,gnd1_y))
            gameDisplay.blit(backgnd2,(gnd2_x,gnd2_y))
            gameDisplay.blit(pikalist[i],(x,y))
            gameDisplay.blit(diglist[i],(thing_startx,thing_starty))
            thing_starty = thing_starty + thing_speed
            gnd1_y = gnd1_y + 10
            gnd2_y = gnd2_y + 10
            if i >= len(pikalist)-1:
                i = 0
            else:
                i += 1
        else:
            #print(delay)
            delay += 1

        
        '''Aparece contagem de pontos'''
        score_count(score)

        if gnd1_y > 600:
            gnd1_y = -12102

        if gnd2_y > 600:
            gnd2_y = -12102

        if thing_starty > display_h:
            thing_starty = 0 - thing_height
            '''condiciona o bloco a aparecer somente em 3 posições aleatoriamente dentro do loop'''
            thing_startx = random.choice([400, 471, 542])
            score += 1
        
        if y < thing_starty+thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x+50 > thing_startx and x+50 < thing_startx + thing_width:
                print('x crossover')
                crash()
    
        clock.tick(100)
        pygame.display.flip()

inicial()
game_loop()
