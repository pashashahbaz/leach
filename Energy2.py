import matplotlib.pyplot as plt
import Setpara2
import CreateRandomSens2
import ConfigSensors2
import Ploter2
import SendReceivePacket2
import DisToSink2
import time
import ResetSensor2
import SelectCH2
import FindReceiver2
import findsender2
import JointonearestCH2
n=100
Area={}
Model={}
Area,Model=Setpara2.setp(Area,Model,n)
X=[0]*n
Y=[0]*n
X,Y=CreateRandomSens2.create(Area,Model,X,Y)
xd=[]
yd=[]
G=[]
df=[]
types=[]
E=[]
ids=[]
distosink=[]
distoCH=[]
MCH=[]
xd,yd,G,df,types,E,ids,distosink,distoCH,MCH=ConfigSensors2.sensor(Area,Model,X,Y,xd,yd,G,df,types,E,ids,distosink,distoCH,MCH)
Sensors={'xd':xd,'yd':yd,'G':G,'df':df,'types':types,'E':E,'ids':ids,'distosink':distosink,'distoCH':distoCH,'MCH':MCH}
d=0

d=Ploter2.plott(Sensors,Model)
initEnergy=0
for i in range(n):
    initEnergy +=Sensors['E'][i]

SRP=[0]*Model['rmax']
RRP=[0]*Model['rmax']
SDP=[0]*Model['rmax']
RDP=[0]*Model['rmax']
SumDead=[0]*Model['rmax']
ClusterH=[0]*Model['rmax']
AllSensorEnergy=[0]*Model['rmax']
srp=0
rrp=0
sdp=0
rdp=0
Sender=[]
Sender.append(n+1)
Receiver=[0]*n
for i in range(n):
    Receiver[i]=i+1

Sensors,srp,rrp,sdp,rdp=SendReceivePacket2.packet(Sensors,Model,Sender,'Hello',Receiver,srp,rrp,sdp,rdp)

Sensors=DisToSink2.send(Sensors,Model)

SRP[0]=srp
RRP[0]=rrp
SDP[0]=sdp
RDP[0]=rdp
s=Model['rmax']
for i in range(1):
    member=[]
    countCH=0
    srp=0
    rrp=0
    sdp=0
    rdp=0
    SRP[i+1]=srp
    RRP[i+1]=rrp
    SDP[i+1]=sdp
    RDP[i+1]=rdp
    time.sleep(0.005)
    
    Sensors=ResetSensor2.reset(Sensors,Model)
    
   
    Aroundclear=10
    if i%Aroundclear==0:
        for j in range(n):
            Sensors['G'][j]=0
    
    TotalCH=[]
    TotalCH,Sensors=SelectCH2.select(TotalCH,Sensors,Model,i)
    print(TotalCH)
    print(Sensors['types'])
    Deadnum=0
    Deadnum=Ploter2.plott(Sensors,Model)
    for k in range(len(TotalCH)):
        Sender[0]=TotalCH[k]
        senderRR=Model['RR']
        Receiver=[]
        Receiver=FindReceiver2.find(Sensors,Model,Sender,Receiver,senderRR)
        print(receiver)
        Sensors=SendReceivePacket2.packet(Sensors,Model,Sender,'Hello',Receiver,srp,rrp,sdp,rdp) 
    Sensors=JointonearestCH2.join(Sensors,Model,TotalCH)
    
    for j in range(n):
        XL=[]
        YL=[]
        if Sensors['type'][j]=='N' and Sensors['distoCH'][j]<Sensors['distosink'][j] and Sensors['E'][j]>0:
            XL.append(Sensors['xd'][j])
            XL.append(Sensors['xd'][Sensors['MCH'][j]])
            YL.append(Sensors['yd'][i])
            YL.append(Sensors['yd'][Sensors['MCH'][j]])
            plt.plot(XL,YL)
    NumPack=Model['NumPacket']
    for j in range(1):
        d=Ploter2.plott(Sensors,Model)
        for k in range(len(TotalCH)):
            Receiver=[]
            Receiver.append(TotalCH[k])
            Sender=[]
            Sender=findsender2.send(Sensors,Model,Receiver,Sender)
            Sensors=SendReceivePacket2.packet(Sensors,Model,Sender,'Hello',Receiver,srp,rrp,sdp,rdp)
    for j in range(len(TotalCH)):
        Receiver=[]
        Receiver.append(n+1)
        Sender=[]
        Sender.append(TotalCH[k])
        Sensors=SendReceivePacket2.packet(Sensors,Model,Sender,'Hello',Receiver,srp,rrp,sdp,rdp)
    
            
