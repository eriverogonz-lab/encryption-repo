def caesar_encryption(text, shift):
    encryption = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                inicio = ord("a")
                new_char = chr((ord(char) - inicio + shift) % 26 + inicio)
                encryption += new_char
            else:
                inicio = ord("A")
                new_char = chr((ord(char) - inicio + shift) % 26 + inicio)
                encryption += new_char
        else:
            encryption += char
            
    return encryption 


def caesar_decryption(text, shift):
    encryption = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                inicio = ord("a")
                new_char = chr((ord(char) - inicio - shift) % 26 + inicio)
                encryption += new_char
            else:
                inicio = ord("A")
                new_char = chr((ord(char) - inicio - shift) % 26 + inicio)
                encryption += new_char
        else:
            encryption += char
            
    return encryption 
