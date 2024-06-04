import pygame
import math
from snowflake import snowflake
from snowflake_machine import snowflake_machine

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

outside_snowflakes=snowflake_machine(screen,2,2,12,0,1280,720)

def draw_fancy_snowflake():
    # center
    center = (640, 360)
    # radius
    radius = 180
    # line width
    line_width= 9
    # middle vertical line
    pygame.draw.line(screen, "white", (center[0], center[1]-radius), (center[0],center[1]+radius ), line_width)
    # middle horizontal line
    pygame.draw.line(screen, "white", (center[0]-radius, center[1]), (center[0]+radius, center[1]), line_width)
    # A, diagonal distance
    A=radius/math.sqrt(2)
    # right diagonal line
    pygame.draw.line(screen,"white",(center[0]+A,center[1]-A),(center[0]-A,center[1]+A), line_width)
    # left diagonal line
    pygame.draw.line(screen,"white",(center[0]+A,center[1]+A),(center[0]-A,center[1]-A), line_width)
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.

    #custom_color=pygame.Color(red,green, blue)
    screen.fill("blue")  # Fill the display with a solid color

    # Render the graphics here.
    outside_snowflakes.update()
    pygame.draw.polygon(screen, "white", [(640, 530), (400, 720), (880, 720)])
    pygame.draw.circle(screen, "lightblue", (640,360),200)
    draw_fancy_snowflake()
    clock.tick(24)         # wait until next frame (at 20 FPS)
    pygame.display.flip()


