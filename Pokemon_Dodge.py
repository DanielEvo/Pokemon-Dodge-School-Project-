import pygame
import time
import mixer
import random
import os
from ClassSpriteSheet import SpriteSheet


'''inicia Python, define tamanho da tela, define nome da tela e seta clock'''
pygame.init()

'''inicia em uma posição no PC x=150 e y=100'''
os.environ["SDL_VIDEO_WINDOW_POS"] = "150,100"
screen = pygame.display.set_mode((1,1))
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
    font = pygame.font.Font(None, 40)
    text = font.render("Dodges: "+str(count), True, black)
    gameDisplay.blit(text,(430,570))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def gameover(text,score):
    largeText = pygame.font.Font('freesansbold.ttf',110) 
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_w/2),(display_h/2))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf2, TextRect2 = text_objects("Score: "+str(score), largeText)
    TextRect2.center = ((display_w/2),(display_h/1.25))
    gameDisplay.blit(TextSurf2, TextRect2)
    pygame.display.update()
    
    time.sleep(2)

    game_loop()
    
def crash(score):
    mixer.music.load("Pokemon_End.wav")
    mixer.music.play(-1,0.0)    
    pikafainted = pygame.image.load('pika_fainted.png')
    image = pygame.transform.scale(pikafainted, (1000, 600))
    gameDisplay.blit(image,(0,0))
    gameover('You are Fainted',score)

def message_init(text):
    largeText = pygame.font.Font('freesansbold.ttf',17) 
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_w/2),(510))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

def inicial():

    intro = True
    mixer.music.load("Pokemon_Init1.wav")
    mixer.music.play(-1,0.0)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or pygame.K_KP_ENTER:
                    print("ok")
                    intro = False

        gamecover = pygame.image.load('game_cover.png')
        cover = pygame.transform.scale(gamecover, (1000, 600))
        gameDisplay.blit(cover,(0,0))
        message_init('Press and hold ENTER to start')
        time.sleep(0.25)
        gameDisplay.blit(cover,(0,0))
        message_init('                    ')
        time.sleep(0.25)
        pygame.display.update()

    mixer.music.load("Pokemon_Enter.wav")
    mixer.music.play(-1,0.0)    
    game_loop()
    
def game_loop():

    x = (481)
    y = (display_h * 0.7)   
    diglettpos=[0,0,0]
    x_change = [410,481,552]
    '''foram levadas em consideração a largura do bloco e a largura da tela'''
    diglett_startx = random.choice([400, 471, 542])
    if diglett_startx == 400:
        diglettpos=[1,0,0]
    elif diglett_startx == 471:
        diglettpos=[0,1,0]
    else:
        diglettpos=[0,0,1]
    diglett_starty = -600
    diglett_speed = 30
    diglett_width = 71
    diglett_height = 66
    '''coordenadas das duas imagens de background'''
    gnd1_x = 0
    gnd1_y = -5801
    gnd2_x = 0
    gnd2_y = -12201
    pikapos=[0,1,0]

    score = 0
    delay = 0
    pikalist.clear()
    diglist.clear()

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
    
    mixer.music.load("Pokemon_Game.wav")
    mixer.music.play(-1,0.0)
    
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
                    pikapos=[0,1,0]
                elif button_L1 and x == 481:
                    x = x_change[0]
                    pikapos=[1,0,0]
                elif button_R1 and x < 481:
                    x = x_change[1]
                    pikapos=[0,1,0]
                elif button_R1 and x == 481:
                    x = x_change[2]
                    pikapos=[0,0,1]

                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            '''Faz as imagens se movimentarem para a esquerda ou para a direita'''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > 481:
                    x = x_change[1]
                    pikapos=[0,1,0]
                elif event.key == pygame.K_LEFT and x == 481:
                    x = x_change[0]
                    pikapos=[1,0,0]
                elif event.key == pygame.K_RIGHT and x < 481:
                    x = x_change[1]
                    pikapos=[0,1,0]
                elif event.key == pygame.K_RIGHT and x == 481:
                    x = x_change[2]
                    pikapos=[0,0,1]
                    
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
            diglett_starty = diglett_starty + diglett_speed
            gameDisplay.blit(backgnd1,(gnd1_x,gnd1_y))
            gameDisplay.blit(backgnd2,(gnd2_x,gnd2_y))
            gameDisplay.blit(pikalist[i],(x,y))
            gameDisplay.blit(diglist[i],(diglett_startx,diglett_starty))

            gnd1_y = gnd1_y + 10
            gnd2_y = gnd2_y + 10
            if i >= len(pikalist)-1:
                i = 0
            else:
                i += 1
        else:
            delay += 1

        
        '''Aparece contagem de pontos'''
        score_count(score)

        if gnd1_y > 600:
            gnd1_y = -12102

        if gnd2_y > 600:
            gnd2_y = -12102

        if diglett_starty > display_h:
            diglett_starty = 0 - diglett_height
            '''condiciona o bloco a aparecer somente em 3 posições aleatoriamente dentro do loop'''
            diglett_startx = random.choice([400, 471, 542])
            '''atualiza posição do diglett na lista diglettpos'''
            if diglett_startx == 400:
                diglettpos=[1,0,0]
            elif diglett_startx == 471:
                diglettpos=[0,1,0]
            else:
                diglettpos=[0,0,1]
            
            score += 1
        
        if (y < diglett_starty+diglett_height) and (diglett_starty < 483):
            isDead=0
            for a in range(len(pikapos)):
                isDead+=pikapos[a]*diglettpos[a]
            if isDead:
                crash(score)
                
    
        clock.tick(100+score*5)
        pygame.display.flip()

inicial()
game_loop()
