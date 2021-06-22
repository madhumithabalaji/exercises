class utils:
    #getCurrentTime: Get current time
    def getCurrentTime():
        return (datetime.datetime.today() - predictIschemia.propPbj['baseDate']).total_seconds()    

class predictIschemia:
    #config object
    propPbj = { 'baseDate': datetime.datetime(2000, 1, 1), 
                'alarmTimerSecs': 2,
                'averageTimer': 20, #Time/Prority for scheduler (priority queue)
                'startIdSeg': 1,
                'startIdAvg': 1
              }
    ischemiaEvents,averageList = [], []
    
    #constructor for predictIschemia class
    def __init__(self, timeVal, stSegVal):
        self.timeVal = timeVal
        self.stSegVal = stSegVal
        return None
    
    #processEKG: Trigger alarm
    def ProcessEKG(ekgObj):
        #print("Inside ProcessEKG")
        predictIschemia.propPbj['startIdSeg']+=1
        ekgObj.stSegVal, ekgObj.timeVal = random.randrange(-5, 5), utils.getCurrentTime()
        predictIschemia.ischemiaEvents.append((predictIschemia.propPbj['startIdSeg'],ekgObj.timeVal, ekgObj.stSegVal))
        prediction.enter(predictIschemia.propPbj['alarmTimerSecs'], 1, predictIschemia.ProcessEKG, kwargs={'ekgObj': ekgObj})
        return None
    
    #avgVals: Calculate min, max and average for every 2-min
    def avgVals(n):
        n = n*math.floor(predictIschemia.propPbj['averageTimer']/2)
        valsList = []
        tempObj = [predictIschemia.ischemiaEvents[i] for i in range(n- math.floor(predictIschemia.propPbj['averageTimer']/2), n ,1)] 
        valsList.append((min(tempObj, key=lambda x: x[2]))[2])
        valsList.append((max(tempObj, key=lambda x: x[2]))[2])
        valsList.append(0)
        #print('valsList \n', valsList)
        return valsList
    
    #calcAvg: Scheduler handler logic for every 2-mins 
    def calcAvg(averageList): 
        valsList = predictIschemia.avgVals(predictIschemia.propPbj['startIdAvg'])
        predictIschemia.averageList.append({'id':predictIschemia.propPbj['startIdAvg'], 'avg': valsList[2], 'min':valsList[0], 'max':valsList[1]})
        predictIschemia.propPbj['startIdAvg']+=1
        if valsList[0] < -2 or valsList[1] > 2 or valsList[1]-valsList[0] > 2:
            predictIschemia.ischemiaAlarmHandler()
        prediction.enter(predictIschemia.propPbj['averageTimer'], 2, predictIschemia.calcAvg, kwargs={'averageList': averageList})
        return None
        
    #ischemiaAlarmHandler: Alarm function to notify user of Ischemia
    def ischemiaAlarmHandler():
        print("Alarm Triggered: Ischemia Prediction")
        return None
    
########## Entry Point ##########

import datetime, random, math, sched, time
from threading import Timer

########## Problem 1 ##########

ekgObj = predictIschemia(utils.getCurrentTime(), random.randrange(-5, 5))  
prediction = sched.scheduler(time.time, time.sleep)
predictIschemia.ischemiaEvents.append((predictIschemia.propPbj['startIdSeg'],ekgObj.timeVal, ekgObj.stSegVal))
prediction.enter(predictIschemia.propPbj['alarmTimerSecs'], 1, predictIschemia.ProcessEKG, kwargs={'ekgObj': ekgObj})
prediction.enter(predictIschemia.propPbj['averageTimer'], 2, predictIschemia.calcAvg, kwargs={'averageList': predictIschemia.ischemiaEvents})
prediction.run()

########## Problem 2 ##########


########## Problem 3 ##########
