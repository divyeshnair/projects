from Tkinter import *
import Tkinter as tk
import tkFont
import webbrowser 
import os 

class Launch():
    def __init__(self,master):
        
        self.txt_font = tkFont.Font(size=30)
        self.label1 = Label(master,text="THE ASHWARIDERS",font=self.txt_font)
        self.label1.place(x=50,y=0)
   
        pic = "img/ashwa1.gif"
        self.photo= PhotoImage(file=pic)
        self.label2 = Label(master,image=self.photo)
        self.label2.place(x=50,y=50)  
 
        self.button1 = Button(master,text="Software Designed and Developed by:Divyesh Nair",width="60",height="2",command = self.create_window)
        self.button1.place(x=0,y=510)
    
        self.button2 = Button(master,text="Launch",width="15",height="2",command = self.main)
        self.button2.place(x=180,y=460)

    def main(self):
        os.system("start python main.py")
        #os.system("gnome-terminal -e 'bash -c \"python main.py; exec bash\"'")

  
    def create_window(self):
        window=Toplevel()
        window.geometry("530x500")
        window.resizable(width=FALSE, height=FALSE)
         
        self.txt_font2 = tkFont.Font(size=20)
        self.txt_font3 = tkFont.Font(size=15)
        self.label1 = Label(window,text="THE ASHWARIDERS",font=self.txt_font)
        self.label1.place(x=50,y=0)
     
        self.label3 = Label(window,text="Developer Details",font=self.txt_font2)
        self.label3.place(x=130,y=80)
   
        pic1 = "img/image1.gif"
        self.photo1= PhotoImage(file=pic1)
        self.label4 = Label(window,image=self.photo1)
        self.label4.place(x=1,y=150)

        self.label5 = Label(window,text="Name: Divyesh Nair",font=self.txt_font3)
        self.label5.place(x=220,y=150)
     
        self.label6 = Label(window,text="Email: divyeshnr@gmail.com",font=self.txt_font3)
        self.label6.place(x=220,y=190)

        pic2 = "img/images2.gif"
        self.photo2= PhotoImage(file=pic2)
        self.button3 = Button(window,image=self.photo2,width="30",height="30",command = self.fb)
        self.button3.place(x=300,y=230)

        pic3 = "img/images3.gif"
        self.photo3= PhotoImage(file=pic3)
        self.button4 = Button(window,image=self.photo3,width="30",height="30",command = self.ln)
        self.button4.place(x=350,y=230)

        pic4 = "img/images4.gif"
        self.photo4= PhotoImage(file=pic4)
        self.button5 = Button(window,image=self.photo4,width="30",height="30",command = self.go)
        self.button5.place(x=400,y=230)

    def fb(self):
        webbrowser.open("https://www.facebook.com/divyesh.nair.9")
    def ln(self):
        webbrowser.open("https://www.linkedin.com/profile/view?id=AAMAABF00bwBZK8mDDu_Udfw8UUlTg4BWITMYQ8&trk=hp-identity-name")

    def go(self):
        webbrowser.open("https://plus.google.com/u/0/114015587344367473764/")
                 

root=Tk()
l = Launch(root)
root.geometry("500x550")
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
'''
def create_window():
    window = tk.Toplevel(root)

root = tk.Tk()
b = tk.Button(root, text="Create new window", command=create_window)
b.pack()

root.mainloop()
'''
