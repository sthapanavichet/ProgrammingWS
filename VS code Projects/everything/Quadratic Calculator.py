#quadratic root function
def quadroot(x=[]):
    a = x[0]
    b = x[1]
    c = x[2]
    delta = (b**2 - (4*a*c))
    ans1 = (-b + sqrt(delta)) / (2*a)
    ans2 = (-b - sqrt(delta)) / (2*a)
    ans = [ans1, ans2]
    return ans



print("Quadratic eqautions form: ax^2 + bx + c")
from cmath import sqrt
import math
import os
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
Eq = [a, b, c]


if(a == 0.0 or b == 0.0 or c ==0.0):
    print("Enter a valid value")
else:
    if(a==1.0 and b==1.0):
        print("Your Quadratic Equation: " + "x^2 + " + "x + " + str(int(c)))
    elif(a==1.0):
        print("Your Quadratic Equation: " + "x^2 + " + str(int(b)) + "x + " + str(int(c)))
    elif(b==1.0):
        print("Your Quadratic Equation: " + str(int(a)) + "x^2 + " + "x +" + str(int(c)))
    else:
        print("Your Quadratic Equation: " + str(int(a)) + "x^2 + " + str(int(b)) + "x + " + str(int(c)))
    delta = (b**2 - (4*a*c))
    ans1 = (-b + sqrt(delta)) / (2*a)
    ans2 = (-b - sqrt(delta)) / (2*a)
    if(delta > 0):
        print("Answer for this Equation:" + str(ans1.real) + " and " + str(ans2.real))
    elif(delta < 0):
        print("Answer for this Equation:" + str(ans1) + " and " + str(ans2))
    elif(delta == 0):
        print("Answer for this Equation:" + str(ans1.real))
    else:
        print("Equation has no solution")
    print(quadroot(Eq))