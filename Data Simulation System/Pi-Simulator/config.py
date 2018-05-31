from Tkinter import *
from PIL import ImageTk,Image
import tkFont
import ttk
import os
import time
import socket
class Raspi:
    mf="-1"
    fl="-1"
    mfsl="-1"
    flsl="-1"
    ipu=""
    net="-1"
    varu1="Lan"
    varu2="Wifi"
    '''
    var7="" 
    var8=""
    var9=""
    var10=""
    var11="" 
    var12=""
    '''
   
    cou=1
    fontu = ""
    fontu1 = ""
    fontu2 = ""
    fontu3 = ""
    fontu4 = ""
        
    def __init__(self,master):
       self.roo=master
       self.main(self.roo)
            
        
    
    def main(self,root1):
        self.fontu = tkFont.Font(family="Helvetica", size=30)
        self.fontu1 = tkFont.Font(family="Times", size=20)
        self.fontu2 = tkFont.Font(family="Times", size=16)
        self.fontu3 = tkFont.Font(family="Times", size=10)
        self.fontu4 = tkFont.Font(family="Times", size=13)
        l1= Label(root1, text="RaspberryPi Simulator",font=self.fontu)
        l1.place(x=300,y=0)

#Connect the device first to start configuring the pi
        def connect():
           
            if not self.sle.get() =="":
                self.b1.configure(state="disabled")
                self.b2.configure(state="normal")
                self.b6.configure(state="normal")

                try:
                    soc=socket.gethostbyname(self.sle.get())
                    self.ipu=soc
                    self.l5.config(text=self.sle.get())
                    self.l18.config(text="Active")
                    self.roo.update()
                    
                except Exception as e:
                    self.l5.config(text=self.sle.get())
                    self.l18.config(text="Inactive")
                    self.roo.update()
                    self.b1.configure(state="normal")
                    self.b2.configure(state="disabled")
                    self.b6.configure(state="disabled")

        def disconnect():
            self.b1.configure(state="normal")
            self.b2.configure(state="disabled")
            self.b6.configure(state="disabled")
            self.sle.set('')
            self.ipu=""

            try:
                self.l5.config(text="")
                self.l18.config(text="")
                self.roo.update()
                
            except Exception as e:
               pass
            
        def topu():
            top=Toplevel(width=210,height=100)
            top.title("RaspberryPi Simulator")
            noti = Label(top, text ="%s is going \ndown for reboot\n NOW!"%self.sle.get(), font=self.fontu4,)
            noti.place(x=10,y=20)

        def reboot():
            msg="reboot"
            try:
                serv=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                host = self.ipu
                port = 5001;
                serv.sendto(msg, (host, port))
                topu()
            except Exception as e:
                print e
                pass


        l2=Label(root1,text="Select Device:",font=self.fontu2)
        l2.place(x=10,y=90)
        l3=Label(root1,text="Device:",font=self.fontu2)
        l3.place(x=10,y=140)
        self.l5=Label(root1, text="",font=self.fontu2)
        self.l5.place(x=150,y=140)
        l4=Label(root1,text="Status:",font=self.fontu2)
        l4.place(x=10,y=190)
        self.l18=Label(root1, text="",font=self.fontu2)
        self.l18.place(x=150,y=190)
        val1=['RASPBERRYPI-1','RASPBERRYPI-2','RASPBERRYPI-3','RASPBERRYPI-4','RASPBERRYPI-5']
        self.sle=ttk.Combobox(root1,textvariable="",width=23)
        self.sle['values'] = val1
        self.sle.place(x=150,y=95)
        self.b1=Button(root1,text="Connect",font=self.fontu4,width=8,height=1,command=connect)
        self.b1.place(x=10,y=230)

        
        self.b6=Button(root1,text="Disconnect",font=self.fontu4,width=9,height=1,command=disconnect)
        self.b6.place(x=110,y=230)
        
        self.b2=Button(root1,text="Reboot",font=self.fontu4,width=8,height=1,command=reboot)
        self.b2.place(x=220,y=230)

        self.b1.configure(state="normal")
        self.b2.configure(state="disabled")
        self.b6.configure(state="disabled")

        
#Set the date and time according to the host system settings        
        def synchro():
            tmu=time.strftime("%H:%M:%S")
            dy=time.strftime("%a")
            dt=time.strftime("%d-%m-%y")
            
            dtt=time.strftime("%d")
            dtm=time.strftime("%b") 
            dty=time.strftime("%Y") 
             
            self.l10.config(text=dt,font=self.fontu2)
             
            self.l11.config(text=dy,font=self.fontu2)
            self.l12.config(text=tmu,font=self.fontu2)
            self.roo.update()
            msg="%s %s %s %s GST %s "%(dy,dtm,dtt,tmu,dty)
            try:
                serv=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                host = self.ipu
                port = 5001;
                serv.sendto(msg, (host, port))
                
            except Exception as e:
                print e    
                pass

        l6=Label(root1, text="Do you want to set the below mentioned \n parameters according to your\n laptop's settings ?",font=self.fontu4)
        l6.place(x=700,y=90)
        l7=Label(root1, text="Date:",font=self.fontu2)
        l7.place(x=730,y=160)
        l8=Label(root1, text="Day:",font=self.fontu2)
        l8.place(x=730,y=210)
        l9=Label(root1, text="Time:",font=self.fontu2)
        l9.place(x=730,y=260)
        self.l10=Label(root1, text="",font=self.fontu2)
        self.l10.place(x=800,y=160)
        self.l11=Label(root1, text="",font=self.fontu2)
        self.l11.place(x=800,y=210)

        self.l12=Label(root1, text="",font=self.fontu2)
        self.l12.place(x=800,y=260)

        b2=Button(root1,text="Sync",font=self.fontu4,width=10,height=1,command=synchro)
        b2.place(x=800,y=300)

        
