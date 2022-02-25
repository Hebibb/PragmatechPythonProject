


class Aircrafts():
    def __init__(self,name,speed,flight_dist,flight_h):
        self.name=name
        self.speed=speed
        self.flight_dist=flight_dist
        self.flight_h=flight_h
    def started(self):
        return f'The aircraft {self.name} is preparing to fly'
    def flight(self):
        pass
    def explanation(self):
        return f'{self.name} can fly at {self.speed}km/hour for {self.flight_h} hours and about {self.flight_dist}km far'
    
class Pass_Airc(Aircrafts):# inheritance
    def __init__(self,name,speed,flight_dist,flight_h,passengers,ferry_cap):
        super().__init__(name,speed,flight_dist,flight_h)
        self.passengers=passengers
        self.f_capacity=ferry_cap
      
        
    def flight(self,launch_type):#polymorphism
        if self.speed>150:
            return f'{self.name} is flying off  aerodrom {launch_type} '
        else: return '{self.name} Cannot fly'

    

boeing=Pass_Airc('boeing', 350, 20003,25,350,400)
print(boeing.explanation())#inheritance
print(boeing.flight('Horizontally'))#polymorphism
boeing.name='Hurjet'
print(boeing.started())
        
        
        
    
    
# class Mil_Airs(Aircrafts):
#     def __init__(self, mtype,amm_capacity,):
#         self.mtype=mtype
#         self.amm_capacity=amm_capacity
#         super().__init__('Military Aircraft')
        
        
# class Jets(Mil_Airs):
#     def __init__(self, amm_type,armor,fight_class):
#         self.amm_type=amm_type
#         self.armor=armor
#         self.fight_class=fight_class
#         super().__init__('Fighter Jet')
    





























    
    
    

        
