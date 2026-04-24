import argparse
from caesar import caesar_encryption
from caesar import caesar_decryption
from Morse import morse_encryption
from Morse import morse_decryption
from file_functions import read_file, write_file

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files")
    
    parser.add_argument("mode", choices=["encrypt", "decrypt"])
    parser.add_argument("cipher", choices=["caesar", "morse"])
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("--shift", type=int, default=3)

    args = parser.parse_args()

    text = read_file(args.input_file)

    if args.cipher == "caesar":
        if args.mode == "encrypt":
            result = caesar_encryption(text, args.shift)
        else:
            result = caesar_decryption(text, args.shift)

    elif args.cipher == "morse":
        if args.mode == "encrypt":
            result = morse_encryption(text)
        else:
            result = morse_decryption(text)

    write_file(args.output_file, result)


if __name__ == "__main__":
    main()
