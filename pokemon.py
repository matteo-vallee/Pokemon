import json
import random

with open('json/infopoke.json', encoding="utf8") as Json_file:
  data = json.load(Json_file)

with open('json/Nature.json', encoding="utf8") as Nature_file:
  datanature = json.load(Nature_file)

with open('json/Move.json', encoding="utf8") as Json_Movefile:
  Movedata = json.load(Json_Movefile)

class Pokemon():
    
    def __init__(self):
      self.gamestate = True
      self.name = None
      self.type = None
      self.HP = 0
      self.Attack = 0
      self.Defense = 0
      self.AttackSPE = 0
      self.DefenseSPE = 0
      self.Speed = 0
      self.Lvl= 0
      self.ivHP = random.randint(0,31)
      self.ivAttack = random.randint(0,31)
      self.ivDefense = random.randint(0,31)
      self.ivAttackSPE = random.randint(0,31)
      self.ivDefenseSPE = random.randint(0,31)
      self.ivSpeed = random.randint(0,31)
      self.Nature = random.choice([i for i in datanature])
      self.HPlvl =0
      self.Attacklvl = 0
      self.Defenselvl = 0
      self.AttackSPElvl = 0
      self.Defenselvl = 0
      self.Speedlvl = 0
      self.Move =None
      self.Movetype = None
      self.Movecategory = None
      self.Movepower = None



    def returninfo(self):
        return print(f"Name : {self.name}\n"
                     f"Lvl : {self.Lvl}\n"
                     f"Nature : {self.Nature}\n"
                     f"Type : {self.type}\n"
                     f"Base HP : {int(self.HPlvl)}\n"
                     f"Base attack : {int(self.Attacklvl)}\n"
                     f"Base defense : {int(self.Defenselvl)}\n"
                     f"Base attack spe : {int(self.AttackSPElvl)}\n"
                     f"Base defense spe: {int(self.Defenselvl)}\n"
                     f"Base Speed: {int(self.Speedlvl)}"
                     )

    def lvlstatready(self):
        self.HPlvl += (((2 * self.HP + self.ivHP + (30 / 4)) * self.Lvl) / 100) + self.Lvl + 10
        self.Attacklvl += ((((2*self.Attack+self.ivAttack+(30/4))*self.Lvl)/100)+5)*datanature[self.Nature]["Attack"]
        self.Defenselvl += ((((2*self.Defense+self.ivDefense+(30/4))*self.Lvl)/100)+5)*datanature[self.Nature]["Defense"]
        self.AttackSPElvl += ((((2*self.AttackSPE+self.ivAttackSPE+(30/4))*self.Lvl)/100)+5)*datanature[self.Nature]["AttackSPE"]
        self.Defenselvl += ((((2*self.DefenseSPE+self.ivDefenseSPE+(30/4))*self.Lvl)/100)+5)*datanature[self.Nature]["DefenseSPE"]
        self.Speedlvl += ((((2*self.Speed+self.ivSpeed+(30/4))*self.Lvl)/100)+5)*datanature[self.Nature]["Speed"]

    def createpokemon(self,nameobj,valeur,lvlpok):
        nameobj = Pokemon()
        nameobj.id = int(valeur) - 1
        nameobj.Lvl = lvlpok
        nameobj.name = data[nameobj.id]["name"][langage]
        nameobj.type = data[nameobj.id]["type"]
        nameobj.HP = data[nameobj.id]["base"]["HP"]
        nameobj.Attack = data[nameobj.id]["base"]["Attack"]
        nameobj.Defense = data[nameobj.id]["base"]["Defense"]
        nameobj.AttackSPE = data[nameobj.id]["base"]["Sp. Attack"]
        nameobj.DefenseSPE = data[nameobj.id]["base"]["Sp. Defense"]
        nameobj.Speed = data[nameobj.id]["base"]["Speed"]
        nameobj.Move = random.choice([i for i in Movedata]),random.choice([i for i in Movedata]),random.choice([i for i in Movedata]),random.choice([i for i in Movedata])
        nameobj.lvlstatready()
        return nameobj



langage = "english"

"""pokemon1 = Pokemon(112,53)
print(pokemon1.Movetype)
print(pokemon1.Movepower)
print(pokemon1.Movecategory)"""