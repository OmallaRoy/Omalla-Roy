
import math # importing of the math library


while True:
    try:
        fact = int(input("Enter a whole number:")) # for user input
        
        if fact < 0:
                print("Enter in a positive whole number")
                continue
        result = math.factorial(fact)
               
    
    except ValueError:
        print("Invalid input! Please enter a whole number")
    else:
        print(f"The result is: {result}")
        break
