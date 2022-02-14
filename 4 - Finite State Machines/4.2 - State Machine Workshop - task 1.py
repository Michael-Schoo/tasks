import time
from typing import Literal

# set initial state 
# door is closed 
door: Literal["open" , "closed"] 
position :Literal["opening", "closing", "stopped", "" ]
door = "closed" 
position = ""
print("Door is", door) 
# repeat forever 
while True: 
    
    # ask user for input 
    instruction = input("User input: ") 
    # transition to opening state 
    if instruction == "b" and door == "closed": 
        position = "opening" 
    # transition to open state 
    elif instruction == "s" and position == "opening": 
        door = "open" 
    # transition to stopped 
    elif instruction == "b" and position == "opening": 
        position = "stopped" 
    # transition to closing state 
    elif instruction == "b" and door == "open": 
        position = "closing" 
    # transition to closed state 
    elif instruction == "s" and position == "closing": 
        position = "stopped" 
    elif instruction == "b" and position == "stopped" and door == "closed":
        position = "opening"
    elif instruction == "b" and position == "stopped" and door == "open":
        position = "closing"

    # print the current state of the door 
    print("Door is",  position if position != "" else door)

    if position == "closing":
        # wait 5 seconds then transition to closed state
        time.sleep(1)
        instruction = input(". ") 
        if instruction == "s" and position == "opening": 
            door = "open" 
            print("Cancled")
            continue
        time.sleep(1)
        instruction = input(".. ") 
        if instruction == "s" and position == "opening": 
            door = "open" 
            print("Cancled")
            continue
        time.sleep(1)
        instruction = input("... ") 
        if instruction == "s" and position == "opening": 
            door = "open" 
            print("Cancled")
            continue
        time.sleep(1)
        instruction = input(".... ") 
        if instruction == "s" and position == "opening": 
            door = "open"
            print("Cancled")
            continue
        time.sleep(1)
        instruction = input("..... ") 
        if instruction == "s" and position == "opening": 
            door = "open" 
            print("Cancled")
            continue
        
        door = "closed"
        position = ""
    elif position == "opening":
        # wait 5 seconds then transition to open state
        time.sleep(1)
        instruction = input(". ") 
        if instruction == "s" and position == "opening": 
            door = "open" 
            print("Cancled")
            continue
        time.sleep(1)
        instruction = input(".. ") 
        if instruction == "s" and position == "opening": 
            door = "open"
            print("Cancled") 
            continue
        time.sleep(1)
        instruction = input("... ")
        if instruction == "s" and position == "opening": 
            door = "open" 
            print("Cancled")
            continue
        time.sleep(1)
        instruction = input(".... ") 
        if instruction == "s" and position == "opening": 
            door = "open" 
            print("Cancled")
            continue
        time.sleep(1)
        instruction = input("..... ") 
        if instruction == "s" and position == "opening": 
            door = "open"
            print("Cancled")
            continue
        
        door = "open"
        position = ""
    