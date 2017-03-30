from Tkinter import*
from accounts import*

class DialogWin(Account):
        

    def LoginWin(self):
        
        self.Log_win=Toplevel()
        self.Log_win.title('Login')

        lab_LW1=Label(self.Log_win,text="Username")
        lab_LW1.grid(row=0,column=0)

        self.ent_LW1=Entry(self.Log_win)
        self.ent_LW1.grid(row=0,column=1)

        lab_LW2=Label(self.Log_win,text="password")
        lab_LW2.grid(row=1,column=0)

        self.ent_LW2=Entry(self.Log_win,show="*")
        self.ent_LW2.grid(row=1,column=1)

        but_LW1=Button(self.Log_win,text="GO",command=self.getAccountinfo)
        but_LW1.grid(row=2,column=0)

        but_LW2=Button(self.Log_win,text="QUIT",command=self.Log_win.destroy)
        but_LW2.grid(row=2,column=1)

    def CreateWin(self):
        
        self.Create_win=Toplevel()
        self.Create_win.title('Login')

        lab_LW1=Label(self.Create_win,text="Create Username")
        lab_LW1.grid(row=0,column=0)

        self.ent_LW1=Entry(self.Create_win)
        self.ent_LW1.grid(row=0,column=1)

        lab_LW2=Label(self.Create_win,text="Enter unique Password")
        lab_LW2.grid(row=1,column=0)

        self.ent_LW2=Entry(self.Create_win,show="*")
        self.ent_LW2.grid(row=1,column=1)

        lab_LW3=Label(self.Create_win,text="Phone no.")
        lab_LW3.grid(row=2,column=0)

        self.ent_LW3=Entry(self.Create_win)
        self.ent_LW3.grid(row=2,column=1)

        but_LW1=Button(self.Create_win,text="Create",command=self.createAccount)
        but_LW1.grid(row=3,column=0)

        but_LW2=Button(self.Create_win,text="QUIT",command=self.Create_win.destroy)
        but_LW2.grid(row=3,column=1)
