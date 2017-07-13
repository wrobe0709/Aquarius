#This file will be used to handle loading data from text file 
import sys
import csv
import fileinput

#Function loads the data from text file
#For now can only handle loading one saved game.  May add filename as parameter if needed.
def loadGame():
	with open("output.txt") as text_file:
	    line = text_file.read()
	    textList = line.split(',')

	    #FOR TESTING ONLY
	    #print(textList)

#For testing only
'''
def main():
	loadGame()

if __name__ == "__main__":
    main()
'''

