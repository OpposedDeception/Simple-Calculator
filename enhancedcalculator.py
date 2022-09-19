import math

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def double(x, y):
    return x ** y

def percentage(x, y):
    return x % y

def math_sqrt(x):
    return math.sqrt(x)
    
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Double")
print("6.Percentage")
print("7.Square root")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number, not necessary if it is a square root: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", minus(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "**", num2, "=", double(num1, num2))
            
        elif choice == '6':
            print(num1, "%", num2, "=", percentage(num1, num2))
                    
        elif choice == '7':
            print(math.sqrt(num1), "=", math_sqrt(num1))
        
        
        new_calculation = input("Do we continue m8? (yep/nah): ")
        if new_calculation == "nah":
          break
        
     
    else:
        print("Bad input bro")
    
