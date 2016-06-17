import SteveExtras as extras
import subprocess
import sys

def doCommand(text):
	text = text.lower()
	words = text.split()
	
	
	#This is for unchanging information
	if text == "what is your name":
		extras.speak('"My name is Steve."')
	if text == "who do you work for":
		extras.speak('"I work for a company called TechHeads"')
	if text == "who owns tekheads":
		extras.speak('"Jordan Petersen and Spencer Peck are the current owners of TechHeads"')
		
	#This is for changing inormation that is not online.
	if text == "what is the company's balance":
		bal = extras.readCompanyBalance()
		extras.speak(bal+"Dollars")
		
	#This is for accessibility and opening programs.
	if words[0] == "open":
		subprocess.call(words[1]+'.exe', shell=True)
	if text == "quit" or text == "exit":
		sys.exit(0)
	
	else:
		extras.speak('"Invalid Command"')
		print(text)
	
	return True
