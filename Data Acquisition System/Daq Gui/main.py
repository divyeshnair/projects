#interval_once update karna enter string ka before check

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.pagelayout import PageLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from datetime import datetime
from kivy.properties import ObjectProperty, StringProperty,NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.widget import Widget
from kivy.clock import Clock
from functools import partial
from  xlwt import Workbook
import xlrd
import os
from  l import * 
Builder.load_file('baja.kv')
class BajaSecond(Screen):
    a = StringProperty('')
    b = StringProperty('')
    d1 = StringProperty('')
    d2 = StringProperty('')
    d3 = StringProperty('')
    d4 = StringProperty('')
    d5 = StringProperty('')
    d6 = StringProperty('')
    d7 = StringProperty('')
    d8 = StringProperty('')
    d9 = StringProperty('')
    d10 = StringProperty('')
    d11 = StringProperty('')
    d12 = StringProperty('')
    unit = NumericProperty(1.8)
    unit1 = NumericProperty(2.4)
    sp_txt = StringProperty('0')
    sp_txt1 = StringProperty('0')
    sp_txt2 = StringProperty('0')
    val = NumericProperty(90)
    val1 = NumericProperty(120)
    val2 = NumericProperty(120)
    needle_rot = 0
    needle_rot1 = 0
    needle_rot2 = 0
    z = 0
    nr =1               #no. of rows
    pr = 0
    value=1
    value1=1
    value2=1       
    send_value=0
    send_value1=0
    send_value2=0
    
       
        
    def getvalue(self,*args):
        
        pu = open("Baja2.txt",'r').read()
        ab,bc,cd,de,ef,gh,hi,ij,jk,kl,lm,mn=pu.split(",")                 
        self.d1=ab
        self.d2=bc
        self.d3=cd
        self.d4=de
        self.d5=ef
        self.d6=gh
        self.d7=hi
        self.d8=ij
        self.d9=jk
        self.d10=kl
        self.d11=lm         
        self.d12=mn   
        
    def turn(self,value):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 50 value.


        '''
        if self.value <= self.send_value:
            
            if self.value < 101:
                self.needle_rot = (50 * self.unit) -(self.value * self.unit)
                self.val = self.needle_rot
                self.sp_txt = str(round(self.value,1))
                self.value=self.value+1
            
        if self.value>self.send_value:
            if self.value>=0:
                self.value=self.value-1
                self.needle_rot = (50 * self.unit) -(self.value * self.unit)
                self.val = self.needle_rot
                self.sp_txt = str(round(self.value,1))

    def turn1(self,args):
        if self.value1 <= self.send_value1:
            if self.value1 < 5000:
                self.needle_rot1 = (50 * self.unit1) -(self.value1 * 0.03)
                self.val1 = self.needle_rot1
                self.sp_txt1 = str(round(self.value1,1))
                self.value1=self.value1+1
        
        if self.value1 > self.send_value1:
            if self.value1 > 0:
                self.value1=self.value1-1
                self.needle_rot1 = (50 * self.unit1) -(self.value1 * 0.03)
                self.val1 = self.needle_rot1
                self.sp_txt1 = str(round(self.value1,1))
                
    def turn2(self,args):
        if self.value2 <= self.send_value2:
            if self.value2 < 5000:
                self.needle_rot2 = (50 * self.unit1) -(self.value2 * 0.03)
                self.val2 = self.needle_rot2
                self.sp_txt2 = str(round(self.value2,1))
                self.value2=self.value2+1
        
        if self.value2 > self.send_value2:
            if self.value2 > 0:
                self.value2=self.value2-1
                self.needle_rot2 = (50 * self.unit1) -(self.value2 * 0.03)
                self.val2 = self.needle_rot2
                self.sp_txt2 = str(round(self.value2,1))
    
    def test(self,*args):
        
        self.send_value = float(open("updation files/123.txt",'r').read())
        Clock.schedule_interval(self.turn,0.2)
 
    def test1(self,*args):
        
        self.send_value1 = float(open("updation files/rpm1.txt",'r').read())
        self.send_value2 = float(open("updation files/rpm2.txt",'r').read())
        Clock.schedule_interval(self.turn1,0.2) and Clock.schedule_interval(self.turn2,0.2) 
 
            
    def __init__(self,*args,**kwargs):
        super(BajaSecond, self).__init__(*args, **kwargs)
        self.a = datetime.now().strftime('%d-%m-%Y')
        self.b = datetime.now().strftime('%H:%M:%S') 
        Clock.schedule_interval(self.getvalue,1)
        Clock.schedule_interval(self.test,1)
        Clock.schedule_interval(self.test1,1)
        

        
class BajaFirst(Screen):
    
    def foto(self,b1,b2,b3,b4,b5):
        s = open("updation files/Baja.txt",'w',0)
        f = open("updation files/Baja.txt",'a+')
        f.write(b1+",")
        f.write(b2+",")
        f.write(b3+",")
        f.write(b4+",")
        f.write(b5)
        f.close()
        sm.current="momo"
        #os.system("start python l.py")
        os.system("gnome-terminal -e 'bash -c \"python l.py; exec bash\"'")


        
class BajaInitial(Screen):
    def get(self):
        s = open("updation files/Baja.txt",'w',0)
        s.write("0,0,0,0,0")
        s.close()
        
        sm.current = "dodo"
        
    Clock.schedule_once(get,1)

          
sm = ScreenManager(transition=WipeTransition())
sm.add_widget(BajaInitial(name = 'jojo'))
sm.add_widget(BajaFirst(name = 'dodo'))
sm.add_widget(BajaSecond(name = 'momo'))

class Baja(App):
    def build(self):
        s = open("Baja2.txt",'w')
        s.write("0,0,0,0,0,0,0,0,0,0,0,0")
        s.close()  
        return sm
if __name__ == '__main__':
    Baja().run()

