# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jeff Haberman
# Creation Date: 5-12-23
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
    #It appears as though there was an unexpected indent on the while statement. The indentation needs to be changed. 
    while cave != '1' and cave != '2':
      #while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
    #It appears as though caves is not a variable that is used. I believe it should be singular like below
    return cave
    #return caves

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
      #The print call was missing parenthesis. The correct code should look like this.
        print('Gobbles you down in one bite!')
        #print 'Gobbles you down in one bite!'
        

displayIntro()
#It appears as though the capitalization is incorrect. The command should look like this.
caveNumber = chooseCave()
#caveNumber = choosecave()
checkCave(caveNumber)

#Appears as though there is a typo in the final print command.
print("Thanks for playing")
#print("Thanks for planing")
