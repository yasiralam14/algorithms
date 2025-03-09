import math
import random
def karatsuba_multiply(num1,num2):
    
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) == 1 and len(num2) == 1:
        return int(num1)*int(num2)
    
    
    
    num1_length = len(num1)
    num2_length = len(num2)
    
    half_length_1 = int(num1_length/2)
    half_length_2 = int(num2_length/2)
    a = num1[0:half_length_1]
    b = num1[half_length_1:]
    c = num2[0:half_length_2]
    d = num2[half_length_2:]
    #print (f"a:{a} b: {b} c {c} d: {d}")

    if len(a) <1 or len(a) <1 or len(a) <1 or len(a) <1 :
        print (f"a:{a} b: {b} c {c} d: {d}")
   
   # print(f"calculating ac where a = {a} and c = {c}")
    ac = karatsuba_multiply(a,c)
   # print(f"calculating bd where b = {b} and d = {d}")
    bd = karatsuba_multiply(b,d)
   # print(f"calculating ad where a = {a} and d = {d}")
    ad = karatsuba_multiply(a,d)
   # print(f"calculating bc where b = {b} and c = {c}")
    bc = karatsuba_multiply(b,c)
    middle = ad + bc
    n_by_2 = int(num1_length/2)
    result = int(10**(num1_length)*ac) + int(10**(n_by_2)*middle) + int(bd)
    
    return int(result)

#print(karatsuba_multiply(3,2))
#print(karatsuba_multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))

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


number1 = 1578470935938730
number2 = 2788473208391899

a = 15784709
b = 35938730
c = 27884732
d= '08391899'

ac = karatsuba_multiply(a,c)
bd = karatsuba_multiply(b,d)
ad = karatsuba_multiply(a,d)
bc = karatsuba_multiply(b,c)

print(f"ac = {ac} and python ac = {a*c}")
print(f"bd = {bd} and python bd = {b*int(d)}")
print(f"ad = {ad} and python ad = {a*int(d)}")
print(f"bc = {bc} and python bc = {b*c}")

middle = ad + bc
n = len(str(a))*2
n_by_2 = int(n/2)
result = int(10**(n)*ac) + int(10**(n_by_2)*middle) + int(bd)

print(f"our result {result} with lenght {len(str(result))} pythons result {number1*number2} with length = {len(str(number1*number2))} and the difference is {number2*number1 - result} here n = {len(str(a))} and n/2 = {int(len(str(a))/2)} and both matches =  {result == number1*number2}")

print(f"does multiplying the big guys matches = {karatsuba_multiply(1578470935938730,2788473208391899)==2788473208391899*1578470935938730}")

print(karatsuba_multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))