from Tkinter import*

class Battleship:
    def __init__(self):
        
        self.s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        self.users=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        self.computers=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        self.dpos=['abc','bcd','efg','fgh','ijk','jkl','mno','nop','aei','eim','bfj','fjn','cgk','gko','dhi','hip']
        self.subpos=['ab','cd','bc','ef','fg','gh','ij','jk','kl','mn','no','op','ae','ei','im','bf','fj','jn','cg','gk','ko','dh','hl','lp']
        self.userdestroy=[]
        self.usersub=[]
        self.compdestroy=[]
        self.compsub=[]

        self.userfragment=[]
        self.compfragment=[]

        self.userfragmentdestroy=[]
        self.userfragmentsub=[]
        self.compfragmentdestroy=[]
        self.compfragmentsub=[]

        ################
        self.lock=[]
        self.lockalpha=[]
        self.pos=0
        self.e=None
        self.zen=0
        #######################
        print "battlefield prepping"
        self.battleinit()
#############################################################################################################################################        
        
    def Battleinstru(self):
        #print "Intiating battle instruction"
        
        self.ship=Toplevel()
        self.ship.title('Battleship Instruction')

        lab_LW1=Label(self.ship,text=("""Welcome Aboard Battleship. I'm Jack Sparrow, king of the 7 seas.Rules are simple.
First you deploy your fleet. You and I both have a Destroyer and a Submarine. The Submarine occupies 2 grid boxes
You can deploy your fleet vertically or horizontally only. Type in your choice with your corresponding alphabets.
If you hit a vessel, you strike will be denoted by >X< symbol. Else if you miss it will be dented by <O> symbol.
Keep an eye out for your health on the right of the screen
Since your new, go first Admiral. ALL HANDS ON DECK!!!"""))
        lab_LW1.grid(row=0,column=0)

        lab3=Label(self.ship,text="Enter coordinates for Destroyer")
        lab3.grid(row=1,column=0)

        self.dest=Entry(self.ship)
        self.dest.grid(row=1,column=1)

        lab_LW2=Label(self.ship,text="Enter coordinates for Submarine")
        lab_LW2.grid(row=2,column=0)

        self.submar=Entry(self.ship)
        self.submar.grid(row=2,column=1)

        but_LW1=Button(self.ship,text="GO",command=self.retcoord)
        but_LW1.grid(row=3,column=0)
#######################################################################################################################################################
    def retcoord(self):
        print 'COORDINATES RETRIVED'
        self.decor=self.dest.get()
        self.sucor=self.submar.get()
        
        self.deploy()

######################################################################################################################################################

    def bgrid(self,text,ref):
        print "clear grid"
        text.delete(1.0,END)
        print "putting grid"
        text.insert(INSERT,str("_"*85+'\n'))
        
        def row(e=0):
            
            text.insert(INSERT,str(" "*5+ref[e]+" "*10+"|"+" "*5))
            e=e+1
            text.insert(INSERT,str(" "*5+ref[e]+" "*10+"|"+" "*5))
            e=e+1
            text.insert(INSERT,str(" "*5+ref[e]+" "*10+"|"+" "*5))
            e=e+1
            text.insert(INSERT,str(" "*5+ref[e]+" "*10+"|"+" "*5))
            text.insert(INSERT,str("_"*85+'\n'))
            return e+1
        fetch=row()
        fetch=row(e=fetch)
        fetch=row(e=fetch)
        fetch=row(e=fetch)
######################################################################################################################################################        

    def deploy(self):
        print "deploying to your coordinates"
        #self.text2.insert(INSERT,"\n Destroyer= 3 Blocks\t")
        #self.text2.insert(INSERT,"Submarine= 2 Blocks\n")

        while (True):
            x=self.decor
            y=self.sucor
        
            
            if (x in self.dpos) and (y in self.subpos):
                self.userdestroy.append(list(x))
                self.usersub.append(list(y))
                break
                
            else:
                
                self.ship.destroy()
                self.text2.insert(INSERT,"Invalid Input. Reinitializing..")
                self.Battleinstru()
                


        self.ship.destroy()
        
        import random
        
            
        xc=random.randint(0,15)
        yc=random.randint(0,23)
        self.compdestroy.append(self.dpos[xc])
        self.compsub.append(self.subpos[yc])

        
        self.fragment()
        self.battleinit_2()
    
