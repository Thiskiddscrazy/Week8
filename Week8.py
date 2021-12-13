""" "Assignment 8.1 has you writing a Python program that has you
   interacting with the file system (directories and files)". """

#The first thing we must do is import os which begins the validation protocol of files / directories.

import os

def main():
	"""Defines our main function which defines the directory and file name through user input while
	also creating a directory if one does not already exist."""
	callDirectory = input("Enter the name of your directory: ") #Calls the directory (if found)
	if not os.path.isdir: #If the directory is not found, print (see below), then:
		print("Directory does not exist!")
		os.makedirs #This command tells Python to create the directory 
		print("\nCreating directory, please wait...")
	
	filename = input("Enter file name:")
	
	f = open(callDirectory+'/'+filename, 'w')#Creating a file using the 'write mode', 'w',in the directory.
	#Borrowed the 'f = open' code algorythm from user ASAD HAMEED via:
	#https://stackoverflow.com/questions/59487696/
	#check-if-a-folder-exists-in-a-given-path-and-if-not-then-create-a-folder-there

	Name = input ("Enter name: ").split(',')
	Address = input ("Enter address: ").split(',') 
	Phone = input ("Input phone number: ").split(',')
	f.write(Name.strip() + ',' + Address.strip() + ',' + Phone.strip() + '\n')

	f.close()	#Used to close the file when not using 'with'

#---------------------------------------------------------------------------------------#
	f = open(callDirectory+'/'+filename, 'r')	#Opening the created file now using read mode , 'r'.


	(Name, Address, Phone) = f.read().split(',')	#Reading user input of created file.
#Printing / entering user info for validation purposes ------
	print("Displaying user info... ")
	print("Name: ",Name)
	print("Address: ",Address)
	print("Phone number: ",Phone)
	f.close()	#close the file

if __name__ == "__main__": # Calls our function
	main()