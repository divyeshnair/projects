from l import *
    
def getBasic(self,uu,rpm1,rpm2,W,F,dx):
    #Gear Ratio
    gr = rpm2/rpm1
    
    #t is Torque,W is load,R is Radius is in metre 
    r = 0.1252
    T = W *9.81 *r
    
    #Power,Driven H.P
    P2 = 2*3.14*rpm2*T/float(60)
    P1 = 2*3.14*rpm1*T/float(60)
    
    #K is Stiffness,F is normal force and dx is displaced distance
    K = F/float(dx)
    
    #Storing the values into excel sheet
    self.brsheet.write(uu,2,round(rpm1,4))
    self.brsheet.write(uu,3,round(rpm2,4))
    self.brsheet.write(uu,4,round(W,4))
    self.brsheet.write(uu,5,round(F,4))
    self.brsheet.write(uu,6,round(dx,4))
    self.brsheet.write(uu,7,round(gr,4))
    self.brsheet.write(uu,8,round(T,4))
    self.brsheet.write(uu,9,round(P2,4))
    self.brsheet.write(uu,10,round(P1,4))
    self.brsheet.write(uu,11,round(K,4))
   
    #saving the excel sheet
    self.br.save('CVTGeneralCal.xls')
     
    return round(K,4),round(P1,4),round(P2,4),round(T,4),round(gr,4)
