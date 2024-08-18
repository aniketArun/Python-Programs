class Fibbonacci:
    def __init__(self, number) -> None:
        self.number = number
        self.series = []

    def fibbonacciSeries(self)->list:
        if self.number == 0:
            print('Enter the value greater than 0')
        elif self.number == 1:
            self.series.append(1)
        else:
            first = 0
            second = 1
            
            for i in range(self.number):
                self.series.append(first)
                sum = first + second
                first = second
                second = sum
        return self.series
    
#driver code

obj = Fibbonacci(int(input('Enter how element you want ? :')))

print("Required Fibbonacci series is : ", obj.fibbonacciSeries())