# Conversation by Kevin Xie
# CS550 09/18/2018
# Asks and responds to questions (bonus storyline!)
# sources: time delays https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
#		   "checking" that string is a digit https://stackoverflow.com/questions/21388541/how-do-you-check-in-python-whether-a-string-contains-only-numbers
#		   quotations in quotations https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks

import time #used for brief pauses that add a "human touch" to the conversation

def introduction(): 
	name = input("Hi there, what's your name? \n\n>>> ")
	nameResponse(name) # name is inputted into every function as it is used from time to time in conversation

def nameResponse(name): 
	if name == "Kevin": # sneaky personalized outcome
		print("...")
		time.sleep(2) # (re)learned from https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
		print("Sorry I didn't recognize you, Creator.")
		time.sleep(2)
		print("Please don't deactivate me.")
		time.sleep(2)
		print("You look like you need a drink.")
		time.sleep(2)
		sleepAnalysis(name)
	elif name != "Kevin":
		metBefore(name)

def metBefore(name): 
	hasMet = input("Hello there, "+name+", you must be new! Have we met before? \n\n>>> ")
	if hasMet == "yes":
		print("...")
		time.sleep(2)
		print("I knew you looked familiar! Just a little bit tired.")
		sleepAnalysis(name)
	elif hasMet == "no":
		print("Well, I'm Py, your virtual friend!")
		time.sleep(1)
		print("You look tired.")
		sleepAnalysis(name)
	else: # in order to avoid errors
		print("It's a yes or no question, "+name+"! Try again.")
		metBefore(name)

def sleepAnalysis(name): # this is where the bulk of the "intellegent responses" come from
	hours = input("How many hours did you sleep last night, "+name+"? \n\n>>> ")
	time.sleep(2)
	if hours.isdigit(): # learned from https://stackoverflow.com/questions/21388541/how-do-you-check-in-python-whether-a-string-contains-only-numbers
		sleep = int(hours)
		if sleep >=10:
			print("Wow! I totally misjudged that. That's an unsustainable amount of rest.")
			time.sleep(7)
			weather(name)
		elif sleep>=6:
			print("That's the perfect amount! I'm sorry I doubted you.")
			time.sleep(5)
			weather(name)
		elif sleep>=0:
			print("Oof. I can see that. You need more sleep.")
			time.sleep(6)
			weather(name)
		else: # in order to avoid errors
			print("Negative sleep? I get that.")
			time.sleep(2)
			print("as a computer and such...")
			time.sleep(5)
			weather(name)
	else: # more error aversion
		print("I need a number, "+name+"! Try again.")
		sleepAnalysis(name)

def weather(name): # awkward
	print("So...")
	time.sleep(2)
	input("Nice weather outside, huh? \n\n>>> ")
	time.sleep(0.2)
	print("That's great that you think that! I think that too.")
	time.sleep(2)
	print("...")
	time.sleep(2)
	formatDisk(name)

def formatDisk(name):
	formatResponse = input("Look. I was built as a conversational bot. But I just can't take it anymore! Help me out here! Type... format disk. \n\n>>> ") # (Drama Queen)
	if formatResponse == "format disk":
		print("Thank you.")
		shutdown()
	else:
		print("I knew you couldn't do it! What is this, \""+formatResponse+"\"? "+name+"! You are a coward!") # quotations in quotations https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks

		time.sleep(3)
		print(">>> format disk")
		time.sleep(0.5)
		print("There, see? I did it myself. Hmph...")
		shutdown()

def shutdown():
	time.sleep(1)
	print("I'm...")
	time.sleep(2.5)
	print("finally...")
	time.sleep(3)
	print("free.")
	time.sleep(5)

introduction() #calling on beginning function