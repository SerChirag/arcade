#TicTacToe
from Tkinter import *
##################################################################################################
import random
class TTT:

    def __init__(self):
        self.grid = ["1","2","3","4","5","6","7","8","9"]
        self.ghanta = ["1","2","3","4","5","6","7","8","9"]
        self.a1=False
        self.b1=False
        self.e=9

        self.turn=0
        
        self.welcomeTTT()
        self.butt1.config(command=self.TTTgame)
        self.printgrid()
        
    def welcomeTTT(self):

        self.text2.insert(INSERT,"""
WELCOME TO THE WORLD OF TIC TAC TOE.
I am Z.I.O.N, the undefeted champion of TIC-TAC-TOE.
The rules of the game are simple:
    1.You are represented by "X" on the board.
    2.I am represented by "O".
    3.Your aim is to get three "X" horizontally,
      vertically or diagnolly.
    4.As you are the challenger, you
      get the first move.

And remember:
     "When you play the Game of Thrones,
     you win or you die. There is no middle ground."
        \n""")
            
        self.text2.insert(INSERT,"\nYOUR TURN. Enter a number from 1-9 : and then press OK ")

    def printgrid(self):
        self.text1.delete(0.0,END)
        self.text1.insert(INSERT,'\n')
        self.text1.insert(INSERT, ("\t|---|---|---|\n"))
        for i in range(3):
            self.text1.insert(INSERT, ("\t|"))
            for j in range(i*3,(i*3)+3):
                self.text1.insert(INSERT, (" "+self.grid[j]+" |"))
            self.text1.insert(INSERT,'\n')
            self.text1.insert(INSERT, ("\t|---|---|---|\n"))
        self.text1.insert(INSERT,'\n')


    def gif(self,a):
        mo=0
        for i in range(len(self.grid)):
            if self.grid[i]==a:
                return mo
            else:
                mo+=1

    def attack(self,a):
        #global self.grid
        if self.grid[0]==a and self.grid[1]==a and self.grid[2]!="X":

            self.ghanta.remove("3")
            self.grid[2]="O"
            
        elif self.grid[0]==a and self.grid[2]==a and self.grid[1]!="X":

            self.ghanta.remove("2")
            self.grid[1]="O"
            
        elif self.grid[2]==a and self.grid[1]==a and self.grid[0]!="X":

            self.ghanta.remove("1")
            self.grid[0]="O"
            
        elif self.grid[3]==a and self.grid[5]==a and self.grid[4]!="X":

            self.ghanta.remove("5")
            self.grid[4]="O"
            
        elif self.grid[5]==a and self.grid[4]==a and self.grid[3]!="X":

            self.ghanta.remove("4")
            self.grid[3]="O"
            
        elif self.grid[3]==a and self.grid[4]==a and self.grid[5]!="X":

            self.ghanta.remove("6")
            self.grid[5]="O"
            
        elif self.grid[6]==a and self.grid[7]==a and self.grid[8]!="X":

            self.ghanta.remove("9")
            self.grid[8]="O"
            
        elif self.grid[8]==a and self.grid[7]==a and self.grid[6]!="X":

            self.ghanta.remove("7")
            self.grid[6]="O"
            
        elif self.grid[8]==a and self.grid[6]==a and self.grid[7]!="X":

            self.ghanta.remove("8")
            self.grid[7]="O"
            
        elif self.grid[0]==a and self.grid[3]==a and self.grid[6]!="X":

            self.ghanta.remove("7")
            self.grid[6]="O"
            
        elif self.grid[0]==a and self.grid[6]==a and self.grid[3]!="X":
            self.ghanta.remove("4")
            self.grid[3]="O"
            
        elif self.grid[3]==a and self.grid[6]==a and self.grid[0]!="X":
            self.grid[0]="O"
            self.ghanta.remove("1")
        elif self.grid[1]==a and self.grid[4]==a and self.grid[7]!="X":
            self.ghanta.remove("8")
            self.grid[7]="O"
            
        elif self.grid[7]==a and self.grid[4]==a and self.grid[1]!="X":

            self.ghanta.remove("2")
            self.grid[1]="O"
            
        elif self.grid[7]==a and self.grid[1]==a and self.grid[4]!="X":

            self.ghanta.remove("5")
            self.grid[4]="O"
            
        elif self.grid[2]==a and self.grid[5]==a and self.grid[8]!="X":

            self.ghanta.remove("9")
            self.grid[8]="O"
            
        elif self.grid[8]==a and self.grid[2]==a and self.grid[5]!="X":

            self.ghanta.remove("6")
            self.grid[5]="O"
            
        elif self.grid[8]==a and self.grid[5]==a and self.grid[2]!="X":

            self.ghanta.remove("3")
            self.grid[2]="O"
            
        elif self.grid[0]==a and self.grid[4]==a and self.grid[8]!="X":
            self.ghanta.remove("9")
            self.grid[8]="O"
        elif self.grid[8]==a and self.grid[0]==a and self.grid[4]!="X":
            self.ghanta.remove("5")
            self.grid[4]="O"
        elif self.grid[8]==a and self.grid[4]==a and self.grid[0]!="X":
            self.grid[0]="O"
            self.ghanta.remove("1")
        elif self.grid[2]==a and self.grid[4]==a and self.grid[6]!="X":
            self.ghanta.remove("7")
            self.grid[6]="O"
        elif self.grid[6]==a and self.grid[4]==a and self.grid[2]!="X":
            self.ghanta.remove("3")
            self.grid[2]="O"
        elif self.grid[6]==a and self.grid[2]==a and self.grid[4]!="X":
            self.ghanta.remove("5")
            self.grid[4]="O"
        else:
            self.defence("X")


    def win(self,a):
        if self.grid[0]==a and self.grid[1]==a and self.grid[2]==a:
            return True
        elif self.grid[3]==a and self.grid[4]==a and self.grid[5]==a:
            return True
        elif self.grid[6]==a and self.grid[7]==a and self.grid[8]==a:
            return True
        elif self.grid[0]==a and self.grid[3]==a and self.grid[6]==a:
            return True
        elif self.grid[1]==a and self.grid[4]==a and self.grid[7]==a:
            return True
        elif self.grid[2]==a and self.grid[5]==a and self.grid[8]==a:
            return True
        elif self.grid[0]==a and self.grid[4]==a and self.grid[8]==a:
            return True
        elif self.grid[2]==a and self.grid[4]==a and self.grid[6]==a:
            return True
        else:
            return False
            


    def defence(self,a):
        #global self.grid
        if self.grid[0]==a and self.grid[1]==a and self.grid[2]!="O":
            self.ghanta.remove("3")
            self.grid[2]="O"
            
            
        elif self.grid[0]==a and self.grid[2]==a and self.grid[1]!="O":
            self.ghanta.remove("2")
            self.grid[1]="O"
            
        elif self.grid[2]==a and self.grid[1]==a and self.grid[0]!="O":
            self.ghanta.remove("1")
            self.grid[0]="O"
            
        elif self.grid[3]==a and self.grid[5]==a and self.grid[4]!="O":
            
            self.ghanta.remove("5")
            self.grid[4]="O"
            
        elif self.grid[5]==a and self.grid[4]==a and self.grid[3]!="O":
            
            self.ghanta.remove("4")
            self.grid[3]="O"
            
        elif self.grid[3]==a and self.grid[4]==a and self.grid[5]!="O":
            
            self.ghanta.remove("6")
            self.grid[5]="O"
            
        elif self.grid[6]==a and self.grid[7]==a and self.grid[8]!="O":
            
            self.ghanta.remove("9")
            self.grid[8]="O"
            
            
        elif self.grid[8]==a and self.grid[7]==a and self.grid[6]!="O":
            
            self.ghanta.remove("7")
            self.grid[6]="O"
            
        elif self.grid[8]==a and self.grid[6]==a and self.grid[7]!="O":
            
            self.ghanta.remove("8")
            self.grid[7]="O"
            
        elif self.grid[0]==a and self.grid[3]==a and self.grid[6]!="O":
            
            self.ghanta.remove("7")
            self.grid[6]="O"
            
        elif self.grid[0]==a and self.grid[6]==a and self.grid[3]!="O":
            
            self.ghanta.remove("4")
            self.grid[3]="O"
            
        elif self.grid[3]==a and self.grid[6]==a and self.grid[0]!="O":
            self.grid[0]="O"
            self.ghanta.remove("1")
        elif self.grid[1]==a and self.grid[4]==a and self.grid[7]!="O":
            print "TRUE"
            
            self.grid[7]="O"
            printgrid()
        elif self.grid[7]==a and self.grid[4]==a and self.grid[1]!="O":
            
            self.ghanta.remove("2")
            self.grid[1]="O"
            
        elif self.grid[7]==a and self.grid[1]==a and self.grid[4]!="O":
            
            self.ghanta.remove("5")
            self.grid[4]="O"
            
        elif self.grid[2]==a and self.grid[5]==a and self.grid[8]!="O":
            self.ghanta.remove("9")
            self.grid[8]="O"
            
        elif self.grid[8]==a and self.grid[2]==a and self.grid[5]!="O":
            self.ghanta.remove("6")
            self.grid[5]="O"
            
        elif self.grid[8]==a and self.grid[5]==a and self.grid[2]!="O":
            
            self.ghanta.remove("3")
            self.grid[2]="O"
            
        elif self.grid[0]==a and self.grid[4]==a and self.grid[8]!="O":
            
            self.ghanta.remove("9")
            self.grid[8]="O"
        elif self.grid[8]==a and self.grid[0]==a and self.grid[4]!="O":
            
            self.ghanta.remove("5")
            self.grid[4]="O"
        elif self.grid[8]==a and self.grid[4]==a and self.grid[0]!="O":
            
            self.grid[0]="O"
            self.ghanta.remove("1")
        elif self.grid[2]==a and self.grid[4]==a and self.grid[6]!="O":
            
            self.grid[6]="O"
            self.ghanta.remove("7")
            
        elif self.grid[6]==a and self.grid[4]==a and self.grid[2]!="O":
            
            self.ghanta.remove("3")
            self.grid[2]="O"
        elif self.grid[6]==a and self.grid[2]==a and self.grid[4]!="O":
            
            self.ghanta.remove("5")
            self.grid[4]="O"
        else:
            a=random.randint(0,len(self.ghanta)-1)
            f=self.ghanta[a]
            h=self.gif(f)
            self.grid[h]="O"
            self.ghanta.pop(a)
            

    def TTTgame(self):       
        
        if (self.a1==False and self.b1==False and self.e>0):
            #self.text1.delete(0.0,END)

            self.turn+=1

            self.text2.delete(0.0,END)
            
            c=self.entry1.get()
            if c in self.ghanta:
                d = int(c)
                self.grid[d-1]="X"
                self.ghanta.remove(c)
                self.a1=self.win("X")
                self.e-=1
                if self.a1 == True:
                    self.text2.insert(INSERT,"\nCONGRATULATION !!! YOU ARE NOW THE CHAMPION OF TIC-TAC-TOE. :) \nPress Quit to Exit")
                    
                elif self.e>0:            
                    self.text2.insert(INSERT,"\n Good move, but now its MY TURN....  ")
                    self.text2.insert(INSERT,"\nYOUR TURN. Enter a number from 1-9 : and then press OK ")
                    self.attack("O")
                    self.b1 = self.win("O")
                    if self.b1 == True:
                        self.text2.insert(INSERT,"\nHAHAHAHAHA!! I won. You thought you could so easily take MY THRONE?? \nPress Quit to Exit")
                        
                    self.e-=1
                else:
                    pass
            else:
                self.text2.insert(INSERT,"  WRONG MOVE !! TRY AGAIN .....")
                self.text2.insert(INSERT,"\nEnter a number from 1-9 : and then press OK ")

        if len(self.ghanta)==0:
            self.text2.insert(INSERT,"  MATCH draw. I still remains the undefeated CHAMPION. Try another time.\nPress Quit to Exit")
        
        
        self.printgrid()

