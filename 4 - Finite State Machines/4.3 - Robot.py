import time

lightSensorL = False
lightSensorR = False
bumpSensor = False
switch = True

moterA = 50
moterB = 50

while True:
    while switch:
        print(lightSensorL, lightSensorR, bumpSensor)
        if bumpSensor:
            moterA = 100
            moterB = 100
            # wait 1 seccond then turn 180 degrees
            print((moterA, moterB))
            motorA = 75
            motorB = -75
            time.sleep(1)
            print((moterA, moterB))
        elif not lightSensorL and not lightSensorR:
            motorA = 0
            motorB = 0
        elif lightSensorL:
            moterA = 25
            moterB = 75
        elif lightSensorR:
            moterA = 75
            moterB = 25
        else:
            moterA = 50
            moterB = 50
        
        match input((moterA, moterB)):
            case "l":
               if (lightSensorL): lightSensorL = False
               else: lightSensorL = True
            case "r":
                if (lightSensorR): lightSensorR = False
                else: lightSensorR = True
            case "b":
                if (bumpSensor): bumpSensor = False
                else: bumpSensor = True
            case "s":
                if (switch): switch = False
                else: switch = True

    if input("") == "s": switch = True
        