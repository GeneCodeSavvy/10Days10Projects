from random import choices, randint, shuffle

def main(number_of_charecters:int = 10, number_of_alphabets:int = 10):
    alphabets = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    password = choices(alphabets, k=number_of_alphabets)
    num_ints = number_of_charecters - number_of_alphabets
    for i in range(num_ints):
        password.append(str(randint(0,9)))
    shuffle(password)
    return(''.join(password))

if __name__ == "__main__":
    print("Welcome to password generator")
    while True:
        try:
            chars: int = int(input("How many charecters do you want in your password? "))
            num_alpha: int = int(input("How many alphabets do you want in your password? "))
            break
        except:
            print("Type a valid integer")
    secret = main(number_of_charecters=chars, number_of_alphabets=num_alpha)
    print("Your password is: ", secret)