######################################################################################################################################################

    def fragment(self):
        print "fragmenting coordinates"
        for i in self.compdestroy:
            for j in i:
                self.compfragment.append(j)
                self.compfragmentdestroy.append(j)
        for i in self.compsub:
            for j in i:
                self.compfragment.append(j)
                self.compfragmentsub.append(j)
        for i in self.userdestroy:
            for j in i:
                self.userfragment.append(j)
                self.userfragmentdestroy.append(j)
        for i in self.usersub:
            for j in i:
                self.userfragment.append(j)
                self.userfragmentsub.append(j)
        z=-1

        for i in self.userfragment[0:len(self.userfragment)-1]:
            e=i
            z=z+1
            for j in self.userfragment[z+1:len(self.userfragment)]:
                if (e==j):
                    self.userfragment.remove(j)
        z=-1
        for i in self.compfragment[0:len(self.compfragment)-1]:
            e=i
            z=z+1
            for j in self.compfragment[z+1:len(self.compfragment)]:
                if (e==j):
                    self.compfragment.remove(j)

######################################################################################################################################################

    def userplay(self):
        print "userplay"
        if(True):
            x=self.entry1.get()#strike point
            if(x in self.s):
            #########################################3
                if (x in self.compfragment):
                    for i in range(0,16):
                        if self.users[i]==x:
                            self.users[i]='>X<'
                            self.compfragment.remove(x)
                            print "user attacked"
                            break
                else:
                    for i in range(0,16):
                        if self.users[i]==x:
                            self.users[i]='<O>'
                            break
            ###########################################
            else:
                self.text2.insert(INSERT,"Invalid Zone. Reinitializing....")

        #store=self.s 
        #self.s=self.users
        self.bgrid(self.text3,self.users)
        #self.s=store
######################################################################################################################################################
        


    def compplay(self):
        print "compplay start"
        if (len(self.lock)==0):
            import random
            while(True):
                x=self.s[random.randint(0,15)]
                if x in self.computers:
                    if (x in self.userfragment):
                        for i in range(0,16):
                            if self.computers[i]==x:
                                self.computers[i]='>X<'
                                self.userfragment.remove(x)
                                self.lock.append(i)
                                self.lockalpha.append(x)
                                break
                    else:
                          for i in range(0,16):
                              if self.computers[i]==x:
                                  self.computers[i]='<O>'
                                  break
                    break
                else:
                    continue   
            #store=self.s
            #self.s=self.computers
            self.bgrid(self.text1,self.computers)
            #self.s= store
        else:
            moves=['up','down','left','right'] #self.pos Value Correspond To Index of moves[]

            if(self.zen==0):
                self.e=self.lock[0]
                self.zen=self.zen+1
            
            if (self.pos==0):
                tar=self.e-4
                if(tar<0):
                    self.pos=self.pos+1

            if (self.pos==1):
                tar=self.e+4
                if(tar>16):
                    self.pos=self.pos+1
                if(tar==self.lock[0]):
                    tar=tar+4

            if (self.pos==2):
                if(self.e in [0,4,8,12]):
                    self.pos=self.pos+1
                else:
                    tar=self.e-1
                    if(tar==self.lock[0]):
                        tar=tar-1

            if (self.pos==3):
                tar=self.e+1
                if(tar==self.lock[0]):
                    tar=tar+1

            while(True):
                x=self.s[tar]
                if x in self.computers:
                    if (x in self.userfragment):
                        for i in range(0,16):
                            if self.computers[i]==x:
                                self.computers[i]='>X<'
                                self.userfragment.remove(x)
                                self.lockalpha.append(x)

                        count=0
                    
                        for i in self.userfragmentdestroy:
                            if i in self.lockalpha:
                                count=count+1
                                continue
                            else:
                                break
                        if (count==3):
                            self.lock=[]
                            self.pos=self.zen=0
                            self.lockalpha=[]

                        count=0
                    
                        for i in self.userfragmentsub:
                            if i in self.lockalpha:
                                count=count+1
                                continue
                            else:
                                break
                        if (count==2):
                            self.lock=self.lockalpha=[]
                            self.pos=0
                            self.zen=0
                        self.e=tar
                        break
                                    
                                
                    else:
                         for i in range(0,16):
                             if self.computers[i]==x:
                                 self.computers[i]='<O>'
                                 self.pos=self.pos+1
                                 self.e=self.lock[0]
                                 break
                         break
                else:
                    self.pos=self.pos+1

                    if (self.pos==0):
                        tar=self.e-4
                        if(tar<0):
                            self.pos=self.pos+1
                    if (self.pos==1):
                        tar=self.e+4
                        if(tar>16):
                            self.pos=self.pos+1
                    if (self.pos==2):
                        if(self.e in [0,4,8,12]):
                            self.pos=self.pos+1
                        else:
                            tar=self.e-1
                    if (self.pos==3):
                        tar=self.e+1
                    continue


            #store=self.s
            #self.s=self.computers
            self.bgrid(self.text1,self.computers)
            #self.s=store
