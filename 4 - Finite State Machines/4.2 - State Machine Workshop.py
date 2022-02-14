# set initial state 
# door is closed 
door = "closed" 
print("Door is", door) 
# repeat forever 
while True: 
    # ask user for input 
    instruction = input("User input: ") 
    # transition to opening state 
    if instruction == "b" and door == "closed": 
        door = "opening" 
    # transition to open state 
    elif instruction == "s" and door == "opening": 
        door = "open" 
    # transition to closing state 
    elif instruction == "b" and door == "open": 
        door = "closing" 
    # transition to closed state 
    elif instruction == "s" and door == "closing": 
        door = "closed" 
    # print the current state of the door 
    print("Door is", door)
