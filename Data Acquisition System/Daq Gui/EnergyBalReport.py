from l import *
    
def getEnergy(self,uu,K,dx,rpm1,M,Y,F):
    #ES is potential energy stored in spring
    ES = 0.5*K*dx*dx    
    
    #Energy loss due to Friction
    x= dx + 0.15
    d1 = 2.4641*x-0.24641
    u = 0.3
    EF = 2 *  u * d1 * F
    
    #Kinetic Energy stored in sheave
    V = 3.14 * d1 * rpm1/float(60)
    KE = 0.5*M*V*V
   
    #Energy developed by rotation of flywheel
    w = 2*3.14*rpm1/float(60)
    ER = M*(Y*w*Y*w)*3 
    
    #Final Formula
    mw1 =EF-ES
    mw2 = 0.5*V*V+Y*Y*w*w
    mw = mw1/float(mw2)
    
    #Storing the values into excel sheet
    self.ersheet.write(uu,2,round(rpm1,4))
    self.ersheet.write(uu,3,round(K,4))
    self.ersheet.write(uu,4,round(M,4))
    self.ersheet.write(uu,5,round(Y,4))
    self.ersheet.write(uu,6,round(F,4))
    self.ersheet.write(uu,7,round(dx,4))
    self.ersheet.write(uu,8,round(ES,4))
    self.ersheet.write(uu,9,round(EF,4)) 
    self.ersheet.write(uu,10,round(KE,4))
    self.ersheet.write(uu,11,round(ER,4))
    self.ersheet.write(uu,12,round(mw,4))
     
    #saving the excel sheet
    self.er.save('CVTEnergyRep.xls')
    
    return round(ES,4),round(EF,4),round(KE,4),round(ER,4),round(mw,4)
