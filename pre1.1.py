def gcd_fun (x, y):  
    if (y == 0):  
        return x  
    else:  
        return gcd_fun (y, x % y)  
x =int (input ("Enter the first number: ")) 
y =int (input ("Enter the second number: "))    
num = gcd_fun(x, y) 
print("GCD of two number is: ")  
print(num) 