import subprocess
import speech_recognition as sr
import platform
#import Steve.crap as ai

def speak(text):
	if platform.system() == 'Windows':
		subprocess.call('"C:\Program Files (x86)\eSpeak\command_line\espeak.exe" '+text, shell=True)
	elif platform.system() == 'Linux':
		subprocess.call('espeak '+text, shell=True)
	elif platform.system() == 'Darwin':
		print("Sorry. There is no support for Mac OS X."

def recognize():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Now listening for speech")
		#ai.cap('Steve - Listening')
		speak("Listening")
		audio = r.listen(source)
	#Recognise speech using the Google Speech Recognition
	try:
		googleString = r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Google Spech cannot recognize your speech")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	
	try:
		return(googleString)
	except UnboundLocalError:
		print("error returning string")
		return('ERROR')
		
def readCompanyBalance():
	balFile = open('companyBalance.txt', 'r')
	bal = balFile.readline().rstrip()
	balFile.close()
	return(bal)
