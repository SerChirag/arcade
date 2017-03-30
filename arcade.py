##########################################################
"""General info about the arcade v1.0045
arcade.py--->deals with main start up GUI
dialog---->deals with login and creation account popup window
gamemanage---->deals with switching to different game
accounts---->deal with getting account info from user
"""
##########################################################3
from Tkinter import*
from tkMessageBox import*
from dialog import*
from gamemanage import*


from PIL import ImageTk,Image
###################################################################################


######################################################################################

class app(Frame,DialogWin,gamemanage):
    def __init__(self,master):
        Frame.__init__(self,master)
        
        
        self.pack()
        self.startscr()
        #self.gamescr()
        
        
    def mess(self):
        
        showinfo(title="HELLO",message="COPPER PADMAN IS RADIOACTIVE",icon=WARNING)




    def startscr(self):
        self.Frame1=Frame(self)
        self.Frame1.grid()
        
        imgb = ImageTk.PhotoImage(Image.open('arcadeimg.jpg'))
        self.labimg=Label(self.Frame1,image=imgb,height=600,width=900)
        self.labimg.image=imgb
        self.labimg.grid(rowspan=10,columnspan=3)

        
        self.label1_strscr=Label(self.Frame1,text="WELCOME TO ARCADE V0.03",bg='white')
        self.label1_strscr.grid(row=0,column=1,sticky='N')

        self.butt1_strscr=Button(self.Frame1,text="LOGIN",command=self.LoginWin)
        self.butt1_strscr.grid(row=2,column=1)

        self.butt2_strscr=Button(self.Frame1,text="CREATE",command=self.CreateWin)
        self.butt2_strscr.grid(row=3,column=1)
        
        self.label2_strscr=Label(self.Frame1,text="Designed by CVJ").grid(row=9,column=0,sticky='SW')
        

    def gamescr(self):
                       
        self.Frame2=Frame(self)
        self.Frame2.grid()
        
        self.label1=Label(self.Frame2,text="WELCOME TO ARCADE")
        self.label1.grid(row=0,column=0)

        self.label2=Label(self.Frame2)
        self.label2.grid(row=1,column=0)

        self.text1=Text(self.Frame2,height=30,width=45)
        self.text1.grid(row=2,column=0,rowspan=2)


        
        self.framelabel1=LabelFrame(self.Frame2,text='Message')
        self.text2=Text(self.framelabel1,height=15,width=65)
        self.text2.grid()
        self.framelabel1.grid(row=2,column=1,padx=10,pady=5)


        self.labelq=Label(self.Frame2,text="""IF you wish to end your game press quit.
Your current score will be saved and added to your scoreboard""")
        self.labelq.grid(row=3,column=1)
        

        self.label3=Label(self.Frame2,text="Enter Command")
        self.label3.grid(row=4,column=0,sticky=W)

        self.entry1=Entry(self.Frame2)
        self.entry1.grid(row=4,column=0)

        self.butt1=Button(self.Frame2,text="OK")
        self.butt1.grid(row=5,column=0)

        self.butt2=Button(self.Frame2,text="Quit")
        self.butt2.grid(row=5,column=1)



    def quitgame(self):
        self.choosegame()
        self.Frame2.destroy()
    
    def goback(self):
        
        self.startscr()
        self.updateacc()
        self.cleanup()
        self.Frame3.destroy()

    def scorestr(self):
        self.scorescr()
        self.dispscore()

        self.Frame3.destroy()

    def go_back(self):
        self.choosegame()
        self.framescore.destroy()

    def choosegame(self):
        

        self.Frame3=Frame(self)
        self.Frame3.grid()
        
        imgb = ImageTk.PhotoImage(Image.open('arcadeimg.jpg'))
        self.labimg=Label(self.Frame3,image=imgb,height=600,width=900)
        self.labimg.image=imgb
        self.labimg.grid(rowspan=10,columnspan=3)


        self.butt1_chscr=Button(self.Frame3,text="Pacman",command=self.startPACMAN)
        self.butt1_chscr.grid(row=2,column=1)

        self.butt2_chscr=Button(self.Frame3,text="TictacToe",command=self.startTTT)
        self.butt2_chscr.grid(row=3,column=1)

        self.butt3_chscr=Button(self.Frame3,text="Battleship",command=self.startBattleship)
        self.butt3_chscr.grid(row=4,column=1)

        self.buttgamescr=Button(self.Frame3,text="ScoreBoard",command=self.scorestr)
        self.buttgamescr.grid(row=5,column=1)
        
        self.butt4_chscr=Button(self.Frame3,text="GO BACK",command=self.goback)
        self.butt4_chscr.grid(row=6,column=1)        
    
        
#######################################################################################        
    
        
        
        
    


if __name__=='__main__':
    top=Tk()
    top.title('ARCADE')
    top.resizable(False,False)
    ###########################
    sw = top.winfo_screenwidth()
    sh = top.winfo_screenheight()
    w = 900
    h = 600
    x = (sw - w)/2
    y = (sh - h)/2
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ##########################
    arc_win=app(top)
    top.mainloop()
    
