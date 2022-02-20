
class LogicGate:
    """
    Listing 8
    """
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """
    Listing 9
    """
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))


class UnaryGate(LogicGate):
    """
    Listing 10
    """
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))


class AndGate(BinaryGate):
    """
    Listing 11
    """
    def __init__(self,n):
        super(AndGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class Connector:
    """
    Listing 12
    """
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

    tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
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

def getPinA(self):
    """
    Listing 14
    """
    if self.pinA == None:
        return input("Enter Pin A input for gate " + self.getLabel()+"-->")
    else:
        return self.pinA.getFrom().getOutput()