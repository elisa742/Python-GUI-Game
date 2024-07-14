from graphics import *
import math

class Enemy:
	def __init__(self,win,x,y):
		self.circle=Circle(Point(x,y),10)
		self.circle.setFill(color_rgb(123,104,238))
		self.circle.setOutline(color_rgb(0,0,0))
		self.circle.draw(win)
		self.vel_x=-50
		self.vel_y=0

	def update(self,x,y,delta_time):
		dx=self.vel_x*delta_time
		dy=self.vel_y*delta_time
		self.circle.move(dx,dy)
	def circle_collision(self,c):
		center=self.circle.getCenter()
		center1=c.getCenter()
		Distance=((center.getX()-center1.getX())**2+(center.getY()-center1.getY())**2)**0.5
		if Distance<20:
			return True
		else:
			return False

class Third_enemy:
	def __init__(self,win,x,y):
		self.circle=Circle(Point(x,y),10)
		self.circle.setFill(color_rgb(255,255,0))
		self.circle.setOutline(color_rgb(0,0,0))
		self.vel_y=-1
		self.vel_x=-50
		self.circle.draw(win)
	def update(self,x,y,delta_time):
		x_axis=self.circle.getCenter().getX()
		dx=self.vel_x*delta_time
		dy=int(math.sin(x_axis/400*8*math.pi)*200)*self.vel_y*delta_time
		self.circle.move(dx,dy)
	def circle_collision(self,c):
		center=self.circle.getCenter()
		center1=c.getCenter()
		Distance=((center.getX()-center1.getX())**2+(center.getY()-center1.getY())**2)**0.5
		if Distance<20:
			return True
		else:
			return False
class Chase:
	def __init__(self,win,x,y):
		self.circle=Circle(Point(x,y),10)
		self.circle.setFill(color_rgb(0,0,255))
		self.circle.setOutline(color_rgb(0,0,0))
		self.circle.draw(win)
		self.vel_y=-0.1
		self.vel_x=-0.1
	def update(self,x,y,delta_time):
		dx=-self.vel_x*delta_time*(x-self.circle.getCenter().getX())
		dy=-self.vel_y*delta_time*(y-self.circle.getCenter().getY())
		self.circle.move(dx,dy)
	def circle_collision(self,c):
		center=self.circle.getCenter()
		center1=c.getCenter()
		Distance=((center.getX()-center1.getX())**2+(center.getY()-center1.getY())**2)**0.5
		if Distance<20:
			return True
		else:
			return False
	