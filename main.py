import sys
from using_array_dict.using_array_and_dict import Task
from find_second_largest.solution import find_second_largest


if __name__ == '__main__':
       
    input_values = []
    try:
      first_arg = sys.argv[1]
      file = open(first_arg, 'r')
      input_array = file.readlines()
      input_values = [ int(line) for line in input_array ]
       
    except IndexError:
        print("input is missing")
    except FileNotFoundError:
        print("File does not exist")
    except ValueError:
        print("integer is required not string")
    except Exception:
        print("something wrong")   
    
    # print("second_largest is: ", find_second_largest(input_values))
    task = Task()
    print(task.insert(input_values[0])) 
    print(task.insert(input_values[1]))
    task.remove(12)
    task.remove(13)