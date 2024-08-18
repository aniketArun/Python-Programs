class PrimeNumber:
    def __init__(self, number) -> None:
        self.num = number

    def check_prime(self) -> str:
        for i in range(2, self.num): #iterative logic
            if(self.num % i == 0):
                return "Not Prime"
        return "Prime"

#driver code 

ob = PrimeNumber(3)

print(ob.check_prime())