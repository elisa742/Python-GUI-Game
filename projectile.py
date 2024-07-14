from graphics import *

class Projectile:

	def __init__(self, window, x, y):
		self.circle = Circle(Point(x, y), 10)
		self.circle.setFill(color_rgb(250,255,255))
		self.circle.setOutline(color_rgb(165,42,42))
		self.circle.draw(window)
		self.vel_x=50
		self.vel_y=0

	def update(self,delta_time):
		dx=self.vel_x*delta_time
		dy=self.vel_y*delta_time
		self.circle.move(dx,dy)

	def circle_collision(self,c):
		center=self.circle.getCenter()
		center1=c.getCenter()
		Distance=((center.getX()-center1.getX())**2+(center.getY()-center1.getY())**2)**0.5
		if Distance< 10+c.getRadius():
			return True
		else:
			return False
		

