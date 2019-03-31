class Bicycle:
    def __init__(self, gear, cadence):
        self.cadence = cadence
        self.gear = gear
        self.speed = self.gear*self.cadence
        if self.gear < 1 or self.gear > 7 or isinstance(self.gear,float):
            self.gear=None  
        if self.speed < 0 or self.speed > 1000:
            self.speed=None
        if self.cadence < 0: 
            self.cadence = None
 
    def __str__(self):
        str_to_print = f"""Bicycle attricutes:
            Cadence: {self.cadence}
            Gear: {self.gear}
            Speed: {self.speed}
            """
        return str_to_print

    def change_speed_to(self,new_speed):
        if self.gear == None or self.cadence == None:
            self.speed=0
        if isinstance(new_speed,str):
            self.speed = 0
        elif new_speed < 0:
            self.speed = 0
        elif new_speed >= 1000:
            self.speed=1000
        elif new_speed == 0:
            self.speed=0
        else:
            if self.gear != None and self.cadence != None and new_speed !=None and new_speed < 1000 and new_speed > 0:
                self.speed = new_speed
                if self.gear*self.cadence != new_speed:
                    if new_speed/self.cadence > 7:
                        self.cadence = new_speed/self.gear
                    elif isinstance((new_speed/self.cadence),int):
                        self.gear =  new_speed/self.cadence 
                    else:   
                        self.cadence = new_speed/self.gear

