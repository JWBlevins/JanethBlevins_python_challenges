def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
            
        return result
    
if __name__ == "__main__":
    print(caesar_cipher("abc", 3))
    print(caesar_cipher("xyz", 2))
    print(caesar_cipher("Hello, World", 5))
        
        
        
            