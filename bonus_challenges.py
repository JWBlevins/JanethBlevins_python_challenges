
from datetime import datetime
def calculator():
    def add(x, y): return x + y
    def subtract(x, y): return x - y
    def multiply(x, y): return x * y
    def divide(x,y): return x / y if y != 0 else "Cannot divide by zero"
    
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    op = input("Choose operation (add, subtract, multiply, divide) or type 'exit' to quit: ").lower().strip()
    
    if op == 'exit':
        return "Goodbye!"
    
    if op not in operations:
        return "Invalid operation"
    
    try:
        
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        return "Invalid input"
    
    result = operations[op](x, y)
    output = f"Result: {result}"
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calculator_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {op} {x} {y} = {result}\n")
        
        return output

if __name__ == "__main__":
    while True:
        result = calculator()
        print(result)
        if result == "Goodbye!":
            break
    
  
    
    
    

