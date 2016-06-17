import pyglet
from pyglet.gl import *
from datetime import datetime
import time

window = pyglet.window.Window(1366, 768, fullscreen=True)

localTime = time.asctime(time.localtime(time.time()))
timeText = pyglet.text.Label(localTime, font_name='Times New Roman', font_size=40, x=window.width//2, y=window.height, anchor_x='center', anchor_y='top', color=(66,194,31,255))#
balText = pyglet.text.Label('', font_name='Times New Roman', font_size=80, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='top', color=(66,194,31,255))#

@window.event
def on_mouse_press(x, y, button, modifiers):
	glColor3f(0.0, 1.0, 0.0)
	draw_point(x, y)

def draw_point(x, y):
	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()

@window.event
def on_draw():
	timeText.draw()
	balText.draw()

def updateTime(rate):
	
	window.clear()
	localTime = time.asctime(time.localtime(time.time()))
	timeText.text = ''
	timeText.text = localTime	
	
	#currentTime = str(datetime.now().time())
	#localTime = time.asctime(time.localtime(time.time()))
	#timeText.text=localTime
	
def readCompanyBalance():
	balFile = open('companyBalance.txt', 'r')
	bal = balFile.readline().rstrip()
	balFile.close()
	return(bal)

def updateBalance(interval):
	balText.text = str(readCompanyBalance())
	
updateBalance(0)
pyglet.clock.schedule(updateTime)
pyglet.clock.schedule_interval(updateBalance, 30)
pyglet.app.run()
#def main(args):
#	print(args)
#	pyglet.app.run()
#	return 0

#if __name__ == '__main__':
#	import sys
#	sys.exit(main(sys.argv))
