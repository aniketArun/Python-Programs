class SlicingOfString():
    def __init__(self) -> None:
        self.word = input('Enter the String :')
        self.start = int(input('Enter Start Index : '))
        self.end = int(input('Enter End Index : '))

    def __str__(self) -> str:
        return self.word [self.start : self.end]
    
print(SlicingOfString())