from math import pi
import random
import pygame
import PyParticles

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')

universe = PyParticles.Environment((width, height))
universe.colour = (255,255,255)
universe.addFunctions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
universe.acceleration = (pi, 0.2)
universe.mass_of_air = 0.02

#for p in range(4):
 #   universe.addParticles(mass=1000, size=6, speed=0, elasticity=0, colour=(20,40,200))
universe.addParticles(x=10, y=10, mass=1000, size=6, speed=0, elasticity=0, colour=(20,40,200))
universe.addParticles(x=10, y=110, mass=1000, size=6, speed=0, elasticity=0, colour=(20,40,200))
universe.addParticles(x=110, y=10, mass=1000, size=6, speed=0, elasticity=0, colour=(20,40,200))
universe.addParticles(x=110, y=110, mass=1000, size=6, speed=0, elasticity=0, colour=(20,40,200))

    
universe.addSpring(0,1, length=100, strength=90)
universe.addSpring(1,2, length=100, strength=90)
universe.addSpring(2,0, length=140, strength=60)
universe.addSpring(2, 3, length=100, strength=90)
universe.addSpring(1,3,length=140, strength=60)
universe.addSpring(0, 3, length=100, strength=100)


# Make a "rope"
for x in range(10):
   universe.addParticles(mass=500, size=2, speed=0, elasticity=0, colour=(200,40,40))

universe.addSpring(3, 4, length=10, strength = 10)

universe.addSpring(4, 5, length=10, strength = 10) 
universe.addSpring(5, 6, length=10, strength = 10)
universe.addSpring(6, 7, length=10, strength = 10)
universe.addSpring(7, 8, length=10, strength = 10)
universe.addSpring(8, 9, length=10, strength = 10)
universe.addSpring(9, 10, length=10, strength = 10)
universe.addSpring(10, 11, length=10, strength = 10)
universe.addSpring(11, 12, length=10, strength = 10)
universe.addSpring(12, 13, length=10, strength = 10)
universe.addSpring(1, 13, length=10, strength = 10)






selected_particle = None
paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = universe.findParticle(mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouseMove(pygame.mouse.get_pos())
    if not paused:
        universe.update()
        
    screen.fill(universe.colour)
    
    for p in universe.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
        
    for s in universe.springs:
        pygame.draw.aaline(screen, (0,0,0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))

    pygame.display.flip()
