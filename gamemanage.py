from battleship import*
from TicTacToe import*
from Pacman import*

from Tkinter import*
class gamemanage(TTT,Pacman,Battleship):
    

    def startTTT(self):
        self.gamescr()
        self.label2.config(text="Tic Tac Toe") 
        self.Frame3.destroy()
        self.butt2.config(command=self.tttquit)
        TTT.__init__(self)#TTT game will start and got to TTT code

    def tttquit(self):
        self.TTT_score=self.turn
        
        self.cur_obj.tttlist.append(self.TTT_score)
        
        self.choosegame()
        self.Frame2.destroy()
        
        

    def startPACMAN(self):
        self.gamescr()
        self.label2.config(text="PACMAN")
        self.Frame3.destroy()
        self.butt2.config(command=self.pacquit)
        Pacman.__init__(self)

    def pacquit(self):
        self.pac_score=self.score
        
        self.cur_obj.paclist.append(self.pac_score)

        
        self.choosegame()
        self.Frame2.destroy()
        

    def startBattleship(self):
        
        self.battleshipscr()
        self.Frame3.destroy()
        Battleship.__init__(self)

    def bsquit(self):
        u=5-len(self.userfragment)
        c=5-len(self.compfragment)
        self.bs_score=(10*c)-(2*u)

        self.cur_obj.bshiplist.append(self.bs_score)

        self.choosegame()
        self.Frameship.destroy()
        

    def battleshipscr(self):
        self.Frameship=Frame(self)
        self.Frameship.grid()

        
        label2=Label(self.Frameship,text="Battleship")
        label2.grid(row=1,column=0,columnspan=3)

        labeluser=Label(self.Frameship,text="User Field of View")
        labeluser.grid(row=2,column=0,sticky=NE)
        
        self.labelx=Label(self.Frameship)
        self.labelx.grid(row=2,column=0)

        self.labely=Label(self.Frameship)
        self.labely.grid(row=3,column=0)


        self.text1=Text(self.Frameship,height=10,width=88,fg='BLUE')
        self.text1.grid(row=2,column=1,columnspan=3)

        labelcomp=Label(self.Frameship,text="Jacks Field of View")
        labelcomp.grid(row=3,column=0,sticky=NE)

        self.text3=Text(self.Frameship,height=10,width=88,fg='RED')
        self.text3.grid(row=3,column=1,columnspan=3,pady=5)
        
        self.framelabel1=LabelFrame(self.Frameship,text='Message')
        self.text2=Text(self.framelabel1,height=10,width=77)
        self.text2.grid()
        self.framelabel1.grid(row=4,column=1,columnspan=3)
        

        label3=Label(self.Frameship,text="Enter Strike Point")
        label3.grid(row=5,column=0,sticky=E)

        self.entry1=Entry(self.Frameship)
        self.entry1.grid(row=5,column=1,sticky=W)

        self.butt1=Button(self.Frameship,text="OK",command=self.battlestart)
        self.butt1.grid(row=6,column=1)

        self.butt2=Button(self.Frameship,text="Quit",command=self.bsquit)
        self.butt2.grid(row=6,column=4)


    def scorescr(self):
        self.framescore=Frame(self)
        self.framescore.grid()

        self.labscr=Label(self.framescore,text='Score')
        self.labscr.grid(row=0,column=2)
        
        self.pactext=Text(self.framescore,height=30,width=35)
        self.pactext.grid(row=1,column=1,padx=5,pady=5)
        
        self.ttttext=Text(self.framescore,height=30,width=35)
        self.ttttext.grid(row=1,column=2,padx=5,pady=5)

        self.bshiptext=Text(self.framescore,height=30,width=35)
        self.bshiptext.grid(row=1,column=3,padx=5,pady=5)

        self.scrquit=Button(self.framescore,text="Go Back",command=self.go_back)
        self.scrquit.grid(row=3,column=2)

    def dispscore(self):
        self.pactext.insert(INSERT,"PACMAN SCORE\n\n")
        c=0
        for i in self.cur_obj.paclist:
            c=c+1
            self.pactext.insert(INSERT,(str(c)+". "+str(i)+"\n"))
            

        self.ttttext.insert(INSERT,"TIC TAC TOE SCORE\n\n")
        c=0
        for i in self.cur_obj.tttlist:
            c=c+1
            self.ttttext.insert(INSERT,(str(c)+". "+str(i)+"\n"))

        self.bshiptext.insert(INSERT,"BATTLE SHIP SCORE\n\n")
        c=0
        for i in self.cur_obj.bshiplist:
            c=c+1
            self.bshiptext.insert(INSERT,(str(c)+". "+str(i)+"\n"))
        
    def updateacc(self):
        import pickle
        import os
        Robj=open("accfile.dat","rb")
        Pobj=open("tempacc.dat","wb")
        
        try:
            while True:
                Racc=pickle.load(Robj)

                if Racc.passw==self.cur_obj.passw:
                    pickle.dump(self.cur_obj,Pobj)
                else:
                    pickle.dump(Racc,Pobj)

                
        except EOFError:
            pass
        Robj.close()
        Pobj.close()
        os.remove("accfile.dat")
        os.rename("tempacc.dat","accfile.dat")
        print "accfile updated"

    def cleanup(self):
        print "cleanup action activating"
        
        del self.cur_obj
        del self.username,self.password,
        
        print "Cleanup DONE"
        
        

        
        
        
    
