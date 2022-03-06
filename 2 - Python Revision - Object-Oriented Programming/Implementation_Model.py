from time import sleep

# https://runestone.academy/ns/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#inheritance-logic-gates-and-circuits
"""
Changes to the original code:
 * Removed connectors and replaced them with passing the inputs into the class instead (implicit     connection)
 * Changed some of the wording of functions - separated some `performGateLogic()` into `calculate()`
 * ... (more)
"""

clock = 0
flip_flop_data: list[list[bool]] = []

class LogicGate:
    def __init__(self) -> None:
        self.clock = 0
        self.value = False

    def calculate(self) -> bool:
        raise NotImplementedError

    def performGateLogic(self) -> bool:
        if self.clock < clock:
            self.value = self.calculate()

        return self.value 

class AlwaysON(LogicGate):
    def calculate(self) -> bool:
        return True

class SWITCH(LogicGate):
    def __init__(self, parent: LogicGate, state: bool):
        super().__init__()
        self.parent = parent
        self.cond = state

    def toggle(self):
        self.cond = not self.cond

    def calculate(self) -> bool:
        return self.cond and self.parent.performGateLogic()

class PRINTER():
    def __init__(self, parent: LogicGate):
        self.parent = parent

    def execute(self) -> bool:
        return self.parent.performGateLogic()

class NOTGate(LogicGate):
    def __init__(self, parent: LogicGate):
        super().__init__()
        self.parent = parent

    def calculate(self) -> bool:
        return not self.parent.performGateLogic()

class ANDGate(LogicGate):
    def __init__(self, parent1: LogicGate, parent2: LogicGate):
        super().__init__()
        self.parent1 = parent1
        self.parent2 = parent2

    def implementation(self):
        res1 = self.parent1.performGateLogic()
        res2 = self.parent2.performGateLogic()
        return res1 and res2

    def calculate(self) -> bool:
        return self.implementation()

class NANDGate(ANDGate):
    def __init__(self, parent1: LogicGate, parent2: LogicGate):
        super().__init__(parent1, parent2)

    def calculate(self) -> bool:
        return not self.implementation()

class ORGate(LogicGate):
    def __init__(self, parent1: LogicGate, parent2: LogicGate):
        super().__init__()
        self.parent1 = parent1
        self.parent2 = parent2

    def implementation(self) -> bool:
        res1 = self.parent1.performGateLogic()
        res2 = self.parent2.performGateLogic()
        return res1 or res2

    def calculate(self) -> bool:
        return self.implementation()

class NORGate(ORGate):
    def __init__(self, parent1: LogicGate, parent2: LogicGate):
        super.__init__(parent1, parent2)

    def calculate(self) -> bool:
        return not self.implementation()

class XORGate(LogicGate):
    def __init__(self, parent1: LogicGate, parent2: LogicGate):
        super().__init__()
        self.parent1 = parent1
        self.parent2 = parent2

    def implementation(self) -> bool:
        result1 = self.parent1.performGateLogic()
        result2 = self.parent2.performGateLogic()

        return (result1 and not result2) or (not result1 and result2)


    def calculate(self) -> bool:
        return self.implementation()


class XNORGate(XORGate):
    def __init__(self, parent1: LogicGate, parent2: LogicGate):
        super().__init__(parent1, parent2)

    def calculate(self) -> bool:
        return not self.implementation()

# This implementation will only return Q
class JKFlipFlop(LogicGate):
    def __init__(self, parentj: LogicGate, parentk: LogicGate, id: int):
        super().__init__()
        self.parentj = parentj
        self.parentk = parentk
        
        flip_flop_data.insert(id, [False])
        self.id = id

    def set_latch(self, value: bool):
        flip_flop_data[self.id][clock] = value

    def calculate(self) -> bool:
        j = self.parentj.performGateLogic()
        k = self.parentk.performGateLogic()

        prev = flip_flop_data[self.id][clock - 1]

        if prev:
            flip_flop_data[self.id].append(not k)
        else:
            flip_flop_data[self.id].append(j)

        return prev

# A special type to resolve before definement problems
class JKFlipFlopReceiver(LogicGate):
    def __init__(self, id: int) -> None:
        super().__init__()
        self.id = id
    
    def calculate(self) -> bool:
        return flip_flop_data[self.id][clock - 1]

def main():
    print("Use 1 and 0 for the button press\n")
    switch = SWITCH(AlwaysON(), True)
    ffaand = ANDGate(switch, JKFlipFlopReceiver(1))
    ffa = JKFlipFlop(ffaand, NOTGate(switch), 0)
    ffa.set_latch(False)

    ffband = ANDGate(switch, NOTGate(JKFlipFlopReceiver(0)))
    ffb = JKFlipFlop(ffband, AlwaysON(), 1)
    ffb.set_latch(False)

    yand = ANDGate(NOTGate(ffa), ffb)

    y = PRINTER(yand)

    global clock
    i = 0
    while True:
        button = input("Button pressed? ")
        if not button.isdigit(): 
            print("Error, try again...\n")
            if "exit" in button.lower(): break
            continue
        switch.cond = bool(int(button))
        i += 1; clock = i
        print("Pulse sent" if y.execute() else "No pulse")
        print()
        sleep(0.1)

main()

tests = [
    ((0, 0, 0), (0, 0, 0)),
    ((0, 0, 1), (0, 1, 0)),
    ((0, 1, 0), (0, 0, 1)),
    ((0, 1, 1), (1, 0, 1)),
    ((1, 0, 0), (0, 0, 0)),
    ((1, 0, 1), (1, 0, 0)),
    # ((1, 1, 0), (X, X, X)),
    # ((1, 1, 1), (X, X, X)),
]

def test():
    global clock
    for (index, test) in enumerate(tests):
        clock = 0
        print("Testing", index)

        [init, next] = test

        switch = SWITCH(AlwaysON(), init[2])
        ffaand = ANDGate(switch, JKFlipFlopReceiver(1))
        ffa = JKFlipFlop(ffaand, NOTGate(switch), 0)
        ffa.set_latch(init[0])

        ffband = ANDGate(switch, NOTGate(JKFlipFlopReceiver(0)))
        ffb = JKFlipFlop(ffband, AlwaysON(), 1)
        ffb.set_latch(init[1])

        yand = ANDGate(NOTGate(ffa), ffb)

        tester = PRINTER(yand)

        # Initialize system
        tester.execute()

        clock += 1

        # Second
        assert next[2] == tester.execute()
        assert next[0] == flip_flop_data[0][1]
        assert next[1] == flip_flop_data[1][1]

    print("Tests finished")

# test()