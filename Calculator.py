class Calculator:
    def __init__(self) -> None:
        self.number_01 = int(input('Enter the Number 1: '))
        self.number_02 = int(input('Enter the Number 2: '))

    def addition(self)->int:
        return self.number_01 + self.number_02

    def subtraction(self)->int:
        return self.number_01 - self.number_02

    def multiplication(self)->int:
        return self.number_01 * self.number_02
    
    def division(self)->int:
        return self.number_01 / self.number_02


    def display_menu(self):
        choice = int(input(f'Enter choice:\n\t1.Addition\n\t2.Substraction\n\t3.Multiplication\n\t4.Division\n\t0.exit'))
        
        if choice == 1:
            print(self.addition())
        
        elif choice == 2:
            print(self.subtraction())
        
        elif choice == 3:
            print(self.multiplication())

        elif choice == 4:
            if self.number_02:
                print(self.division())
            else:
                print("Math Error")

        elif choice == 0:
            print("Good Bye :)")
        
        else:
            print("Sorry ! Wrong input !")

ob = Calculator()
