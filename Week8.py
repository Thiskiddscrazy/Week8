""" "Assignment 8.1 has you writing a Python program that has you
   interacting with the file system (directories and files)". """

#The first thing we must do is import os which begins the validation protocol of files / directories.

import os

def main():
	"""Defines our main function which defines the directory and file name through user input while
	also creating a directory if one does not already exist."""

	callDirectory = input("Enter the name of your directory: ")

	if not os.path.exists(callDirectory): #If the directory is not found, print (see below), then:
		print("Directory does not exist!")
		os.mkdir #This command tells Python to create the directory 
		print("\nCreating directory, please wait...")
	
	fileName = input("Enter file name:")
	#Tried this way, and it wrote to the file, but keep getting error on line #26- FileNotFoundError
	#fileName = 'Homework.txt'
	#with open (fileName, 'w') as filehandle:
	#	filehandle.write ("This way very difficult to compose!!")
	#os.path.join(callDirectory, fileName) found this but doesn't seem to do anything either.
	
	f = open(callDirectory+'/'+fileName, 'w')#Creating a file using the 'write mode', 'w',in the directory.
	
	"""Borrowed the 'f = open' code algorythm from user ASAD HAMEED via:
	https://stackoverflow.com/questions/59487696/check-if-a-folder-exists-
	in-a-given-path-and-if-not-then-create-a-folder-there"""
	
	Name, Address, Phone = input("Enter name, Address, and Phone number, separated by a comma: ").split(',')
	f.write(Name + ',' + Address + ',' + Phone + '\n')
	f.close()	#Used to close the file when not using 'with'

#---------------------------------------------------------------------------------------#
	f = open(callDirectory+'/'+fileName, 'r')	#Opening the created file now using read mode , 'r'.


	(Name, Address, Phone) = f.read().split(',')	#Reading user input of created file.
#Printing / entering user info for validation purposes ------
	print("Displaying user info... ")
	print("Name: ",Name)
	print("Address: ",Address)
	print("Phone number: ",Phone)
	f.close()	#close the file

if __name__ == "__main__": # Calls our function
	main()

#Also used https://docs.python.org/3/tutorial/inputoutput.html