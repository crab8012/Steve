from pyglet.gl import *
import math

def drawCircle(radius, x, y):
	origin = (x, y)
	y = 0
	draw_point(origin[0], origin[1])
	#draw_point(origin[0] + radius, origin[1] + radius)
	#draw_point(origin[0] - radius, origin[1] - radius)
	while(True):
		draw_point(origin[0] + radius * math.cos(y), origin[1] + radius * math.sin(y))
		y = y + 1
		#if x == 360:
			#window.clear()
		if y == 360:
			break
			
	#x= 5 * math.cos⁡(1) , y=5 * math.sin(1)
	
def draw_point(x, y):
	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()

def draw_tree():
	x = window.width//2
	y=0
	
	draw_point(x, y)
	draw_point(x+10, y+10)
	draw_point(x+20, y+20)
	draw_point(x+30, y+30)
	draw_point(x+40, y+40)
	draw_point(x+50, y+50)
	draw_point(x+60, y+60)
	draw_point(x+70, y+70)
	draw_point(x+80, y+80)
	draw_point(x+90, y+90)
