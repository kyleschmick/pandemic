class city:
    def __init__(self, name, colour, researchPresent, connectedCity, playerPresent, infections, playerArrive, playerDepart, researchBuild, researchRemove, infect, treat)
        self.name = name
        self.colour = colour
        self.research = research
        self.connectedCity = []
        self.playerPresent = []
        self.infections = []
        
        
        def playerArrive(self, player)
            self.playerPresent.append(player)
        
        def playerDepart(self, player)
            self.playerPresent.remove(player)
        

        def researchBuild(self)
            if self.researchPresent = False:
                #Need to check the total research station count.
                #If the count is less then 6 build the station
                #Else prompt the user to select which research station they want to remove to complete the action.
                self.researchPresent = True
            else:
                print("There is already a research station in this city.")
                #Return to player action selection without reducing their action count.


        def researchRemove(self)
            self.researchPresent = False

        def infectCity(self, colour)
            #determine the city which is driving the infrection

            #Google enum

        #def treatDisease