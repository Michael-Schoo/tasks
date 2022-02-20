import time

lightSensorL = False
lightSensorR = False
bumpSensor = False
switch = True

motorA = 50
motorB = 50

while True:
    while switch:
        print(lightSensorL, lightSensorR, bumpSensor)
        if bumpSensor:
            motorA = 100
            motorB = 100
            # wait 1 second then turn 180 degrees
            print((motorA, motorB))
            motorA = 75
            motorB = -75
            time.sleep(1)
            print((motorA, motorB))
        elif not lightSensorL and not lightSensorR:
            motorA = 0
            motorB = 0
        elif lightSensorL:
            motorA = 25
            motorB = 75
        elif lightSensorR:
            motorA = 75
            motorB = 25
        else:
            motorA = 50
            motorB = 50
        
        match input((motorA, motorB)):
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
    # turn back on the switch - possibly
    if input("") == "s": switch = True
        