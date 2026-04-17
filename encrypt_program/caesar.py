def caesar_encryption(text, shift):
    encryption = ""
    for char in text:
        if char.isalpha():
            inicio = ord("a")
            new_char = chr((ord(char) - inicio + shift) % 26 + inicio)
            encryption += new_char
        else:
            encryption += char
            
    return encryption 


def caesar_decryption(text, shift):
    encryption = ""
    for char in text:
        if char.isalpha():
            inicio = ord("a")
            new_char = chr((ord(char) - inicio - shift) % 26 + inicio)
            encryption += new_char
        else:
            encryption += char
            
    return encryption 
