# Pandemic The Game
# Programmed by ...ME!
# God have mercy on me.
import random
from classes.character import character
from classes.city import city


# Main:
def pandemic():
    # Call game setup
    gamesetup()
    

# Game setup function. 
def gamesetup():
    
    playercount = plrcount() #Prompt for number of players
    print ("You have selected", playercount, "players.")

    epidemiccardcount = ecardcount() #Prompt for number of Epidemic Cards
    print ("You have selected", epidemiccardcount, "Epidemic Cards.")
    
    characterlist = createcharlist() #Build character list
    playercharacterlist = random.sample(characterlist, playercount) #Randomly select player characters
    print("The player characters are:")
    for count in range (0,playercount):
        y = characterlist[count]
        print("Player", count+1, ":", y.name)
    
    # For Later Give the option of drawing again if you get a shitty character


    #Build and Randomize City Card List
    #Initialize Player City Card List
    #Distribute appropriate number of City Cards to each player
    #Split City Card list into (approximately equal parts
    #Distribute Epidemic Cards

    #Build and Randomize Infection Deck List
    #Setup infections
    return

#Get player count and validate
def plrcount():
    while True:
        try: 
            pcount = int(input("How many players are playing? (Between 2 and 4) "))
        except:
            print("Sorry, I didn't understand that. You must select between 2 and 4 players.")
            continue

        if pcount < 2 or pcount > 4:
            print("Sorry, you must select a number between 2 and 4.")
            continue
        else:
            break
    return pcount
    
def ecardcount():
    while True:
        try: 
            eccount = int(input("How many Epidemic Cards are playing? (Between 4 and 6) "))
        except:
            print("Sorry, I didn't understand that. You must select a number between 4 and 6.")
            continue
        if eccount < 4 or eccount > 6:
            print("Sorry, you must select a number between 4 and 6.")
            continue
        else:
            break
    return eccount

def createcharlist():
    
    charmedic = character("Medic", "Remove all cubes of a single colour when doing Treat Disease. Automatically remove cubes of cured diseases from the city you are in. ")
    charscientist = character("Scientist", "You only need 4 cards of the same colour to do the Discover a Cure action.")
    charresearcher = character("Researcher", "As an action, you may give (or a player can take) any City Card from you hand. You must both be in the same city. The card does not have to match the city you are in.")
    charquarantinespecialist = character("Quarantine Specialist", "Prevent disease cube placements (and outbreaks) in the city you are in and all adjacent cities.")
    charcontingencyplanner = character("Contingency Planner", "As an action, take ANY discarded Event card and store it. When you play the stored Event card, remove it from the game. LIMIT: 1 event card can be stored at a time.")
    charopsexpert = character("Operations Expert", "As an action, build a Research Station in the city you are in. Once per turn at a Research Station, you may spend and action and discard any City Card to move to any city.")
    chardispatcher = character("Dispatcher", "Move another player's pawn as if it were yours. As an action, move any pawn to a city with another pawn. Get permission before moving another player's pawn.")

    charlist = []
    charlist = [charmedic, charscientist, charresearcher, charquarantinespecialist, charcontingencyplanner, charopsexpert, chardispatcher]
    return(charlist)

def createcity():
    #def __init__(self, name, colour, research, adjacent1, adjacent2, adjacent3, adjacent4, adjacent5, player1, player2, player3, player4)
    cityAtlanta = citycard(Atlanta, blue, , )

pandemic()
