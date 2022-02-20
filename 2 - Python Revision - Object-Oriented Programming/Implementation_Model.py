
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
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
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

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
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

    def performGateLogic(self):

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

    def performGateLogic(self):

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

    def performGateLogic(self):

        a = self.getPinA()
        return not a


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