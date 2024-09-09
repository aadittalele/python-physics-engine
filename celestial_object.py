import math
import random
import pygame

class CelestialObject:
  def __init__(self, x, y, mass, radius, x_velocity, y_velocity):
    self.x = x
    self.y = y
    if mass <= 0:
      self.mass = 1000
    self.mass = mass
    self.radius = radius
    self.velocity_x = x_velocity
    self.velocity_y = y_velocity
    self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

  def update(self, celestial_objects):
    # if self.radius > 70:
    #   return
    
    force_x = 0
    force_y = 0

    for i in range(len(celestial_objects)):
      obj = celestial_objects[i]
      if obj != self:
        dx = self.x - obj.x
        dy = self.y - obj.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance < self.radius + obj.radius:
          if self.mass != 0 or obj.mass != 0:
            if self.radius < obj.radius:
              self.radius = 0
              self.mass = 0
            else:
              obj.radius = 0
              obj.mass = 0
            continue

        force = (0.001 * self.mass * obj.mass) / (distance ** 2) 

        angle = math.atan2(dy, dx)

        force_x -= force * math.cos(angle)
        force_y -= force * math.sin(angle)

    if self.mass != 0:
      self.velocity_x += force_x / self.mass
      self.velocity_y += force_y / self.mass

    self.x += self.velocity_x
    self.y += self.velocity_y

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)