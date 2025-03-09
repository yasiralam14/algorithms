import math
def karatsuba_multiply(num1,num2):
    
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) == 1 and len(num2) == 1:
        return int(num1)*int(num2)
    if len(num1)>len(num2):
        number_zeros = len(num1) - len(num2)
        num2 = '0'*number_zeros + num2
    elif (len(num1)<len(num2)):
        number_zeros = len(num2) - len(num1)
        num1 = '0'*number_zeros + num1
    if len(num1)%2 ==1:
        num1 ='0'+num1
    if len(num2)%2 ==1: 
        num2 = '0'+num2
    
    
    num1_length = len(num1)
    num2_length = len(num2)
    
    half_length_1 = math.floor(num1_length/2)
    half_length_2 = math.floor(num2_length/2)
    a = num1[0:half_length_1]
    b = num1[half_length_1:]
    c = num2[0:half_length_2]
    d = num2[half_length_2:]
   
    ac = karatsuba_multiply(int(a),int(c))
    bd = karatsuba_multiply(int(b),int(d))
    ad = karatsuba_multiply(int(a),int(d))
    bc = karatsuba_multiply(int(b),int(c))
    middle = ad + bc
    result = 10**(num1_length)*ac + 10**(num1_length/2)*middle + bd
    
    return int(result)
    
print(karatsuba_multiply(200,30))
    
print(karatsuba_multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
    