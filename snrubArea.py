from timeit import default_timer as timer
import random

def monteArea(ui_r,nPts):
    #Uses method of randomly scattering points in a square (positive x and y).
    #If the random point distance is within the edge length (radius) of the origin, it is counted. (quarter circle)
    #The ratio of points counted to total points is approx pi/4.

    #However, this method is leaned out by just using nPts as the radius and estimating pi first.

    # Start the function timer
    start_estimate = timer()

    #Define bins and square area
    countAll = 0
    countIn = 0
    nPtsSqrd = nPts*nPts

    while countAll<nPts:
        x = random.randrange(0,nPts)
        y = random.randrange(0, nPts)
        distSqrd = x*x+y*y #calc distance
        if distSqrd<=nPtsSqrd:
            #Inside the quater circle, count it
            countIn+=1
        countAll+=1

    area = 4*countIn/countAll*ui_r*ui_r
    stop_estimate = timer()
    tRun = stop_estimate-start_estimate

    return [area, tRun]