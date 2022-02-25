from Implementation_Model import *

def stateThing():
   power = Power("Power")
   switch = Switch("Switch")

   and1 = AndGate("and1")
   and2 = AndGate("and2")
   and3 = AndGate("and3")
   not1 = NotGate("not1")

   jk1 = JKFlipFlop("jk1")
   jk2 = JKFlipFlop("jk2")

   # The power connecting to the switch (top-left)
   powerswitch = Connector(power, switch)
   # The top-left `and` connecting switch and jk2
   Connector(jk2, and1)
   Connector(switch, and1)
   #  The top-right `not` connecting switch
   Connector(switch, not1)
   # The top-right `and1` and `not1` connecting to jk1
   Connector(not1, jk1)
   Connector(and1, jk1)
   # The bottom-left `and2` connecting switch and jk1
   Connector(switch, and2)
   Connector(switch, jk1)
   #  The `and2` and power connecting to jk2
   Connector(and2, jk2)
   Connector(power, jk2)
   #  The right `and3` connecting from jk1 and jk2
   Connector(and3, jk1)
   Connector(and3, jk2)

   return and3.getOutput()


print(stateThing())




   



