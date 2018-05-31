from  xlwt import Workbook
from datetime import datetime
from BasicReport import  *
from EnergyBalReport import *
import serial
port_new = '/dev/ttyACM0'
port = 30003
baud = 9600
#ser=serial.Serial(port_new,baud)

class Saha():
    
    br =Workbook()
    brsheet = br.add_sheet('Test1')
    er =Workbook()
    ersheet = er.add_sheet('Test1')
    a4 = 0
    a5 = 0
    a6 = 0 
    a7 = 0
    a8 = 0
    a9 = 0
    a11 = 0
    def Primary(self):
        self.BasicRepIntial()
        self.EnergyRepIntial()
        self.Constraints(1)
    def BasicRepIntial(self):
        self.brsheet.write(0,0,"DATE")
        self.brsheet.write(0,1,"TIME")
        self.brsheet.write(0,2,"RPM1")
        self.brsheet.write(0,3,"RPM2")
        self.brsheet.write(0,4,"LOAD")
        self.brsheet.write(0,5,"NORMAL FORCE")
        self.brsheet.write(0,6,"DISPLACED DISTANCE")
        self.brsheet.write(0,7,"GEAR RATIO")
        self.brsheet.write(0,8,"TORQUE")
        self.brsheet.write(0,9,"P2")
        self.brsheet.write(0,10,"P1")
        self.brsheet.write(0,11,"STIFFNESS")
        self.br.save('CVTGeneralCal.xls') 
    
    def EnergyRepIntial(self):
        self.ersheet.write(0,0,"DATE")
        self.ersheet.write(0,1,"TIME")
        self.ersheet.write(0,2,"RPM1")
        self.ersheet.write(0,3,"STIFFNESS")
        self.ersheet.write(0,4,"MASS")
        self.ersheet.write(0,5,"Y")
        self.ersheet.write(0,6,"NORMAL FORCE")
        self.ersheet.write(0,7,"DISPLACED DISTANCE")
        self.ersheet.write(0,8,"POTENTIAL ENERGY")
        self.ersheet.write(0,9,"ENERGY LOSS DUE TO FRICTION")
        self.ersheet.write(0,10,"KINETIC ENERGY IN SHEAVE")
        self.ersheet.write(0,11,"ENERGY DEVELOPED BY ROTATION")
        self.ersheet.write(0,12,"FINAL FORMULA")
        self.er.save('CVTEnergyRep.xls')                 
    
    def Constraints(self,val):
        pullData = open("updation files/Baja.txt",'r').read()
        self.a4,self.a5,self.a6,self.a7,self.a8 = pullData.split(',')
        reval = self.daha(val)
        return reval
    def daha(self,val):
        m = 0
        time2 = ''   
        limit = 0       
        while limit != -1: 
            x =[]
            y =[]
            b =raw_input("Enter string") #ser.readline().strip()
            s = open("Baja2.txt",'w',0)
            s.close()
            try:    
                i = len(b)
                for j in range(0,i):
            	    if b[j] == ',':
                        m = j
            	        break     
            	    else:
                        x.append(b[j])
                        y = []
                if m==0:
                    y.append(0)
                else:
                    for j in range(m+1,i):
                    	y.append(b[j])
                a2 = float(''.join(x))
                a3 = float(''.join(y))
                time1=datetime.now().strftime('%H-%M-%S')
                if time2 != time1:
                    self.brsheet.write(val,0,datetime.now().strftime('%d-%m-%Y'))
                    self.brsheet.write(val,1,time1)
                    self.ersheet.write(val,0,datetime.now().strftime('%d-%m-%Y'))
                    self.ersheet.write(val,1,time1)
                    a12,a13,a14,a15,a16 = getBasic(self,val,a2,a3,float(self.a4),float(self.a5),float(self.a7))
    	            a17,a18,a19,a20,a21 = getEnergy(self,val,a12,float(self.a7),a2,float(self.a6),float(self.a8),float(self.a5))
                    f = open("Baja2.txt",'w')
                    f.write(str(a2)+",")
                    f.write(str(a3)+",")
                    f.write(str(a12)+",")
                    f.write(str(a13)+",")
                    f.write(str(a14)+",")
                    f.write(str(a15)+",")
                    f.write(str(a16)+",")
                    f.write(str(a17)+",")
                    f.write(str(a18)+",")
                    f.write(str(a19)+",") 
                    f.write(str(a20)+",")
                    f.write(str(a21))
                    f.close() 
                    val=val+1
                    time2 = time1
                    limit = limit+1
            except:
                print "sorry"
                continue   
        return val
if __name__ == '__main__':
    Saha().Primary()
