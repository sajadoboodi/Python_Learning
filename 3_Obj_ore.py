class Computer:
    count = 0
    def __init__(self,ram,hard,cpu):
        Computer.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
    
    def value(self):
        return (self.ram*500)+(self.hard*10)+(self.cpu*1000)
    
    def __del__(self):
        Computer.count -= 1

    
class Laptop(Computer):

    def value(self):
        return super().value()+(self.size*800)
    



pc1 = Computer(16,1,7)
print(pc1.value())

pc2 = Computer(32,1,9)
print(pc2.value())

lap1 = Laptop(31,1,7)
lap1.size = 16
print(lap1.value())
print(Computer.count)
pc2.__del__()
print(Computer.count)