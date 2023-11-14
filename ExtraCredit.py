#Import relevant libraries
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import area_calcs
import perimeter
import gen_equispaced_pts
import gen_randomspaced_pts
import snrubArea

#Extra Credit 1
#Initiate for loop, incrementing N points

#User Inputs
maxN = 100
rCirc = 1
x0 = 0
y0 = 0
doRand = 0

#Init Variables
p = []
a = []
nStore = []
tRunP = []
tRunA = []

for n in range(10,maxN,1):
    nStore.append(n)

    #Choose random points or equi-spaced points
    if doRand:
        circPoints = gen_randomspaced_pts.gen_randomspaced_pts(x0,y0,rCirc,n)
    else:
        circPoints = gen_equispaced_pts.gen_equispaced_pts(x0,y0,rCirc,n)
    #Compute perimeter
    perimeterData = perimeter.perimeterfunction(circPoints,x0,y0,rCirc)
    tRunP.append(perimeterData[3])
    p.append(perimeterData[0])

    #Compute area
    areaData = area_calcs.estimate_area(x0,y0,rCirc,circPoints)
    tRunA.append(areaData[3])
    a.append(areaData[0])

pFig, pAxis = plt.subplots()
tAxisP = pAxis.twinx()
pAxis.plot(nStore,p,'--r',label='Est. Perimeter')
pAxis.set_xlabel('n Points')
pAxis.set_ylabel('Perimeter',color='r')
tAxisP.plot(nStore,tRunP,'--k',label='Run Time')
tAxisP.set_ylabel('Run Time [s]')
tAxisP.ticklabel_format(axis='y',style='sci',useMathText=1,scilimits=(0,0))
plt.title('Influence of N Points on Perimeter Estimation and Run Time')

aFig, aAxis = plt.subplots()
tAxisA = aAxis.twinx()
aAxis.plot(nStore,a,'--r',label='Est. Area')
aAxis.set_xlabel('n Points')
aAxis.set_ylabel('Area',color='r')
tAxisA.plot(nStore,tRunA,'--k',label='Run Time')
tAxisA.set_ylabel('Run Time [s]')
tAxisA.ticklabel_format(axis='y',style='sci',useMathText=1,scilimits=(0,0))
plt.title('Influence of N Points on Area Estimation and Run Time')

#Generate plot of perimeter and CPU time
#Generate plot of area and CPU time

#Extra Credit 2
#Estimate area using random monte carlo integration
monteArea = []
tMonte = []
nStoreMonte = []
for n in range(10,10000,100):
    nStoreMonte.append(n)
    monteAreaData = snrubArea.monteArea(rCirc,n)
    monteArea.append(monteAreaData[0])
    tMonte.append(monteAreaData[1])

mFig, mAxis = plt.subplots()
tAxisM = mAxis.twinx()
mAxis.plot(nStoreMonte,monteArea,'--r',label='Est. Area')
mAxis.set_xlabel('n Points')
mAxis.set_ylabel('Area',color='r')
tAxisM.plot(nStoreMonte,tMonte,'--k',label='Run Time')
tAxisM.set_ylabel('Run Time [s]')
tAxisM.ticklabel_format(axis='y',style='sci',useMathText=1,scilimits=(0,0))
plt.title('Area Estimation using Monte Carlo Integration')

#Extra Credit 3
#Estimate pi using monte carlo integration

piEst = monteArea[-1]
print(piEst)
plt.show()
