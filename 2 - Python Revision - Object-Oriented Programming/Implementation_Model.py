
import string


class LogicGate:
    """
    Listing 8
    """
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self) -> string:
        return self.label

    def getOutput(self) -> bool:
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """
    Listing 9
    """
    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self) -> bool:
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self) -> bool:
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class UnaryGate(LogicGate):
    """
    Listing 10
    """
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self) -> bool:
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"--> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    """
    Listing 11
    """
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self) -> bool:

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    """
    Listing 11 - made into `or`
    """
    def __init__(self,n):
        super(OrGate,self).__init__(n)

    def performGateLogic(self) -> bool:

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NotGate(BinaryGate):
    """
    Listing 11 - made into `not`
    """
    def __init__(self,n):
        super(NotGate,self).__init__(n)

    def performGateLogic(self) -> bool:

        a = self.getPinA()
        return not a

class NORGate(BinaryGate):
    """
    Listing 11 - made into `NOR`
    """
    def __init__(self,n):
        super(NotGate,self).__init__(n)

    def performGateLogic(self) -> bool:

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return not 1
        else:
            return not 0

class NANDGate(BinaryGate):
    """
    Listing 11 - made into `NAND`
    """
    def __init__(self,n):
        super(NotGate,self).__init__(n)

    def performGateLogic(self) -> bool:

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return not 1
        else:
            return not 0

class XORGate(BinaryGate):
    """
    Listing 11 - made into `XOR`
    """
    def __init__(self,n):
        super(NotGate,self).__init__(n)

    def performGateLogic(self) -> bool:

        a = self.getPinA()
        b = self.getPinB()
        if a!=b:
            return 1
        else:
            return 0
            
class XNORGate(BinaryGate):
    """
    Listing 11 - made into `XNOR`
    """
    def __init__(self,n):
        super(NotGate,self).__init__(n)

    def performGateLogic(self) -> bool:

        a = self.getPinA()
        b = self.getPinB()
        if a!=b:
            return not 1
        else:
            return not 0


class Connector(BinaryGate):
    """
    Listing 12
    """
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self) -> BinaryGate:
        return self.fromgate

    def getTo(self) -> BinaryGate:
        return self.togate
    

def setNextPin(self,source):
    """
    Listing 13
    """
    if self.pinA == None:
        self.pinA = source
    else:
        if self.pinB == None:
            self.pinB = source
        else:
           raise RuntimeError("Error: NO EMPTY PINS")


def getPinA(self) -> bool:
    """
    Listing 14
    """
    if self.pinA == None:
        return input("Enter Pin A input for gate " + self.getLabel()+"--> ")
    else:
        return self.pinA.getFrom().getOutput()



# make a JK Flip Flop
class JKFlipFlop(BinaryGate):
    """
    Listing - GitHub Copilot
    """
    def __init__(self,n):
        super(JKFlipFlop,self).__init__(n)
        self.pinJ = None or self.pinA
        self.pinK = None or self.pinB
        self.pinQ = None
        self.pinQ_ = None

    def getPinJ(self) -> bool:
        if self.pinJ == None:
            return int(input("Enter Pin J input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinJ.getFrom().getOutput()

    def getPinK(self) -> bool:
        if self.pinK == None:
            return int(input("Enter Pin K input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinK.getFrom().getOutput()

    def getPinQ(self) -> bool:
        if self.pinQ == None:
            return int(input("Enter Pin Q input for gate "+self.getLabel()+"--> "))
        else:
            return self.pnQ.getFrom().getOutput()
    
    def getPinQ_(self) -> bool:
        if self.pinQ_ == None:
            return int(input("Enter Pin Q_ input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinQ_.getFrom().getOutput()

    def performGateLogic(self) -> tuple[bool, bool]:

        # j = self.getPinJ()
        # k = self.getPinK()
        # q = self.getPinQ()
        # q_ = self.getPinQ_()

        # t1 = not (j and q_)
        # b1 = not (k and q )

        # t2 = not (b2 and t1)
        # b2 = not (t2 and b1)
        self.q = 0
        self.j = self.getPinJ()
        self.k = self.getPinK()
        if (self.j == 1):
            self.q=1
        elif (self.k == 1):
            self.q=0
        elif (self.k == 0):
            self.q=1
        
        #       Q   
        return self.q


class Power(UnaryGate):
    """

    """
    def __init__(self,n):
        super(Power,self).__init__(n)

    def performGateLogic(self) -> bool:

        # a = self.getPin()
        return 1

class Switch(UnaryGate):
    """

    """
    def __init__(self,n):
        super(Switch,self).__init__(n)

    def performGateLogic(self) -> bool:

        a = self.getPin()
        return a


# construct the circuit by creating all of the gates you need and connecting them up according to the schematic provided. (jk flipflop)
