class vehicle:
    def __init__(self,name,fare):
        self.name = name
        self.fare = fare
class bus(vehicle):
    def __init__(self,name,fare,seating_capacity):
        super().__init__(name,fare)
        self.seating_capacity = seating_capacity
    def businfo(self):
        total_fare = self.fare * self.seating_capacity
        mantinance = 0.1 * total_fare
        total = (total_fare + mantinance)
        print(total)
obj = bus("School Volvo", 110, 50)
obj.businfo()