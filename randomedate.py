import random
import time
def getrandomdate(startdate, enddate):
    print("printing random date between",startdate,"and",enddate)
    randomgenerator=random.Random()
    dateFormat="%d-%m-%Y"
    startTime = time.mktime(time.strptime(startdate,dateFormat))
    endTime = time.mktime(time.strptime(enddate,dateFormat))
    randomTime = startTime + randomgenerator.random() * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("random date = ", getrandomdate("01-01-1963","31-12-2020"))