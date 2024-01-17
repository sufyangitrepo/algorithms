"""
  Not Efficient
    We can use set for this problem but from get_random functionality
    will not be efficient becuause given get_random(list) function
    take list so for that we will have to convert that set to list O(n)
  Efficient
    We will use list for storing nubmbers and will use hash_map(dict)
    to keep unique the list of numbers
    lets code...
"""


class Task:
  
    def __init__(self) -> None:
        self.values = []
        self.values_mapping =  {}

    def insert(self, value) -> str:
        print(self.values_mapping)
        if self.values_mapping.get(value) is not None:
            return "Not inserted! bcs it is already exist"
        self.values.append(value)
        self.values_mapping[value] = len(self.values)-1
    
        return "inserted"

   
    def remove(self, value):
        if self.values_mapping.get(value) is None:
            return "value not exist"

        index = self.values_mapping.get(value)
        
        # swap expected value with last value in the list
         # len(self.values)-1 
        last_index = len(self.values) - 1
        last_value = self.values[last_index]

        # 1. shift any index value to last as well update map
        self.values[last_index] = value
        self.values_mapping[value] = last_index
        # 2. shift last value to that index as well update map for this value
        self.values[index] = last_value
        self.values_mapping[last_value] = index
        
        self.values.pop()
        del self.values_mapping[value]
        return self.values

    

    def __str__(self) -> str:
        return self.__class__.__name__
    
