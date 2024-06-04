import pygame

class snowflake:
    def __init__(self,surface,radius,speed,start_x,start_y,color="white"):
        self.surface=surface
        self.radius=radius
        self.speed=speed
        self.x=start_x
        self.y=start_y
        self.color=color
    def draw(self):
        pygame.draw.circle(self.surface,self.color,(self.x,self.y),self.radius)
    def update(self):
        self.y+=self.speed