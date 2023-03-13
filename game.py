from Combat import Fight
from pokemon import Pokemon
from SetupCombat import SetupFight


class Game(Pokemon,SetupFight,Fight):

    def super__init__(self):
        pass

    def gameBCL(self):

        while self.gamestate == True :
            print("Enter the name of the first team")
            objectteam1 = input()
            print("Enter the number of pokemon for team 1 that you want ( Max 6)")
            choicepokemont1 = int(input())
            team1 = self.createteam1(objectteam1)

            while choicepokemont1 > 0 :
                print("Enter the name for the object_pokemon")
                nameobj = input()
                print("Enter the pokemon id")
                valeur = input()
                print("Enter the name lvl")
                lvlpoke = int(input())

                self.initilizeteam1(self.createpokemon(nameobj,valeur,lvlpoke), team1)
                self.initialisefirstpoke(team1)
                print(team1.poketeam)
                choicepokemont1 -= 1

            print("Enter the name of the second team")
            objectteam2 = input()
            print("Enter the number of pokemon for team 2 that you want ( Max 6)")
            choicepokemont2 = int(input())
            team2 = self.createteam2(objectteam2)
            while choicepokemont2 > 0:
                print("Enter the name for the pokemon")
                nameobj2 = input()
                print("Enter the pokemon id")
                valeur2 = input()
                print("Enter the name lvl")
                lvlpoke2 = int(input())
                self.initilizeteam1(self.createpokemon(nameobj2, valeur2, lvlpoke2), team2)
                self.initialisefirstpoke(team2)
                choicepokemont2 -= 1

            print("Do you want to remove some pokemon from the first team ? (yes or no)")
            choiceremove = input()
            if choiceremove == "yes":
                print("how many ?")
                removenumber = int(input())
                while removenumber >= 0 :
                    print("witch object pokemon ?")
                    for i in range(len(team1.poketeam)):
                        print(team1.poketeam[i]["name"])
                    object_pokemon = input()
                    team1.removepoket1(team1,object_pokemon)
            else:
                pass

            print("Do you want to remove some pokemon from the second team ? (yes or no)")
            choiceremove2 = input()
            if choiceremove2 == "yes":
                print("how many ?")
                removenumber2 = int(input())
                while removenumber2 >= 0:
                    print("witch object pokemon ?")
                    for i in range(len(team2.poketeam)):
                        print(team2.poketeam[i]["name"])
                    object_pokemon2 = input()
                    team1.removepoket1(team2, object_pokemon2)
            else:
                pass
            print("FIIIIIGHHHTTT!!")
            state = self.state = True
            self.turnBCL(team1,team2,self.checkttackfirst(team1, team2),state)




    def createteam1(self, objectteam1):
        team1 = SetupFight()
        return team1

    def createteam2(self, objectteam2):
        team2 = SetupFight()
        return team2

game1 = Game()
game1.gameBCL()