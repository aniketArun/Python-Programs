class Palindrome:
    def __init__(self) -> None:
        self.string = input('Enter the string: ')

    def __str__(self) -> str:
        reversed_str = ""
        length = len(self.string)-1
        while(length >= 0):
            reversed_str += self.string[length]
            length -= 1

        # print(reversed_str)
        return "Palindrome" if reversed_str == self.string else "Not Palindrome"

print(Palindrome())