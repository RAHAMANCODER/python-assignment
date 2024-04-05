from tabulate import tabulate
class Match:
     def __init__(self,venue,date,time,TEAM_1,TEAM_2):
          self.venue=venue
          self.date=date
          self.time=time
          self.TEAM_1=TEAM_1
          self.TEAM_2=TEAM_2
          
     def Match_info(self):
           return f"venue:{self.venue}\ndate:{self.date}\ntime:{self.time}\nTEAM_1:{self.TEAM_1}\nTEAM_2:{self.TEAM_2}\n "      
     
     
class Player:   
     def __init__(self):
           self.players=[]
          
     def add_player(self,player): 
         self.players.append(player) 
         
     def list_(self,team):
         print('TEAM_',team )
         for list_1 in self.players:
              print(list_1)
   
class Score():
     def __init__(self,TEAM_1_SCORE,TEAM_2_SCORE):
           self.TEAM_1_SCORE=TEAM_1_SCORE
           self.TEAM_2_SCORE=TEAM_2_SCORE
           
     def print_3(self):
          return f"TEAM_1_SCORE:{self.TEAM_1_SCORE}\nTEAM_2_SCORE:{self.TEAM_2_SCORE}\n"
     
     def man_ofthe_match(self,name):
          return f"MAN_OF_THE_MATCH:{name} was awared the man of the match for all-round perforance taking the 3 wickets, 2 catches and scored 40 runs in 18 balls\n"
          
     def match_summary(self): 
          if self.TEAM_1_SCORE>self.TEAM_2_SCORE:
               return f"MATCH_SUMMARY:\nPyhton attackers win the match: {self.TEAM_1_SCORE}"
          elif self.TEAM_1_SCORE<self.TEAM_2_SCORE:
               return f"CSK win the match {self.TEAM_2_SCORE}"
          else:
               print("match is tie")
               
            
class NextMatch:
           def __init__(self,venue,date,time,TEAM_1,TEAM_2):
              self.venue=venue
              self.date=date
              self.time=time
              self.TEAM_1=TEAM_1
              self.TEAM_2=TEAM_2
          
           def Match_info(self):
                 return f"NEXT_MATCH\nvenue:{self.venue}\ndate:{self.date}\ntime:{self.time}\nTEAM_1:{self.TEAM_1}\nTEAM_2:{self.TEAM_2}\n "       
   
               
               
                           
Team_1=Match("Amcet_Ground","01-04-2024","10.00 AM\n","PYTHON_ATTACKER","CHENNAI_SUPER_KINGS")
print(Team_1.Match_info()) 

play=Player()
play.add_player("1.Rahaman/BATSMAN(c)")
play.add_player("2.Dinesh/SPINNER(VC)")
play.add_player("3.Praveen/ALLROUNDER")
play.add_player("4.Pavan/BOWLER")
play.add_player("5.Hari/KEEPER")
play.add_player("6.Jeeva/ALLROUNDER")
play.add_player("7.Dhanush/BATSMAN\n ")
play.list_(1)
team_2=Player()
team_2.add_player("1.Dhoni/KEEPER")
team_2.add_player("2.Ruturaj/BATSMAN(C)")
team_2.add_player("3.Sachin/BATSMAN")
team_2.add_player("4.Pathirana/BOWLER")
team_2.add_player("5.Jadeja/SPINNER(VC)")
team_2.add_player("6.Mithcel/ALLROUNDER")
team_2.add_player("7.Dube/ALLROUNDER\n")
team_2.list_(2)
scores=Score(180,170)
print(scores.print_3())
print(scores.man_ofthe_match('\nDinesh'))
print(scores.match_summary())
print("\n")
print("python_attacker_score card")

def score():
        data=[
               ["Rahman" , "60" , "40","150","padirana(b)_dhoni(c)"],
               ["praveen" ,"55" ,"30","170","jadeja_runout"],
               ["jeeva" , "30" ,"20","145","mitchel_(b)"],
               ["dinesh", "40","30","145","jadeja_runout"]
          ]
                                     
        head=["NAME","RUNS","BALLS" ,"S/R","WICKET"]
        return tabulate(data,head)
table=score() 
print(table)
print("\n")
print("CSK_score card")

def score_1():
   data=[
               ["ruturaj" , "60" , "40","150","rahaman(b)_praveen(c)"],
               ["dhoni" ,"55" ,"30","170","dinesh"],
               ["jadeja" , "30" ,"20","145","dhanush_(b)"],
               ["sachin", "40","30","145","dinesh"]
          ]
   head=["NAME","RUNS","BALLS" ,"S/R","WICKET"]
   return tabulate(data,head)
table_1=score_1() 
print(table_1)
nextmatch=NextMatch("bengalore","15-04-2024","10.00 AM","PYTHON_ATTACKER","RCB")
print(nextmatch.Match_info())

"""
venue:Amcet_Ground
date:01-04-2024
time:10.00 AM

TEAM_1:PYTHON_ATTACKER
TEAM_2:CHENNAI_SUPER_KINGS

TEAM_ 1
1.Rahaman/BATSMAN(c)
2.Dinesh/SPINNER(VC)
3.Praveen/ALLROUNDER
4.Pavan/BOWLER
5.Hari/KEEPER
6.Jeeva/ALLROUNDER
7.Dhanush/BATSMAN

TEAM_ 2
1.Dhoni/KEEPER
2.Ruturaj/BATSMAN(C)
3.Sachin/BATSMAN
4.Pathirana/BOWLER
5.Jadeja/SPINNER(VC)
6.Mithcel/ALLROUNDER
7.Dube/ALLROUNDER

TEAM_1_SCORE:180
TEAM_2_SCORE:170

MAN_OF_THE_MATCH:
Dinesh was awared the man of the match for all-round perforance taking the 3 wickets, 2 catches and scored 40 runs in
 18 balls

MATCH_SUMMARY:
Pyhton attackers win the match: 180


python_attacker_score card
NAME       RUNS    BALLS    S/R  WICKET
-------  ------  -------  -----  --------------------
Rahman       60       40    150  padirana(b)_dhoni(c)
praveen      55       30    170  jadeja_runout
jeeva        30       20    145  mitchel_(b)
dinesh       40       30    145  jadeja_runout


CSK_score card
NAME       RUNS    BALLS    S/R  WICKET
-------  ------  -------  -----  ---------------------
ruturaj      60       40    150  rahaman(b)_praveen(c)
dhoni        55       30    170  dinesh
jadeja       30       20    145  dhanush_(b)
sachin       40       30    145  dinesh

NEXT_MATCH
venue:bengalore
date:15-04-2024
time:10.00 AM
TEAM_1:PYTHON_ATTACKER
TEAM_2:RCB
"""
        
