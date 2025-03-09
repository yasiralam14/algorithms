import math
import random
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
   
    ac = karatsuba_multiply(a,c)
    bd = karatsuba_multiply(b,d)
    a_plus_b = int(a)+int(b)
    c_plus_d = int(c)+int(d)
    multiple = karatsuba_multiply(a_plus_b,c_plus_d)
    middle = multiple- int(ac) - int(bd)
    n= len(num1)
    n_by_2 = int(n/2)
    result = int(10**(n)*ac) + int(10**(n_by_2)*middle) + int(bd)
    
    return result


list_of_numbers = []
for i in range(6):
    digits = 2**(i+1)
    first_range = int('1'+'0'*(digits-1))
    second_range = int('9'*digits)
    for j in range(10):
        number1 = random.randint(first_range,second_range)
        number2 = random.randint(first_range,second_range)
        list_of_numbers.append((number1,number2))
        
for pair in list_of_numbers:
    test_result = karatsuba_multiply(pair[0],pair[1])
    python_result = pair[0]*pair[1]
    if test_result != python_result:
        print(f"The first number is {pair[0]} and the second number is {pair[1]}")
        print(f"What we got {test_result}")
        print(f"what python got {python_result}")
        print(f"Our length {len(str(test_result))}")
        print(f"Python length {len(str(python_result))}")
        break
    
