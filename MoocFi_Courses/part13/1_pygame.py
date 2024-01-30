import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("C:/Users/USER/Python_Basics/MoocFi_Courses/part13/robot.png")

window.fill((0, 0, 0))
# robots in 4 corners
# window.blit(robot, (0, 0))
# window.blit(robot, (640-robot.get_width(), 0))
# window.blit(robot, (0, 480-robot.get_height()))
# window.blit(robot, (640-robot.get_width(), 480-robot.get_height()))

# 10 robots in a row
# for x in range(10):
#     window.blit(robot, (30+50*x, 200))

# 100 robots (10*10)
# align_x = 10
# align_y = 10
# for x in range(10):
#     align_x += 10
#     for y in range(10):
#         align_y += 10
#         window.blit(robot, (20+10*x+30*x, 20+10*y+10*y))

# 1000 random robots
for _ in range(1000):
    random_x = random.randint(0, 640-robot.get_width())
    random_y = random.randint(0, 480-robot.get_height())
    window.blit(robot, (random_x, random_y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()