import math
def second_degree (a, b, c):
    #ask to the user what is her polynomial
    delta = b ** 2 - (4 * a * c)
    #calculates delta
    if delta < 0: 
        return None
    else: #calculate the roots
        x1 = ((-b + math.sqrt(delta)) / (2 * a))
        x2 = ((-b - math.sqrt(delta)) / (2 * a))
        return x1, x2
def calculate_y (a, b, c, x1, x2):
    results = []
    if x1 < x2:#calculate all the int numbers of x between the roots
        x = x1
        x = math.ceil(x)
        while x <= x2:
            y = a * (x ** 2) + b * x + c
            results.append((x, y))
            x = x + 1
        
    else: #avoid errors if x2 > x1
            x = x2
            x = math.ceil(x)
            y = a * (x ** 2) + b * x + c
            while x <= x1:
                y = a * (x ** 2) + b * x + c
                results.append((x, y))
                x = x + 1
    return results
a_value = float(input("What is the a value?"))
b_value = float(input("what is the b value?"))
c_value = float(input("what is the c value?"))
roots = second_degree(a_value, b_value, c_value)
if roots:
     x1, x2 = roots
     print(f"x1 ={x1}")
     print(f"x2 ={x2}")
y_values = calculate_y (a_value, b_value, c_value, x1, x2)
print (y_values)



