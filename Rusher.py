'''
Created on Mar 9, 2014

@author: Administrator
'''
import sfml as sf
class Rusher(object):
    
    def __init__(self,position):
        self.speed = 1
        self.angle = 0
        self.circle = sf.CircleShape()
        self.circle.position = position
        self.circle.radius = 5
        self.circle.outline_color = sf.Color.RED
        self.circle.outline_thickness = 1
        self.goal = sf.Vector2(400,-100)
        
    def get_positon(self):
        return self.circle.position
    
    def get_speed(self):
        return self.speed
    
    def draw(self,target):
        target.draw(self.circle)
        
    def update_pos(self):
        x_dis = self.circle.position.x - self.goal.x
        y_dis = self.circle.position.y - self.goal.y
        self.circle.position = self.circle.position + sf.Vector2(0.01,0)
        
    