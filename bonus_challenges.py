
def fizzbuzz_with_a_twist():
    for i in range(1, 101):
        output = ""
        
        if i % 3 == 0:
           output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
                output +=  "Bang"
                            
        print(output if output else i)
        
    
    
if __name__ == "__main__":
        fizzbuzz_with_a_twist()