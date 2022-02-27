from Implementation_Model import *
# trying to make it... but made a better version directly on the file Implementation_Model

# This code also does not work, because the code was rewrite.
def stateThing():
   # start

   power = Power("Power")
   switch = Switch("Switch")

   and1 = AndGate("and1")
   and2 = AndGate("and2")
   and3 = AndGate("and3")
   not1 = NotGate("not1")
   not2 = NotGate("not1")

   jk1 = JKFlipFlop("jk1")
   jk2 = JKFlipFlop("jk2")

   # The power connecting to the switch (top-left)
   a= Connector(power, switch)
   # The top-left `and1` connecting switch and jk2
   b=Connector(switch, and1)
   c=Connector(jk2, and1)
   # The top-right `not1` connecting switch
   d=Connector(switch, not1)
   # The top-right `and1` and `not1` connecting to jk1
   e=Connector(not1, jk1)
   f=Connector(and1, jk1)
   # The bottom-left `and2` connecting switch and jk1
   h=Connector(switch, and2)
   i=Connector(switch, jk1)
   # The `and2` and power connecting to jk2
   j=Connector(and2, jk2)
   k=Connector(power, jk2)
   # The `not2` and power connecting to jk1
   l=Connector(not2, jk1)
   # The right `and3` connecting from jk1 and jk2
   m=Connector(and3, not2)
   n=Connector(and3, jk2)

   list1 = []
   for i in range(8):
      and3.performGateLogic()
      print(and3.getOutput())
      print("\n")
      list1.append(and3.getOutput())
   return list1
   # return and3.getOutput()


print(stateThing())




   



