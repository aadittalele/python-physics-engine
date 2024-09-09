import math
import pygame
import celestial_object

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Physics Engine")

celestial_objects = []
tempObject = None
tempVelocities = [0, 0]

running = True
dragging = False
pointing = False

FPS = 60
clock = pygame.time.Clock()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
      dragging = False
      pointing = False
      celestial_objects = []
      tempObject = None
      tempVelocities = [0, 0]

    if keys[pygame.K_s]:
      dragging = False
      pointing = False
      celestial_objects = []
      tempObject = None
      tempVelocities = [0, 0]
      
      celestial_objects.append(celestial_object.CelestialObject(400, 300, 1000000, 155, 0, 0)) # Star
      celestial_objects.append(celestial_object.CelestialObject(400, 600, 1500, 15, 1.85, 0)) # Planet
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()
      start_pos = mouse_pos
      if not pointing:
        pos = pygame.mouse.get_pos()
        tempObject = celestial_object.CelestialObject(pos[0], pos[1], 0, 10, 0, 0)
        celestial_objects.append(tempObject)
        dragging = True

    if event.type == pygame.MOUSEMOTION:
        if dragging or pointing:
          mouse_pos = pygame.mouse.get_pos()
          start_pos = (tempObject.x, tempObject.y)
          distance = ((mouse_pos[0] - start_pos[0]) ** 2 + (mouse_pos[1] - start_pos[1]) ** 2) ** 0.5
          angle = math.atan2(mouse_pos[1] - start_pos[1], mouse_pos[0] - start_pos[0])

          if dragging:
            tempObject.radius = max(distance, 10)
          if pointing:
            tempVelocities[0] = math.cos(angle) * distance / 50
            tempVelocities[1] = math.sin(angle) * distance / 50

    if event.type == pygame.MOUSEBUTTONUP:
      if pointing:
        pointing = False
        tempObject.mass = tempObject.radius * 6660
        
        if tempVelocities[0] ** 2 + tempVelocities[1] ** 2 < 0.25:
          tempVelocities = [0, 0]
        tempObject.velocity_x = tempVelocities[0]
        tempObject.velocity_y = tempVelocities[1]
      if dragging:
        dragging = False
        pointing = True

  for obj in celestial_objects:
    obj.update(celestial_objects)

  screen.fill((0, 0, 0))

  for obj in celestial_objects:
    obj.draw(screen)

  if pointing:
    pygame.draw.line(screen, (255, 0, 0), start_pos, (mouse_pos[0], mouse_pos[1]), width=5)

  pygame.display.flip()

  dt = clock.tick(FPS) / 1000

pygame.quit()