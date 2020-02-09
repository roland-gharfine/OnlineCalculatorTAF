from time import *
import datetime

class logger():
    def __init__(self):

        self.Log("Logger intiialized")

    def LogError(self, errMsg):
        timestamp = self.getTimestamp()
        date = self.getDate()
        fh = open("..\\logs\\OnlineCalculatorTAF_" + date + ".error.log", "a")
        fh.write(timestamp + "," + errMsg + "\r\n")
        fh.close()

    def Log(self, msg):
        timestamp = self.getTimestamp()
        date = self.getDate()
        fh = open("..\\logs\\OnlineCalculatorTAF_" + date + ".default.log", "a")
        fh.write(timestamp + "," + msg  + "\r\n")
        fh.close()


    def getTimestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def getDate(self):
        return datetime.date.today().strftime("%Y%m%d")

