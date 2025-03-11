test_list = [1,2,3]

def count_inversion_with_mergesort(array):
    count = 0
    if len(array)<=1:
        
        return array,count
    else:
        middle = int(len(array)/2)
        left = array[0:middle]
        right = array[middle:]
        left,left_counts = count_inversion_with_mergesort(left)
        right,right_counts = count_inversion_with_mergesort(right)
        count = count + left_counts + right_counts
        lefts_index =0
        right_index =0
        temp_arra =[]
        for i in range(len(array)):
            if lefts_index >=len(left):
                temp_arra.extend(right[right_index:])
                return temp_arra,count
            elif right_index>= len(right):
                temp_arra.extend(left[lefts_index:])
                return temp_arra,count
            if left[lefts_index]<=right[right_index]:
                temp_arra.append(left[lefts_index])
                lefts_index = lefts_index+1
            else:
                temp_arra.append(right[right_index])
                count = count + len(left[lefts_index:])
                right_index=right_index+1
        return temp_arra, count
    
print(count_inversion_with_mergesort(test_list)[1])

numbers = []
with open("numbers.txt", 'r') as file:
    while True:
        line = file.readline()
        if line =="":
            break
        line = int(line)
        numbers.append(line)
        
print(len(numbers))

print(count_inversion_with_mergesort(numbers)[1])
        
        