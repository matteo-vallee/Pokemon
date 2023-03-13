from pokemon import Pokemon
from SetupCombat import SetupFight
import json
import math
import random

with open('json/type.json', encoding="utf8") as Jsontype_file:
  Typedata = json.load(Jsontype_file)

class Fight():

    def super__init__(self):
        pass


    def attackglopoketeam1(self,team1,team2):
        print("Which Attack do you want to do ?")
        for i in range(0, len(team1.poketeamactif.Move)):
            print(str(i + 1) + ". " + team1.poketeamactif.Move[i]["name"]+". "+team1.poketeamactif.Move[i]["type"])
        choiceA = int(input())-1
        effectiveness = 1
        if  choiceA < 4 and choiceA >= 0 :

            team1.poketeamactif.Movetype = team1.poketeamactif.Move[choiceA]["type"]
            team1.poketeamactif.Movecategory = team1.poketeamactif.Move[choiceA]["category"]
            team1.poketeamactif.Movepower = team1.poketeamactif.Move[choiceA]["power"]


            for ty in team2.poketeamactif.type:

                effectiveness *= Typedata[team1.poketeamactif.Movetype][ty]
                print(effectiveness)
            if team1.poketeamactif.Movecategory == "physical":
                return int(math.floor(((((((
                                                   2 * team1.poketeamactif.Lvl / 5) + 2) * team1.poketeamactif.Attacklvl * team1.poketeamactif.Movepower / team2.poketeamactif.Defense) / 50 + 2) * effectiveness) * random.randint(
                    217, 255)) / 255))  # physical attack
            elif team1.poketeamactif.Movecategory == "special":
                return int(math.floor(((((((
                                                   2 * team1.poketeamactif.Lvl / 5) + 2) * team1.poketeamactif.AttackSPE * team1.poketeamactif.Movepower / team2.poketeamactif.DefenseSPE) / 50 + 2) * effectiveness) * random.randint(
                    217, 255)) / 255))  # special attack
            else:
                return 0
        print("Invalid choice")
        self.attackglopoketeam1(team1,team2)



    def attackglopoketeam2(self,team1,team2):
        print("Which Attack do you want to do ?")
        for i in range(len(team2.poketeamactif.Move)):
            print(str(i + 1) + ". " + team2.poketeamactif.Move[i]["name"]+". "+team2.poketeamactif.Move[i]["type"])
        choiceA = int(input()) - 1
        effectiveness = 1

        if choiceA < 4 and choiceA >= 0:

            team2.poketeamactif.Movetype = team2.poketeamactif.Move[choiceA]["type"]
            team2.poketeamactif.Movecategory = team2.poketeamactif.Move[choiceA]["category"]
            team2.poketeamactif.Movepower = team2.poketeamactif.Move[choiceA]["power"]

            for ty in team1.poketeamactif.type:
                effectiveness *= Typedata[team2.poketeamactif.Movetype][ty]
                print(effectiveness)
            if team2.poketeamactif.Movecategory == "physical":
                return int(math.floor(((((((2 * team2.poketeamactif.Lvl / 5) + 2) * team2.poketeamactif.Attacklvl * team2.poketeamactif.Movepower / team1.poketeamactif.Defense) / 50 + 2) * effectiveness) * random.randint(217, 255)) / 255))  # physical attack

            elif team1.poketeamactif.Movecategory == "special":
                return int(math.floor(((((((2 * team2.poketeamactif.Lvl / 5) + 2) * team2.poketeamactif.AttackSPE * team2.poketeamactif.Movepower / team1.poketeamactif.DefenseSPE) / 50 + 2) * effectiveness) * random.randint(217, 255)) / 255))  # special attack
            else:
                return 0
        print("Invalid choice")
        self.attackglopoketeam2(team1,team2)




    def switch_pokemonteam1(self,team1):

        print("Which pokemon do you want to switch ?")
        for i in range(len(team1.poketeam)):
            print(team1.poketeam[i].name)
        choice = input("")

        # Check if the choice is valid
        if choice.isdigit() and 0 < int(choice) <= len(team1.poketeam) and  team1.poketeamactif != team1.poketeam[int(choice)-1]:
            team1.poketeamactif = team1.poketeam[int(choice)-1]
            print("You switch to " + team1.poketeamactif.name)
        else:
            print("Invalid choice")
            self.switch_pokemonteam1(team1)

    def switch_pokemonteam2(self,team2):

        print("Which pokemon do you want to switch ?")
        for i in range(len(team2.poketeam)):
            print(team2.poketeam[i].name)
        choice = input("")

        # Check if the choice is valid
        if choice.isdigit() and 0 < int(choice) <= len(team2.poketeam) and  team2.poketeamactif != team2.poketeam[int(choice)-1]:
            team2.poketeamactif = team2.poketeam[int(choice)-1]
            print("You switch to " + team2.poketeamactif.name)
        else:
            print("Invalid choice")
            self.switch_pokemonteam2(team2)

    def turnBCL(self,team1,team2,attackfirst,state):

        if attackfirst == "team2.poketeamactif"and state ==True:
            print("Team2")
            print("What do you want to do ?")
            print("1. Attack")
            print("2. Switch")
            choice = input("")


            if choice == "1":
                damage = self.attackglopoketeam2(team1,team2)
                print(team2.poketeamactif.name + " use " + team2.poketeamactif.Move[int(choice) - 1]["name"] + " and deal " + str(damage) + " damage")
                self.take_damageteam1(damage,team1)
                print(team1.poketeamactif.name + " have " + str(team1.poketeamactif.HPlvl) + " hp left")

            elif choice == "2":
                self.switch_pokemonteam2(team2)

            if team1.poketeamactif.HPlvl >0:
                if attackfirst == "team1.poketeamactif" and state ==True:
                    attackfirst = "team2.poketeamactif"
                if attackfirst == "team2.poketeamactif" and state ==True:
                    attackfirst = "team1.poketeamactif"
                print(attackfirst)
                self.turnBCL(team1, team2, attackfirst,state)
            else:
                print("Team 2 WIIIINNNN")
                state = False
                self.turnBCL(team1, team2, attackfirst, state)




        if attackfirst == "team1.poketeamactif"and state ==True:
            print("Team1")
            print("What do you want to do ?")
            print("1. Attack")
            print("2. Switch")
            choice = input("")

            if choice == "1":
                damage = self.attackglopoketeam1(team1,team2)
                print(team1.poketeamactif.name + " use " + team1.poketeamactif.Move[int(choice) - 1][
                    "name"] + " and deal " + str(damage) + " damage")
                self.take_damageteam2(damage, team2)
                print(team2.poketeamactif.name + " have " + str(team2.poketeamactif.HPlvl) + " hp left")



            elif choice == "2":
                self.switch_pokemonteam1(team1)

            if team2.poketeamactif.HPlvl > 0:
                if attackfirst == "team2.poketeamactif"and state ==True:
                    attackfirst = "team1.poketeamactif"
                if attackfirst == "team1.poketeamactif" and state == True:
                    attackfirst = "team2.poketeamactif"
                print(attackfirst)
                self.turnBCL(team1,team2,attackfirst,state)
            else:
                print("Team 1 WIIIINNNN")
                state = False
                self.turnBCL(team1, team2, attackfirst, state)



    def checkttackfirst(self,team1,team2):
            if team1.poketeamactif.Speedlvl > team2.poketeamactif.Speedlvl:
                return "team1.poketeamactif"
            elif team1.poketeamactif.Speedlvl < team2.poketeamactif.Speedlvl :
                return "team2.poketeamactif"
            else:
                return random.choice(["team1.poketeamactif", "team2.poketeamactif"])


    def take_damageteam1(self, damage,team1):
        team1.poketeamactif.HPlvl -= damage
        if team1.poketeamactif.HPlvl <= 0:
            team1.poketeamactif.HPlvl = 0

        else:
            team1.poketeamactif.HPlvl -= damage



    def take_damageteam2(self, damage,team2):
        if team2.poketeamactif.HPlvl <= 0:
            team2.poketeamactif.HPlvl = 0

        else:
            team2.poketeamactif.HPlvl -= damage





    def alivet2(self,team2):
        return team2.poketeamactif.HPlvl > 0

    def alivet1(self,team1):
        return team1.poketeamactif.HPlvl > 0

    def startfigh(self,namecombat):
        namecombat = Fight()