#Configure the mfd id,flowmeter id and sleep time
        def sendInfo():
            if self.mf.get()=="":
                mf="-1"
            else:
                mf=self.mf.get()
            if self.fl.get()=="":
                fl="-1"
            else:
                fl=self.fl.get()
            if self.mfsl.get()=="":
                mfsl="-1"
            else:
                mfsl=self.mfsl.get()
            if self.flsl.get()=="":
                flsl="-1"
            else:
                flsl=self.flsl.get()
                
            msg="%s,M,%s,F,%s,MT,%s,FT"%(mf,fl,mfsl,flsl)
            try:
                serv=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                host = self.ipu
                port = 5002;
                serv.sendto(msg, (host, port))
                
            except Exception as e:
                print e    
                pass
            self.mf.delete('0',END)
            self.fl.delete('0',END)
            self.mfsl.set('')
            self.flsl.set('')
            
        l13=Label(root1, text="MFD Id:",font=self.fontu2)
        l13.place(x=10,y=430)
        self.mf=Entry(root1,width=20)
        self.mf.place(x=140,y=435)
        l14=Label(root1, text="FlowMeter Id:",font=self.fontu2)
        l14.place(x=300,y=430)
        self.fl=Entry(root1,width=20)
        self.fl.place(x=470,y=435)
        l15=Label(root1, text="Sleep Time(MFD):",font=self.fontu2)
        l15.place(x=10,y=480)
        l16=Label(root1, text="Sleep Time(Flowmeter):",font=self.fontu2)
        l16.place(x=300,y=480)
        val1=['','1','2','3','4','5','6','7','8','9',10,
              '11','12','13','14','15','16','17','18','19','20',
              '21','22','23','24','25','26','27','28','29','30',
              '31','32','33','34','35','36','37','38','39','40',
              '41','42','43','44','45','46','47','48','49','50',
              '51','52','53','54','55','56','57','58','59','60']
        self.mfsl=ttk.Combobox(root1,textvariable="",width=10)
        self.mfsl['values'] = val1
        self.mfsl.place(x=180,y=483)
        val1=['','1','2','3','4','5','6','7','8','9',10,
              '11','12','13','14','15','16','17','18','19','20',
              '21','22','23','24','25','26','27','28','29','30',
              '31','32','33','34','35','36','37','38','39','40',
              '41','42','43','44','45','46','47','48','49','50',
              '51','52','53','54','55','56','57','58','59','60']
        self.flsl=ttk.Combobox(root1,textvariable="",width=10)
        self.flsl['values'] = val1
        self.flsl.place(x=510,y=483)


        b3=Button(root1,text="Go",font=self.fontu2,width=10,command=sendInfo)
        b3.place(x=240,y=520)   

#Configure the network of pi
        def internet():
            if self.ss.get()=="":
                ss="-1"
            else:
                ss=self.ss.get()
                
            if self.pp.get()=="":
                pp="-1"
            else:
                pp=self.pp.get()
            inter=self.net
            msg= "%s,M,%s,U,%s,P" %(inter,ss,pp)
       
            try:
                serv=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                host = self.ipu
                port = 5003;
                serv.sendto(msg, (host, port))
                
            except Exception as e:
                print e    
            self.ss.delete('0',END)
            self.pp.delete('0',END)
            
        l17=Label(root1, text="Network:",font=self.fontu1)
        l17.place(x=370,y=90)
        ch=IntVar()
        dh=IntVar()
        
        ch1=Checkbutton(root1,text=self.varu1,variable=ch,font=self.fontu1,onvalue=1,offvalue=0,command=lambda :(check(),sendo()))
        ch1.place(x=490,y=85)
        ch2=Checkbutton(root1,text=self.varu2,variable=dh,font=self.fontu1,command=lambda :(check1(),sendo1()))
        ch2.place(x=580,y=85)
        
        l23=Label(root1,text="SSID:",font=self.fontu2)
        l23.place(x=370,y=150)
        l24=Label(root1,text="Password:",font=self.fontu2)
        l24.place(x=370,y=195)
        self.ss=Entry(root1,width=20)
        self.ss.place(x=480,y=150)
    
        self.pp=Entry(root1,width=20)
        self.pp.place(x=480,y=195)
        self.ss.configure(state='disabled')
        self.pp.configure(state='disabled')
                
        b3=Button(root1,text="Done",font=self.fontu4,width=10,command=internet)
        b3.place(x=450,y=240)   
        
        def check():
            
            if ch.get() == 1:
                self.ss.configure(state='disabled')
                self.pp.configure(state='disabled')
                
            
        def check1():
              if dh.get() == 1:
                self.ss.configure(state='normal')
                self.pp.configure(state='normal')
              else:
                self.ss.configure(state='disabled')
                self.pp.configure(state='disabled')
            
               
        def sendo():
              if ch.get() == 1:
                  dh.set(0)
                  self.net=self.varu1
        def sendo1():
              
              if dh.get() == 1:
                  self.net=self.varu2
                  ch.set(0)
          
root=Tk()

c=Raspi(root)
root.geometry("1000x580")
root.resizable(width=False, height=False)
#width = root.winfo_screenwidth()
#height = root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))
root.title("RaspberryPi Simulator")
root.mainloop()

