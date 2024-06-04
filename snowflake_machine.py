import pygame
from snowflake import snowflake
import random
class snowflake_machine:
    def __init__(self,screen,speed,frames_per_snowflake,radius,min_x,max_x,end_y,start_y=0):
        self.screen=screen
        self.speed=speed
        self.frames_per_snowflake=frames_per_snowflake
        self.radius=radius
        self.min_x=min_x
        self.max_x=max_x
        self.start_y=start_y
        self.end_y=end_y
        self.snowflakes=[]
        self.elapsed_time=0
    def create_snowflake(self):
        start_x=random.randint(self.min_x,self.max_x)
        self.snowflakes.append(snowflake(self.screen,self.radius,self.speed,start_x,self.start_y))
    def draw_snowflake(self):
        for i in range (len(self.snowflakes)-1,-1,-1):
           self.snowflakes[i].update()
           if self.snowflakes[i].y>self.end_y:
               self.snowflakes.pop(i)
           self.snowflakes[i].draw()
    def update(self):
        self.elapsed_time+=1
        if self.elapsed_time>=self.frames_per_snowflake:
            self.create_snowflake()
            self.elapsed_time=0
        self.draw_snowflake()

