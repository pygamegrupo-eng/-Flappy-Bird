import pygame
import sys 

Ancho=800
Alto=600
black=(0,0,0)

Fps=60

#pj
Suelo_Y = Alto - 50
player_size = 40      
player_x = 100       
player_y = Suelo_Y - player_size
player_color = (255, 255, 0)  
color_piso = (104, 106, 217)


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

  pygame.draw.rect(screen, color_piso ,(0, Suelo_Y, Ancho, 50))
  pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    
  pygame.display.flip()
  clock.tick(Fps)

pygame.quit()
sys.exit()







