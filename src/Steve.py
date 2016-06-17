import pyglet
from pyglet.gl import *
import crabGLShapes as shape
import SteveExtras as extras
import SteveCommands as commands
import threading


#key = pyglet.window.key
#if symbol == key.SPACE:
#	glClearColor(0.0, 0.0, 0.0, 0.0)

window = pyglet.window.Window(200, 60, style=pyglet.window.Window.WINDOW_STYLE_DIALOG)
window.set_location(0, 30)
window.set_caption('Steve - Not Listening')
extras.speak('"Ready"')

class thinkThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		globalVars.listening = True
		text = extras.recognize()
		commands.doCommand(text)
		globalVars.listening = False
		window.set_caption('Steve - Not Listening')
		return()

class crap():
	def cap(text):
		window.set_caption(text)

class globalVars():
	listening = False
	fullscreen = False
	
def drawBackground():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	glVertex2f(0, 0)
	glVertex2f(window.width, window.height)
	glEnd()

	glColor3f(1.0, 0.0, 0.0)
	glBegin(GL_LINES)
	glVertex2f(0, window.height)
	glVertex2f(window.width, 0)
	glEnd()

	glColor3f(0.0, 0.0, 1.0)
	glBegin(GL_LINES)
	glVertex2f(0, window.height//2)
	glVertex2f(window.width, window.height//2)
	glEnd()
	
	glColor3f(1.0, 1.0, 0.0)
	shape.drawCircle(50, window.width//2, window.height//2)

	glColor3f(0.0, 1.0, 1.0)
	shape.drawCircle(25, window.width//2, window.height//2)
	
	glColor3f(1.0, 0.0, 1.0)
	shape.drawCircle(12, window.width//2, window.height//2)

#@window.event
#def on_key_press(key, modifiers):
	#if key == 102:
		#if globalVars.fullscreen:
			#globalVars.fullscreen = False
			#window.fullscreen = False
		#elif not globalVars.fullscreen:
			#globalVars.fullscreen = True
			#window.fullscreen = True

	##print(key)

@window.event
def on_mouse_press(x, y, button, modifiers):
	if globalVars.listening == False:
		thread1 = thinkThread(1, "Thread-1")
		try:
			thread1.start()
		except:
			print("Error: unable to start thread")
				
	elif globalVars.listening == True:
		try:
			thread1.stop()
			globalVars.listening = False
			window.set_caption('Steve - Not Listening')
			extras.speak('"Not Listening"')
		except:
			print("Error Stopping Thread")

@window.event
def on_draw():
	drawBackground()

pyglet.app.run()
