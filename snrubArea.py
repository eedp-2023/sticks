from timeit import default_timer as timer
import random

def monteArea(ui_r,nPts):
    # Start the function timer
    start_estimate = timer()

    countAll = 0
    countIn = 0
    nPtsSqrd = nPts*nPts

    while countAll<nPts:
        x = random.randrange(0,nPts)
        y = random.randrange(0, nPts)
        distSqrd = x*x+y*y
        if distSqrd<nPtsSqrd:
            countIn+=1
        countAll+=1

    area = 4*countIn/countAll
    stop_estimate = timer()
    tRun = stop_estimate-start_estimate

    return [area, tRun]