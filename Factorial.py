class Main():
    def factorial_iterative(self, number)->int:
        # if number is 0 or 1 return 1
        if(number == 0 or number == 1):
            return 1
        # initialize the variable which will keep the track of value
        factorial = 1
        #iterate over number
        while(number):
            factorial *= number
            number -= 1 #reduce the number each time by one
        return factorial #finally return the value of factorial 
    

    def factorial_recursive(self, number)->int:
        #if the number 0 or 1 return 1
        if(number == 1 or number == 0):
            return 1
        #if number is not 0 or 1 make a recursive call 
        return (number * self.factorial_recursive(number-1)) 
    
#driver code
#create object of the class
obj = Main()

print(obj.factorial_iterative(5))
print(obj.factorial_recursive(5))