#This file will be used to handle saving/writing data to text file
import sys
import csv
import fileinput

#Function takes the following as parameters and writes to text file in comma delimited string:
#1.  Character name
#2.  Current room
#3.  Inventory (list of items)
#For now can only handle saving one game.  Each call to method overwrites text file in directory.
#Will update once we have more details of data files
def saveGame(characterName, currentRoom, inventoryList):
	with open("output.txt", "w") as text_file:
		text_file.write(characterName + ',')
		text_file.write(currentRoom + ',')
		text_file.write(','.join(str(i) for i in inventoryList))

#FOR TESTING ONLY
'''
def main():
	inventList = ['sword', 'torch', 'bow']
	charName = 'Zelda'
	currRoom = 'Dungeon_Entrance'
    saveGame(charName, currRoom, inventList)


if __name__ == "__main__":
    main()
'''
