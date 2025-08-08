
              
from datetime import datetime
    
def write_log():
        message = input("Enter a log message: ")
        print(f"You typed: {message}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp}\t{message}\n"
        
        with open('log.txt', 'a') as file:        
             file.write(entry)
print("Message logged!")
        
if __name__ == "__main__":
        write_log()