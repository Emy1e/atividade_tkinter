from cmath import sqrt

class Calculadora:
    def __init__(self, num1, num2, operacao):
        self.num1 = num1
        self.num2 = num2
        self.operacao = operacao
    
    def calculo(self):
        resultado

        if self.operacao == "+":
            resultado = self.num1 + self.num2

        elif self.operacao == "-":
            resultado = self.num1 - self.num2
            
        elif self.operacao == "*":
            resultado = self.num1 * self.num2
        
        elif self.operacao == "/":
            resultado = self.num1 / self.num2
            
        elif self.operacao == "E":
            print(sqrt(self.num1), sqrt(self.num2))

        elif self.operacao == "F":
            resultado = self.num1 ** self.num2

        return resultado