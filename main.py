import pygame
import sys 

Ancho=800
Alto=600

Fps=60

pygame.init()
pygame.display.set_caption(" ")
screen =pygame.display.set_mode((Ancho,Alto))
clock=pygame.time.Clock()

ejecutando=True
while ejecutando:
  for evento in pygame.event.get():
    if evento.type==pygame.QUIT:
      ejecutando=False
  pygame.display.flip()

  clock.tick(Fps)

pygame.quit()








