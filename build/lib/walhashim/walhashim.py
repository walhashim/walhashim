class MyClass:
    
    # Initialize the class correctly
    def __init__(self, ls):
        self.ls = ls        
    
    # Return the max value in the list
    def return_max(self):
        return max(self.ls)
    
    # Return the minimum vale in the list
    def return_min(self):
        return min(self.ls)
    
    # Return the max value squared
    def return_max_squared(self):
        
        max_number = max(self.ls)
        max_squared = max_number ** 2
        
        return max_squared
    
    # Return length of the list:
    def return_length(self):
        return len(self.ls)
    
    # Return the sum of all positive numbers only
    def return_positive_sum(self):
        sum_num = 0
        for x in self.ls:
            if x > 0:
                sum_num += x
             
        return sum_num
    
    # Return the count of all negative numbers (How many negative numbers are in the list)
    def return_negative_count(self):
        i = 0
        for x in self.ls:
            if x < 0:
                i = i+1
                
        return i
    
    # Create 2 additional methods of your choice
    def method_one(self):
        return sum(self.ls)
    
    def method_two(self):
        
        sum_num = sum(self.ls)
        len_num = len(self.ls)
        avg_num = sum_num / len_num
        
        return round(avg_num,2)







