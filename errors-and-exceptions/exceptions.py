# catch the errors using except block and do the processing accordingly
# put the code which needs to be under check in 'try' block
# read more about asset(), raise and class of exceptions

try:
    n = int(input("Enter a Number : "))
    m = 1 / n
    print(f"1/(number you entered) = {m}")
except ValueError:
    print("Please enter an Integer")
except ZeroDivisionError:
    print("We can't divide any number by zero, please enter a valid number")
except:
    print("Something went wrong! Please reachout to Admin for more details")
