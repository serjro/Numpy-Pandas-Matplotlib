import time, os
class TrafficLight:
    __color=["\033[31m {}","\033[33m {}","\033[32m {}"]
    __timer = [7,2,3]
    def running(self):
        i=1
        while i>0:
            print("\n" * 47)
            print(TrafficLight.__color[i-1].format("TrafficLight"))
            time.sleep(TrafficLight.__timer[i-1])
            i=i+1
            if i>3: i=1
a=TrafficLight()
a.running()