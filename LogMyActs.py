#!/usr/bin/python
#-*-coding:utf-8 -*
from tkinter import *
from datetime import datetime


# Ecriture des logs dans le fichier 

def writeFile(tech, client, action):
	"""
	Do not return anything. 
	Method that writes the data retrieved in the GUI into a file "MyActs.txt".
	"""
	now = datetime.now()
	date = now.strftime("%d/%m/%Y")
	time = now.strftime("%H:%M:%S")
	with open('MyActs.txt', 'a') as file:
		#file = open("./LogsMyACts.txt","w")
		file.write("\n\n\n###############################################\n")
		file.write("Technicien : "+tech+"\n")
		file.write("-----------------------------------------------\n")
		file.write("Client : "+client+"\n")
		file.write("-----------------------------------------------\n")
		file.write("Date : "+date+"\n")
		file.write("Heure : "+time+"\n")
		file.write("-----------------------------------------------\n")
		file.write("Action effectuée : "+action+"\n")
		file.write("###############################################\n")

def submitButton():
	"""
	Do not return anything. 
	Initializes the variables of each entry when pressing the "validate" button. 
	Calling the file writing function.
	"""
	tech_entry = tech_name.get()
	client_entry = client_name.get()
	action_entry = action_name.get()
	writeFile(tech_entry,client_entry,action_entry)

def closeWindow():
	"""
	Do not return anything. 
	Destroy the GUI window.
	"""
	gui.destroy()


# MAIN 
gui = Tk()
gui.title("LogsMyACts")
gui.geometry("600x170")
# Gets the requested values of the height and widht.
windowWidth = gui.winfo_reqwidth()
windowHeight = gui.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(gui.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(gui.winfo_screenheight()/2 - windowHeight/2)
 # Positions the window in the center of the page.
gui.geometry("+{}+{}".format(positionRight, positionDown))

##########################################################################################

techLabel = Label(gui, width=350, justify="left")
techLabel.pack()
techLabel.config(text=" Initiales technicien (quadrigramme) :")
techname = StringVar()
tech_name = Entry(gui, textvariable=techname,width=350)
tech_name.pack()
tech_name.bind('<Return>', (lambda event: submitButton()))
# Regex for good entry [A-Z]{4}

##########################################################################################

clientLabel = Label(gui, width=350, justify="left")
clientLabel.pack()
clientLabel.config(text="Nom du client :")
clientname = StringVar()
client_name = Entry(gui, textvariable=clientname,width=350)
client_name.pack()
client_name.bind('<Return>', (lambda event: submitButton()))

##########################################################################################

actionLabel = Label(gui, width=350, justify="left")
actionLabel.pack()
actionLabel.config(text="Action effectuée :")
actionname = StringVar()
action_name = Entry(gui, textvariable=actionname,width=350)
action_name.pack()
action_name.bind('<Return>', (lambda event: submitButton()))

##########################################################################################

submit_button = Button(text="Valider", width=350, command=submitButton)
submit_button.pack()
exit_button = Button(text="Quitter", width=350, command=closeWindow)
exit_button.pack()
gui.mainloop()

