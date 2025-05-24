
# print("You are welcome,please enter in any two numbers ready for division!")



# while True:
#          num1 = int(input("Enter in the first number"))
#          num2 = int(input("Enter in the second number"))
#         try:
#             result = num1/num2
#             if  not type(num1 or num2) is int:
#                raise TypeError("Only integers are allowed")
#         except ZeroDivisionError:
#             print("Please you cannot divide by zero!Enter in another number") 
                                
#         except TypeError as e:
#             print(f"Not a number:{e}")
             
#         else:
#         break
#     print(result)
          
             


print("You are welcome, please enter any two numbers ready for division!")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
    except ZeroDivisionError:
        print("You cannot divide by zero! Try again.\n")
    except ValueError:
        print("Invalid input! Please enter only numbers.\n")
    else:
        print(f"Result: {result}")
        break
