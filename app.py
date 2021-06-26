import pygame, sys
from pygame.locals import *
import random

pygame.init()

#variables locales
screen_width = 400
screen_height = 400
border_background = (200,200,200)
snake_color_body = (0,180,0) # green
snake_color_head = (0,255,0)
apple_color = (180,0,0) #rojo
background = (0,0,0)
snake_move=10
screen = pygame.display.set_mode((screen_width, screen_height))

font_game = pygame.font.SysFont('Arial',20)
font_game2 = pygame.font.SysFont('Arial',18)
def createRandomApple(screen_height):
    return round(random.randrange(10, screen_height-20)/10)*10 

#render de instrucciones
screen.blit(pygame.font.Font.render(font_game2, "Instrucciones para jugar:",1,(150,150,150)),(100,40))
screen.blit(pygame.font.Font.render(font_game2, "Puedes moverte con teclas W,A,S,D",1,(150,150,150)),(30,80))
screen.blit(pygame.font.Font.render(font_game2, "Puedes moverte con las flechas",1,(150,150,150)),(30,120))
screen.blit(pygame.font.Font.render(font_game2, "Debes comer manzanas para obtener Puntos",1,(150,150,150)),(30,160))
screen.blit(pygame.font.Font.render(font_game2, "Pierdes al impactar con los bordes",1,(150,150,150)),(30,200))
screen.blit(pygame.font.Font.render(font_game2, "Pierdes al impactar con tu propio cuerpo",1,(150,150,150)),(30,240))
screen.blit(pygame.font.Font.render(font_game, "Presiona la tecla Enter para comenzar",1,(150,150,150)),(30,280))

def main():
    game_over= False
    coor_x=200
    coor_y=200
    automove_x=0
    automove_y=0
    last_move= ''
    delay_game= 200
    game_start= False
    tail= [[coor_x, coor_y]]
    apple = [createRandomApple(screen_width),createRandomApple(screen_height),10,10]
    pygame.display.set_caption("The Snake")
    
    while not game_over:
        pygame.time.delay(delay_game)
        if(coor_x == apple[0] and coor_y == apple[1]):
            tail.append([apple[0],apple[1]])  # agrega la posicion en la que estaba la manzana
            apple = [createRandomApple(screen_width),createRandomApple(screen_height),10,10]
            for x in tail: #la manzana no aparecera en el cuerpo de la serpiente
                if apple[0] == x[0] and apple[1] == x[1]:
                    apple = [createRandomApple(screen_width),createRandomApple(screen_height),10,10]
        #colision con el borde
        if coor_x < 10 or coor_x > 380 or coor_y < 10 or coor_y > 380:
                game_over=True
        for events in pygame.event.get():
            if events.type == QUIT:
                game_over=True
            elif events.type == KEYDOWN:
                if events.scancode == 40:
                    game_start = True
                if events.scancode == 79 or events.scancode == 7: #right
                    if last_move != 'left':   
                        tail.insert(0,[coor_x,coor_y])
                        tail.pop()
                        automove_x= 10
                        automove_y= 0
                        last_move= 'right'
                elif events.scancode == 80 or events.scancode == 4: #left  
                    if last_move != 'right':
                        tail.insert(0,[coor_x,coor_y])
                        tail.pop()
                        automove_x= -10
                        automove_y= 0
                        last_move='left'
                elif events.scancode == 82 or events.scancode == 26: #up
                    if last_move != 'down':
                        tail.insert(0,[coor_x,coor_y])
                        tail.pop()
                        automove_y= -10
                        automove_x= 0
                        last_move = 'up'
                elif events.scancode == 81 or events.scancode == 22: #down
                    if last_move != 'up':
                        tail.insert(0,[coor_x,coor_y])
                        tail.pop()
                        automove_y= 10
                        automove_x= 0
                        last_move='down'
                elif events.scancode == 41:
                    game_over=True
        #automovimiendo
        coor_x= coor_x + automove_x
        coor_y= coor_y + automove_y
        tail.insert(0,[coor_x,coor_y])
        tail.pop()
        #reder del juego
        if game_start == True:
            screen.fill(background)
            pygame.draw.rect(screen,snake_color_head,[coor_x,coor_y,10,10])
            pygame.draw.rect(screen,apple_color,apple)
            screen.blit(pygame.font.Font.render(font_game, f"Score: {len(tail)-1}",False,(150,150,150)),(15,15))
            pygame.draw.lines(screen,border_background,True,[(0,0),(0, 400),(400,400),(400,0)], width=10)
        #haciendo render de la cola y validando la colision de cabeza con el cuerpo
        for unit in tail[1:]:
                pygame.draw.rect(screen,snake_color_body,[unit[0],unit[1],10,10])
                if coor_x == unit[0] and coor_y == unit[1]:
                    game_over=True
        pygame.display.update()
    return 

if __name__ == '__main__':
    pygame.init()
    main()