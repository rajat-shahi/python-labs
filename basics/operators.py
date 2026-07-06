# if both the numbers are integers then the result will be integer as well (exponentiation, multiplication)
# if any one of them is float, the result will be float as well 

print(2**3)
print(2.**3)
print(2**3.)
print(2.**3.)

print(2*3)
print(2.*3)
print(2*3.)
print(2.*3.)

# Division operator always returns float as result

print(10/2)
print(10./2)
print(10/2.)
print(10./2.)

# Floor Division / Integer Division => takes the floor of the result 
print(10//2)
print(10.//2)
print(10//2.)
print(10.//2.)

print(6./4)
print(6.//4)
print(6./-4)
print(6.//-4)

# modulo operator

print(4%2)
print(5%2)

# addition and subtraction for doing the respective operations
print(10-5)
print(10+5)

# Unary Operators 
print(-6-6)
print(10 - -6)

# priority pyramid (highest to lowest): Unary(+.-) => (**) => (*,/,//,%) => Binary(+,-)
# if same priority then from "left to right"
# sub-expressions (under parentheses) are always calculated first