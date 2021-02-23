import pyautogui as pg
import time

#check startPoint
#x=pg.position()
#print(x)

def autoCopypaste(x=0):
    
    time.sleep(1)
#startPoint = pg.position()
#print(startPoint)
#(x=160, y=253)

    startPoint = (160,253+x)
    pg.click(startPoint,button='left')
#check endPoint
#endPoint = pg.position()
#print(endPoint)
#(x=445, y=253)

    time.sleep(1)
    endPoint = (445,253+x)
    pg.dragTo(endPoint,duration=2,button='left')

#copy
    time.sleep(1)
    pg.hotkey('command','c')

#left untitled2 to untitle
#(310,182)
    time.sleep(1)
    lefttoUntiltled = (310,182)
    pg.click(lefttoUntiltled,button='left')

#paste
    time.sleep(1)
    pg.click(startPoint,button='left')
    pg.hotkey('command','v')

#back to untitled2 
#(800,182)
    time.sleep(1)
    lefttoUntiltle = (800,182)
    pg.click(lefttoUntiltle,button='left')

#runProgram
#autoCopypaste()
#autoCopypaste(40)
#autoCopypaste(80)

#forLoop
for i in range(3):
    autoCopypaste(40*i)




