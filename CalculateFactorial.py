class CalculateFactorial:
    def __init__(self):
        self.factorialNum = 0

    def CalculateFactorial(self, n):
        if n < 0:
            raise ValueError("Факторіал визначений лише для невід'ємних цілих чисел.")
        if n == 0 or n == 1:
            self.factorialNum = 1
            return 1
        else:
            result = n * self.CalculateFactorial(n - 1)
            self.factorialNum = resultca
            return result

    def GetFactorial(self):
        return self.factorialNum


