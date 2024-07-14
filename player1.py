from graphics import *
import math

class Player:
	def __init__(self,window,x,y):
		self.circle=Circle(Point(x,y),15)
		self.circle.setFill(color_rgb(250,255,255))
		self.circle.setOutline(color_rgb(165,42,42))
		self.circle.draw(window)
		self.vel_x=0
		self.vel_y=0
		pass
	def update(self,keys,delta_time):
		if keys["w"]:
			self.vel_y=-50
		elif keys["a"]:
			self.vel_x=-50
		elif keys["d"]:
			self.vel_x=50
		elif keys["s"]:
			self.vel_y=50
		dx=self.vel_x*delta_time
		dy=self.vel_y*delta_time
		self.circle.move(dx,dy)
	def point_collision(self,x,y):
		center=self.circle.getCenter()
		Distance=((center.getX()-x)**2+(center.getY()-y)**2)**0.5
		if Distance < 15:
			return True
		else:
			return False
	def circle_collision(self,c):
		center=self.circle.getCenter()
		center1=c.getCenter()
		Distance=((center.getX()-center1.getX())**2+(center.getY()-center1.getY())**2)**0.5
		if Distance < 15+c.getRadius():
			return True
		else:
			return False
	def collision_with_enemy(self):
		self.circle.setFill(color_rgb(250,0,0))
