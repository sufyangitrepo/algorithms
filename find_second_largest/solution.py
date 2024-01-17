"""
  We will use two variable to store the index of 
   1. larget 
   2. second_largest
  of array
  initially larest have 0 index
  and second_largest have -1
  first will traverse array.  loop will start 1 index
  
  inside will be two condition
    1. if arr[largest] is less then the arr[counter]
        update second_larget with largest
        then will update with counter index 
    2. else (mean a arr[largest] is greater than arr[counter] )
        1. condition if arr[second_largest] is less than counter AND (is still -1 ) 
            update second_largest with counter 

"""
"12 -12 13 15 14 15 14"

def find_second_largest(arr):
    if len(arr) > 1:
        largest = 0
        second_largest = -1
        for counter in range(1, len(arr)):

            if arr[largest] < arr[counter]:
                second_largest = largest
                largest = counter
            else:
                if arr[largest] != arr[counter]:
                    if second_largest == -1 or arr[second_largest] < arr[counter]:
                        second_largest = counter
        return arr[second_largest]   
    else:
        print("array must have min 2 elements")   
