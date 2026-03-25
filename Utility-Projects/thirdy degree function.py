import math
def test_roots(a, b, c, d):
    Root_test = -abs(d)#turn the 'd' value into negative, to calculate the divisors without errors
    while Root_test <= abs(d):
        if Root_test != 0 and d % Root_test == 0:
            x = Root_test
            y = a * (x ** 3) + b * (x ** 2) + c * x + d
            if y == 0:
                x1 = x
                return x1
                
        Root_test = Root_test + 1
#calculates all the values of the second degree polynomial
def second_degree(a, b, c, x1):
    Quad_a = a
    Quad_b = x1 * a + b
    Quad_c = x1 * Quad_b + c
    delta = Quad_b ** 2 - (4 * Quad_a * Quad_c)
    if delta < 0:
        print ("this function do not has real matematic roots")
    else:#calculate the roots of polynomial, reducing to the first degree form
        x2 = ((-Quad_b + math.sqrt(delta)) / (2 * Quad_a))
        x3 = ((-Quad_b - math.sqrt(delta)) / (2 * Quad_a))
        return x2, x3
try: #ask to the user about her polynomial.
    a_value = float(input("what is the a value?"))
    b_value = float(input("what is the b value?"))
    c_value = float(input("what is the c value?"))
    d_value = float(input("what is the d value?"))
except ValueError:#avoid errors, if the user type letters in the input
    print("you have to type a number!")
x1 = test_roots(a_value, b_value, c_value, d_value)
x2, x3 = second_degree(a_value, b_value, c_value, x1)
print (f"the value of polynomial roots is:")
print (f"the value of x1 its {x1}")
print (f"The value of x2 its {x2}")
print (f"The value of x3 its {x3}")
print (f"the polynomial, reduced to the first-degree form is:")
print (f"(x-{x1})(x-{x2})(x-{x3})")