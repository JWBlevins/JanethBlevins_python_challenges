
    
def find_max(numbers):
    if not numbers:
        return "List is empty"
    
    max_value = numbers[0]
    
    for num in numbers:
        if num > max_value:
            max_value = num
            
    return max_value
if __name__ == "__main__":
        
    print(find_max([4,9,1,17,2]))
    print(find_max([-5, -9, -2, -12]))
    print(find_max([42]))
    print(find_max([]))
