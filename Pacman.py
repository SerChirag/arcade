#Pacman
"""
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||          ||||          ||||         ||||    |||||||    ||||          ||||    |||||||  |||||
|||  ||||||  ||||  ||||||  ||||  |||||||||||  ||  ||  |||  ||||  ||||||  ||||  ||  |||||  |||||
|||  ||||||  ||||  ||||||  ||||  |||||||||||  ||||   ||||  ||||  ||||||  ||||  |||  ||||  |||||
|||          ||||          ||||  |||||||||||  ||||| |||||  ||||          ||||  |||||  ||  |||||
|||  ||||||||||||  ||||||  ||||  |||||||||||  |||||||||||  ||||  ||||||  ||||  |||||||    |||||
|||  ||||||||||||  ||||||  ||||         ||||  |||||||||||  ||||  ||||||  ||||  |||||||||  |||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
"""

"""Hello, Welcome to the Adventurous World of PACMAN.
The PACMAN agent is represented by letter 'C'.

YOUR MISSION, SHOULD YOU CHOOSE TO ACCEPT:

    1.Collect all coins on the M.A.Z.E represented by "."
    2.Each coin is worth 10 points.
    3.Do so in minimum number of moves. After the game is over, 1 point will be deducted for each move.
    4.Avoid the nasty G.H.O.S.T represented by numbers. They love to devour all who dare to explore the M.A.Z.E.


GOOD LUCK AGENT. MAY THE ODDS ALWAYS BE ON YOUR FAVOUR :) 
"""
import random
from Tkinter import *
###############################################################################################################################################
class Pacman:
    def __init__(self):
        self.coin=0
        self.move=0
        self.score=0
        self.grid=[]

        self.a=12
        self.b=12

        self.gridinit()
        

        self.ghost=[["1",14,23],["2",5,17],["3",21,13],["4",12,5],["5",14,13]]
        self.hi = ["1","2","3","4","5"]

        self.butt1.config(command=self.StartPac)

        self.text2.insert(INSERT,"""Hello, Welcome to the Adventurous World of PACMAN.
The PACMAN agent is represented by letter 'C'.

YOUR MISSION, SHOULD YOU CHOOSE TO ACCEPT:

    1.Collect all coins on the M.A.Z.E represented by "."
    2.Each coin is worth 10 points.
    3.Do so in minimum number of moves. After the game is over, 1 point will be deducted for each move.
    4.Avoid the nasty G.H.O.S.T represented by numbers. They love to devour all who dare to explore the M.A.Z.E.


GOOD LUCK AGENT. MAY THE ODDS ALWAYS BE ON YOUR FAVOUR :) 
""")                
        

    def gridinit(self):
        for i in range(25):
            
            for j in range(25):
                self.grid.append(".")
        for i in range(25,600,25):
            self.grid[i]="|"
            self.grid[i-1]= "|"

        for i in range(406,418):
            self.grid[i]="-"    
        for i in range(485,496):
            self.grid[i]="-"
        for i in range(334,346):
            self.grid[i]="-"
        for i in range(181,188):
            self.grid[i]="-"
        for i in range(253,268):
            self.grid[i]="-"
        for i in range(77,88):
            self.grid[i]="-"
        for i in range(153,456,25):
            self.grid[i]="|"
        for i in range(551,570):
            self.grid[i]="-"
        for i in range(95,477,25):
            self.grid[i]="|"
        for i in range(41,198,25):
            self.grid[i]="|"
        for i in range(331,498,25):
            self.grid[i]="|"
        for i in range(0,25):
            self.grid[i]="-"
        for i in range(600,625):
            self.grid[i]="-"
        self.grid[0]="X"
        self.grid[24]="X"
        self.grid[624]="X"
        self.grid[600]="X"

        self.setco((12,12),"C")
        self.setco((14,23),"1")
        self.setco((5,17),"2")
        self.setco((21,13),"3")
        self.setco((12,5),"4")
        self.setco((14,13),"5")
        self.pg()
        


    def getcoins(self):
        lo = 0
        for i in self.grid:
            if i == ".":
                lo +=1
        return 397-lo

    def pg(self):
        for i in range(0,625,25):
            for j in range(i,i+25):
                self.text1.insert(INSERT,self.grid[j])
            self.text1.insert(INSERT,"\n")
            

    def getco(self,(a,b)):
        return self.grid[((a*25)-1)+(b+1)]

    def setco(self,(a,b),new):
        self.grid[((a*25)-1)+(b+1)]=new
        return self.grid
        
    def up(self,(a,b),u): 
        if (self.getco((a-1,b)) == "-" or self.getco((a-1,b)) == "|"):
            return 0
        elif self.getco((a-1,b)) in self.hi:
              return None
        else:
            f = self.getco((a,b))
            self.setco((a-1,b),f)
            self.setco((a,b),u)
            return self.grid

    def down(self,(a,b),u):
        if (self.getco((a+1,b)) == "-" or self.getco((a+1,b)) == "|"):
            return 0
        elif self.getco((a+1,b)) in self.hi:
            return 1
        else:
            f = self.getco((a,b))
            self.setco((a+1,b),f)
            self.setco((a,b),u)
            return self.grid


    def right(self,(a,b),u):
        if (self.getco((a,b+1)) == "-" or self.getco((a,b+1)) == "|"):
            return 0
        elif self.getco((a,b+1)) in self.hi:
            return 1
        else:
            f = self.getco((a,b))
            self.setco((a,b+1),f)
            self.setco((a,b),u)
            return self.grid


    def left(self,(a,b),u):
        if (self.getco((a,b-1)) == "-" or self.getco((a,b-1)) == "|"):
            return 0
        elif self.getco((a,b-1)) in self.hi:
            return 1
        else:
            f = self.getco((a,b))
            self.setco((a,b-1),f)
            self.setco((a,b),u)
            return self.grid    

    def movement(self):
        
        for j in range(0,5):
            i = self.ghost[j]
            a = i[1]
            b = i[2]
            k = random.randint(1,4)
            if k==1:
                if (self.getco((a-1,b)) == "-" or self.getco((a-1,b)) == "|"):
                     pass
                else:
                    self.setco((a,b),".")
                    self.setco((a-1,b),i[0])
                    
                    a=a-1
                
            elif k==2:
                if (self.getco((a,b-1)) == "-" or self.getco((a,b-1)) == "|"):
                    pass
                else:
                    self.setco((a,b),".")
                    self.setco((a,b-1),i[0])
                    
                    b=b-1
            elif k==3:
                if (self.getco((a,b+1)) == "-" or self.getco((a,b+1)) == "|"):
                    pass
                else:
                    self.setco((a,b),".")
                    self.setco((a,b+1),i[0])
                    
                    b=b+1
            elif k==4:
                if (self.getco((a+1,b)) == "-" or self.getco((a+1,b)) == "|"):
                    pass
                else:
                    self.setco((a,b),".")
                    self.setco((a+1,b),i[0])
                    
                    a=a+1
            else:
                pass
            self.ghost[j][1]=a
            self.ghost[j][2]=b
            
        

    def StartPac(self):
        self.text1.delete(0.0,END)
        self.text2.delete(0.0,END)
        
        #flag =0

        if ("." in self.grid):

            self.coins = self.getcoins()
            self.score = (self.coins*10) - self.move

            
            self.text2.insert(INSERT,"\nCONTROL MANUAL:                      wSCOREBOARD:")
            self.text2.insert(INSERT,"\nw for moving self.up                Number of Moves: "+str(self.move))
            self.text2.insert(INSERT,"\na for moving self.left              Number of self.coins: "+str(self.coins))
            self.text2.insert(INSERT,"\nd for moving self.right             Total Score: "+str(self.score))
            self.text2.insert(INSERT,"\ns for moving self.down ")
            self.text2.insert(INSERT,"\nq for quit")
            
            
            
            p =self.entry1.get()
            
            p=p.upper()
            if p=="W":
                self.move +=1
                f=self.up((self.a,self.b)," ")
                if f==0:
                    self.text2.insert(INSERT,"\nWALL CRASH !!!")
                    self.pg()
                elif f==1:
                    self.text2.insert(INSERT,"\nYOU HAVE BECOME G.H.O.S.T SNACK ")
                    #break            
                else:
                    self.pg()
                    self.a-=1
                    
            elif p=="A":
                self.move +=1
                f=self.left((self.a,self.b)," ")
                if f==0:
                    self.text2.insert(INSERT,"\nWALL CRASH !!!")
                    
                    self.pg()
                elif f==1:
                    self.text2.insert(INSERT,"\nYOU HAVE BECOME G.H.O.S.T SNACK ")
                    #break
                else:
                    self.pg()
                    self.b-=1
            

            elif p=="D":
                self.move +=1
                f=self.right((self.a,self.b)," ")
                if f==0:
                    self.text2.insert(INSERT,"\nWALL CRASH !!!")
                    self.pg()
                elif f==1:
                    self.text2.insert(INSERT,"\nYOU HAVE BECOME G.H.O.S.T SNACK ")
                    #break
                else:
                    self.pg()
                    self.b+=1
                    

            elif p=="S":
                self.move +=1
                f=self.down((self.a,self.b)," ")
                if f==0:
                    self.text2.insert(INSERT,"\nWALL CRASH !!!")
                    self.pg()
                elif f==1:
                    self.text2.insert(INSERT,"\nYOU HAVE BECOME G.H.O.S.T SNACK ")
                    #break
                else:
                    self.pg()
                    self.a+=1
            elif p=="Q":
                self.text2.insert(INSERT,"\nYou have chosen to quit")
                self.text2.insert(INSERT,"\nRetreiving agent ............")
                
                #break
            else:
                self.text2.insert(INSERT,"\nWrong Input !! ")
            self.movement()
        else:
            

            
            self.text2.insert(INSERT,"\nPREPARING ASSEMENT .............")
            self.text2.insert(INSERT,"\n\nNumber of Moves: "+self.move)
            self.text2.insert(INSERT,"\nNumber of self.coins: "+self.coins)
            self.text2.insert(INSERT,"Total Score: "+self.score)
            


