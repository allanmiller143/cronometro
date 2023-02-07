import time

def cronometro(t):
    while t:
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs) 
        print(timer,end=  "\r")
        time.sleep(1)
        t -=1
    print("tempo finalizado")
    
t = int(input("quanto tempo: "))  

cronometro(t)  