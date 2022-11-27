from colorama import Fore, Back, init
import sys

class calculator:
    def __init__(self, x, y):
        self.x = int(input("Write first number: "))
        self.y = int(input("Write second number: "))
    
    def multiply(self):
        return self.x * self.y
                     
    def substract(self):
        return self.x - self.y
                     
    def divide(self):
        return self.x / self.y
     
    def add(self):
        return self.x + self.y
    
    def modulus(self):
        return self.x % self.y
                       
    def double(self):
        return self.x ** self.y
    
init(convert=True)

print(Back.GREEN + Fore.RED + 'Welcome to calculator!')
print('1. Add')
print('2. Multiply')
print('3. Substract')
print('4. Divide')
print('5. Modulus')
print('6. Double')

choice = input("Enter choice: ")
    
user_input = calculator(0, 0)



    
if choice in('1', '2', '3', '4', '5', '6'):      
    if choice == '1':
        add_num = user_input
        print(add_num.add())
        input()
        sys.exit()
    if choice == '2':
        multiply_num = user_input
        print(multiply_num.multiply())
        input()
        sys.exit()
    if choice == '3':
        substract_num = user_input
        print(substract_num.substract())
        input()
        sys.exit()
    if choice == '4':
        divide_num = user_input
        print(divide_num.divide())
        input()
        sys.exit()
    if choice == '5':
        modulus_num = user_input
        print(modulus_num.modulus())
        input()
        sys.exit()
    if choice == '6':
        double_num = user_input
        print(double_num.double())
        input()
        sys.exit()