######################################################################################################################################################

    def end(self):
        print "chk end"
        if(len(self.userfragment)==0)or(len(self.compfragment)==0):
            return True
        else:
            return False

######################################################################################################################################################

    def health(self):
        print "Health update"
        #x=StringVar()
        #y=StringVar()
        
        #x.set(str("YOU  ="+"[]"*len(self.userfragment)))
        #y.set(str("JACK ="+"[]"*len(self.compfragment)))

        #self.labelx=Label(self.Frameship,textvariable=x)
        #self.labelx.grid(row=2,column=0)

        #self.labely=Label(self.Frameship,textvariable=y)
        #self.labely.grid(row=3,column=0)
        
        self.labelx.config(text=str("YOU  ="+"[]"*len(self.userfragment)))
        self.labely.config(text=str("JACK ="+"[]"*len(self.compfragment)))

        print self.userfragment
        print self.compfragment
######################################################################################################################################################        
        
    def battleinit(self):
        print "battle init part 1"
        self.bgrid(self.text1,self.s)
        self.bgrid(self.text3,self.s)
        self.Battleinstru()
        
######################################################################################################################################################
    def battleinit_2(self):
        print "battle init part2"
        self.fragment()
        self.health()
        
        self.toss=1

        self.text2.insert(INSERT,"YOUR TURN\n")
        
######################################################################################################################################################
        
    def battlestart(self):

        if(self.end()==False): 
            if(self.toss%2<>0):  
                print "USER ATTACKING"
                self.userplay()
                self.health()

                print "USER FINISHED"
                
                self.toss=self.toss+1
                self.battlestart()

                if(len(self.compfragment)==0):
                    self.text2.insert(INSERT,"YOU WIN!\n")
                    self.text2.insert(INSERT,"YOU CAN PRESS QUIT YOUR SCORE WILL BE SAVED\n")
                elif(len(self.userfragment)==0):
                    self.text2.insert(INSERT,"YOU LOSE!\n")
                    self.text2.insert(INSERT,"YOU CAN PRESS QUIT YOUR SCORE WILL BE SAVED\n")

                

            else:
                print "COMPUTER TURN"
                
                self.text2.insert(INSERT,"Jacks Turn\n")
                self.compplay()
                #self.text2.insert(INSERT,"Jacks Done\n")
                self.toss=self.toss+1
                self.health()
                print "COMPUTER FINISHED"

                if(len(self.compfragment)==0):
                    self.text2.insert(INSERT,"YOU WIN!\n")
                    self.text2.insert(INSERT,"YOU CAN PRESS QUIT YOUR SCORE WILL BE SAVED\n")
                elif(len(self.userfragment)==0):
                    self.text2.insert(INSERT,"YOU LOSE!\n")
                    self.text2.insert(INSERT,"YOU CAN PRESS QUIT YOUR SCORE WILL BE SAVED\n")

                self.text2.insert(INSERT,"Your Turn\n")



"""
        else:

            if(len(self.compfragment)==0):
                self.text2.insert(INSERT,"YOU WIN!\n")
            elif(len(self.userfragment)==0):
                self.text2.insert(INSERT,"YOU LOSE!\n")
            else:
                self.text2.insert(INSERT,"DRAW!\n")

"""
######################################################################################################################################################
        
               


                


