import pygame
import random

# Define screen size
WIDTH = 800
HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # List of colors for circles

# Define circle class
class Circle:
  def __init__(self, x, y, radius, color):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.dx = random.randint(-5, 5)  # Randomize initial x-direction speed
    self.dy = random.randint(-5, 5)  # Randomize initial y-direction speed

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

  def update(self):
    # Bounce off edges
    if self.x + self.radius > WIDTH or self.x - self.radius < 0:
      self.dx *= -1
    if self.y + self.radius > HEIGHT or self.y - self.radius < 0:
      self.dy *= -1

    # Update position
    self.x += self.dx
    self.y += self.dy

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Colored Circles")
clock = pygame.time.Clock()

# Create circles
circles = []
for i in range(10):  # Create 10 circles
  x = random.randint(0 + 50, WIDTH - 50)  # Random x within screen (avoid edges)
  y = random.randint(0 + 50, HEIGHT - 50)  # Random y within screen (avoid edges)
  radius = random.randint(10, 30)  # Random radius
  color = random.choice(colors)  # Choose random color from list
  circles.append(Circle(x, y, radius, color))

# Main loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Clear screen
  screen.fill(BLACK)

  # Update and draw circles
  for circle in circles:
    circle.update()
    circle.draw(screen)

  # Update display
  pygame.display.flip()

  # Set frame rate
  clock.tick(60)  # Aim for 60 FPS

# Quit Pygame
pygame.quit()
