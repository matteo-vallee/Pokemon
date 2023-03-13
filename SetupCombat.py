
class SetupFight():

    def __init__(self):
        self.poketeam =[]
        self.poketeamactif = []
        self.team = 0

    def createteam1(self,object_team1):
        object_team1 = SetupFight()
        object_team1.team = 1
        return object_team1


    def initilizeteam1(self, newpoke1,object_team1):
        if object_team1.team <= 6:
            object_team1.poketeam.append(newpoke1)
            object_team1.team += 1

        else:
            pass

    def createteam2(self,objectteam2):
        object_team2 = SetupFight()
        object_team2.team = 1
        return object_team2

    def initilizeteam2(self,newpoke2,objectteam2):
        if  objectteam2.team < 6:
            objectteam2.poketeam.append(newpoke2)
            objectteam2.team += 1
        else:
            pass


    def removepoket1(self,listepoke,poke):
            listepoke.poketeam.remove(poke)

    def removepoket2(self,listepoke,poke):
            listepoke.poketeam.remove(poke)

    def initialisefirstpoke(self,team):
            team.poketeamactif = team.poketeam[0]







