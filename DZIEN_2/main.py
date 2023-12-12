from  oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

print("________________ klasa OldResistor _______________")
r0 = OldResistor(10.2E2)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("________________ klasa Resistor _______________")
r1 = Resistor(50E3)
r1.ohms = 18.3
print(f'układ elektryczny:\noporność: {r1.ohms} omów\nnapięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A\n')

print("________________ klasa VoltageResistance _______________")
r2 = VoltageResistance(1E3)
print(f'początkowe natężenie prądu: {r2.current} A')
r2.voltage = 39
print(f'napięcie prądu: {r2.voltage} V')
print(f'natężenie prądu: {r2.current} A')
