#CLASSE
class Calculadora():

    def __init__(self):
        self.a = 0
        self.b = 0
    
    def soma(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self):
        return self.a * self.b
    
    def divisao(self):
        return self.a / self.b
    
#inicio
c = Calculadora()

x = int(input())
y = int(input())

c.a = x
c.b = y 

print(c.multiplicacao())
