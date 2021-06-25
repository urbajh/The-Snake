import pygame, sys
from pygame.locals import *
import random

pygame.init()

#variables locales
screen_width = 400
screen_height = 400
snake_color = (255,0,0) #rojo
food_color = (0,255,0) # green
background = (0,0,0)

def ShowApple(screen_height):
    return random.randrange(10, screen_height-10)
    
def main():
    game_over= False
    axis_x=200
    axis_y=200
    snake_move=10
    apple = [round(ShowApple(screen_height)/10)*10,round(ShowApple(screen_height)/10)*10,10,10]
    print(apple)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")
    tail= []
    # hacer un array de numeros que vaya sumando cuando se come una manzana, 
    # tomando la ultimaposicion en la que estuvo la serpiente
    # cada vez que se realiza un movimiento se elimina el ultimo del array y se agrega la posicion del primero

    # cuando la cabeza colisione con alguna coordenada de su cuerpo el juego teremina
    while not game_over:
        for events in pygame.event.get():
            #print(events)
            if events.type == QUIT:
                game_over=True
            if axis_x == 0 or axis_x == 400 or axis_y == 0 or axis_y == 400:
                game_over=True
            elif events.type == KEYDOWN:
                if events.scancode == 79 or events.scancode == 7: #right   
                    axis_x+=snake_move
                    tail.insert(0,[axis_x,axis_y])
                    tail.pop()
                elif events.scancode == 80 or events.scancode == 4: #left  
                    axis_x-=snake_move
                    tail.insert(0,[axis_x,axis_y])
                    tail.pop()
                elif events.scancode == 82 or events.scancode == 26: #up
                    axis_y-=snake_move
                    tail.insert(0,[axis_x,axis_y])
                    tail.pop()
                elif events.scancode == 81 or events.scancode == 22: #down
                    axis_y+=snake_move
                    tail.insert(0,[axis_x,axis_y])
                    tail.pop()
            if(axis_x == apple[0] and axis_y == apple[1]):
                print('te comiste la manzana wey')
                tail.append([apple[0],apple[1]])  # agrega la posicion en la que estaba la manzana
                print('te crecio la cola goloso', tail)
                apple = [round(ShowApple(screen_height)/10)*10,round(ShowApple(screen_height)/10)*10,10,10]
            # que la manzana no aparezca en los bordes del mapa ni en los lugares que ocupa la serpiente

        screen.fill(background)
        for unit in tail:
                pygame.draw.rect(screen,snake_color,[unit[0],unit[1],10,10])
        pygame.draw.rect(screen,snake_color,[axis_x,axis_y,10,10])
        pygame.draw.rect(screen,snake_color,apple)
        pygame.draw.lines(screen,snake_color,True,[(0,0),(0, 400),(400,400),(400,0)], width=10)
        pygame.display.update()
        pygame.time.Clock().tick(30)
    return 

if __name__ == '__main__':
    pygame.init()
    main()