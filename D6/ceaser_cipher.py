def decode(text: str, shift: int) -> str:
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isdigit():
            decrypted_text += str((int(char) - shift) % 10)
        else:
            decrypted_text += char
    return decrypted_text


def encrypt(text: str, shift: int) -> str:
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            encrypted_text += str((int(char) + shift) % 10)
        else:
            encrypted_text += char
    return encrypted_text

def main(job:str, shift:int, text:str) -> str:
    if job == "encode":
        return encrypt(text=text, shift=shift)
    else:
        return decode(text=text, shift=shift)

if __name__ == "__main__":
    while True:
        try:
            task : str = input("Type 'encode' to encrypt and 'decode' to decrypt\n")
            if task not in ["encode", "decode"]:
                task = input("Type 'encode' to encrypt and 'decode' to decrypt\n")
                raise ValueError
            break
        except:
            print("Type exactly one of the two words only\n")

    while True:
        try:
            shift_num : int = int(input("What is the number of shift you want to check?\n"))
            break
        except:
            print("Type an integer\n")

    text : str = input("What is your text? \n")
    

    print(main(job=task, shift=shift_num, text=text))

        
