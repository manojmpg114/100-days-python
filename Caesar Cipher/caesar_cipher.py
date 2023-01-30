#caesar_cipher.py

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift): #did it with lists but works fine with strings -- could easily use this base as the only function with negative shifts
    
    #encrypted = []
    cipher = ""
    for char in text:
        try:
            #encrypted.append(alphabet[alphabet.index(char) + shift])
            cipher+=alphabet[alphabet.index(char) + shift]
        except IndexError:
            #encrypted.append(alphabet[(alphabet.index(char) + shift)-26])
            cipher+=alphabet[(alphabet.index(char) + shift)-26]
        
    #return ''.join(encrypted)
    #return cipher
    #print(f'The encoded text is {cipher}')
    print(f'The {direction}d text is {cipher}')
    
def decode(text, shift):
    message = ""
    for char in text:
        try:
            message+=alphabet[alphabet.index(char) - shift]
        except IndexError:
            message+=alphabet[(alphabet.index(char) - shift)+26]
    
    print(f'Decoded text is {message}')
    
def caesar(text,shift):
    if direction == 'encode':
        encrypt(text,shift) #didn't want to rewrite the main points of the function
    elif direction == 'decode':
        shift *= -1
        encrypt(text, shift)


if __name__ == '__main__':
    
    # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))
    
    # # if direction == 'encode':
    # #     encrypt(text,shift)
    # # elif direction == 'decode':
    # #     decode(text,shift)
    
    # caesar(text,shift)
    
    repeat = True
    while repeat:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift %=26  #keeps shift in a range below 26
        
        caesar(text,shift)
        
        check = input("Type 'yes' to continue or 'no' to quit: ").lower()
        if check == 'no':
            repeat = False
    
