#This file will be used to handle loading data from text file 
import sys
import csv
import fileinput

#Function loads the data from text file
#For now can only handle loading one saved game.  May add filename as parameter if needed.
def load_game():
	"""Loads game"""
	with open("output.txt") as text_file:
		line = text_file.read()
		text_list = line.split(',')

	    #FOR TESTING ONLY
	    #print(text_list)

#For testing only
'''
def main():
	load_game()

if __name__ == "__main__":
    main()
'''

