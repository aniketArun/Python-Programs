class OddEven():
    def __init__(self, number) -> None:
        self.num = number
    
    def check_odd_even(self) -> str:
        '''alternate way:
        if self.num % 2 == 0:
            return "Even"
        else:
            return "Odd"
        '''

        #this can be written in one line as follows->
        return "Odd" if self.num % 2 != 0 else "Even" 

#driver code

Number = OddEven(int(input('Enter the Number: ')))

print(Number.check_odd_even())