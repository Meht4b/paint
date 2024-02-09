import pygame
from classes import *
pygame.init()

window = pygame.display.set_mode((1000,1000))
radius = 10
sock = ClientNetwork()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        if event.type == pygame.MOUSEWHEEL:
            radius += event.y
            radius = 1 if radius<1 else radius

    if pygame.mouse.get_pressed()[0]:
        sock.send((pygame.mouse.get_pos(),radius))
        pygame.draw.circle(window,(255,255,255),pygame.mouse.get_pos(),radius)
    else:
        sock.send(None)

    coords = pickle.loads(sock.recv())
    print(coords)
    for i in coords:
        pygame.draw.circle(window,(255,255,255),i[0],i[1])

    pygame.display.update()