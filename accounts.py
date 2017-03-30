"""
You guys have to have to complete this module

about this account.py

the constructor is never intialised please dont use it in any way
getAccountinfo()--->it is called from the login popup window when the login button is pressed.

createAccount()---->it is called from the create account popup window when the create button is pressed

"""
from Tkinter import*
import pickle
class Account:

    def getAccountinfo(self):
        self.username=self.ent_LW1.get()
        self.password=self.ent_LW2.get()

        if self.verify()==True:
            self.Log_win.destroy()
            self.choosegame()
            self.Frame1.destroy()
        else:
            self.Log_win.destroy()
            
            self.mess=Toplevel()
            label=Label(self.mess,text='You have entered wrong credential or you have not registrated')
            label.grid(row=1)
            butt=Button(self.mess,text='OK',command=self.mess.destroy)
            butt.grid(row=2)

        

    def verify(self):
        fobj=open('accfile.dat','rb')
        chk=False
        self.objpos=0
        try:
            while True:
                obj=pickle.load(fobj)
                if obj.user==self.username and obj.passw==self.password:

                    self.cur_obj=obj

                    chk=True
                    break
                else:
                    chk=False
                self.objpos=self.objpos+1
        except EOFError:
            chk=False
        fobj.close()
        return chk
    
        


    def createAccount(self):
        self.s_username=self.ent_LW1.get()
        self.s_password=self.ent_LW2.get()
        
        if len(self.s_username)>0 and len(self.s_password)>0:
            obj=acc(self.s_username,self.s_password) 
            fobj=open('accfile.dat','ab')
            pickle.dump(obj,fobj)
            fobj.close()

            self.Create_win.destroy()
            

        else:
            self.Create_win.destroy()
            self.mess=Toplevel()
            label=Label(self.mess,text='You have entered wrong credential or you have not registrated')
            label.grid(row=1)
            butt=Button(self.mess,text='OK',command=self.mess.destroy)
            butt.grid(row=2)

######################################## 
    
class acc:
    
    def __init__(self,a,b):
        self.user=a
        self.passw=b
        self.paclist=[]
        self.tttlist=[]
        self.bshiplist=[]
        
##########################################


                  
