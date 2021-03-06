#Day07-0506.py

from datetime import datetime
import webbrowser

print(datetime.today().strftime("%Y-%m-%d %H:%M"))

class Car:
    
    iSerialNum = 0
    sColourCode = ""
    iMaxSpeed = 0
    iSpeed = 0
    bAudio = False
    sFrom = ""
    sTo = ""
        
    def __new__(cls,  sColourCode, iMaxSpeed, iSpeed):
        print("New")
        return super().__new__(cls)
                        
    def __init__(self,  sColourCode, iMaxSpeed, iSpeed):
        Car.iSerialNum += 1
        self.sColourCode = sColourCode
        self.iMaxSpeed = iMaxSpeed
        self.iSpeed = iSpeed
        print(f"{self.iSerialNum}, Init!")
        
    def horn(self):
        print(f"{self.iSerialNum}, Horn!")
    
    def audio(self):
        self.bAudio = not self.bAudio
        print(f"{self.iSerialNum}, Audio = {self.bAudio}")
    
    def changeSpeed(self, iSpeed):
        
        if iSpeed > 0:
            self.iSpeed = min(self.iMaxSpeed, iSpeed)
        else:
            self.iSpeed = 0 
            
        print(f"{self.iSerialNum}, Speed = %d" %(self.iSpeed))
        
    def navigation(self, sFrom, sTo):
        
        self.sFrom = sFrom
        self.sTo = sTo
        sUrl = f"https://www.google.co.kr/maps/dir/{self.sFrom}/{self.sTo}"
        
        webbrowser.open(sUrl)
        
    def setHere(self, sHere):
        
        if self.sTo == sHere:
            print("Arrived")
        else:
            print("Go!")
            

class Bus(Car):
    
    bBell = False
    iMaxPassenger =0
    
    def bell(self):
        self.bBell = not self.bBell
        print(f"{self.iSerialNum}, bBell = {self.bBell}")
    
bus1 = Bus("BUS-5",100, 50)
bus1.bell()
bus1.bell()
bus1.bell()

bus1.navigation("천호동+서울특별시+강동구", "굽은다리역+서울특별시")

bus1.setHere("Seoul")
bus1.setHere("Daegu")
bus1.setHere("Busan")

car1 = Car("CAR-1", 100, 50)
car1.horn()
car1.audio()
car1.audio()
car1.audio()
car1.changeSpeed(100)
car1.changeSpeed(130)
car1.changeSpeed(50)
car1.changeSpeed(0)
car1.changeSpeed(-1)

car2 = Car("CAR-2", 10, 5)
car2.horn()
car2.audio()

car2.changeSpeed(130)
car2.changeSpeed(50)
car2.changeSpeed(0)
car2.changeSpeed(-1)



    