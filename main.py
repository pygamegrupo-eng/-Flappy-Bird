import pygame
import sys 

Ancho=800
Alto=600
black=(0,0,0)

Fps=60

#pj
player_size = 40      
player_x = 100       
player_y = 300       
player_color = (255, 255, 0)  

pygame.init()
pygame.display.set_caption(" ")
screen =pygame.display.set_mode((Ancho,Alto))
clock=pygame.time.Clock()

ejecutando=True
while ejecutando:
  for evento in pygame.event.get():
    if evento.type==pygame.QUIT:
      ejecutando=False
  

 

    screen.fill(black)

    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    
    pygame.display.flip()
    clock.tick(Fps)

pygame.quit()
sys.exit()







