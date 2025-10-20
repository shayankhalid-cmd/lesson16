class vehicle:
    def __init__ (self,milage,max_speed):
        self.milage = milage
        self.max_speed = max_speed
modelX = vehicle(18,240)
print("model max speed is",modelX.max_speed)
print("model milage is",modelX.milage)