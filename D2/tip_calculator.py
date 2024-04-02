def main(bill: float, tip: int, people: int):
    total_bill = bill + (bill * (tip / 100))
    return round(total_bill / people, 2)

if __name__ == "__main__":
    while True:
        try:
            total_bill = float(input("What is the total bill? $"))
            break
        except ValueError:
            print("Please enter a valid number for the total bill.")

    while True:
        try:
            tip_percent = int(input("How much would you like to tip? 10% / 15% / 20% "))
            if tip_percent not in [10, 15, 20]:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid tip percentage (10, 15, or 20).")

    while True:
        try:
            number_of_people = int(input("How many people will be paying the bill? "))
            if number_of_people <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number of people (greater than 0).")

    amount_per_person = main(total_bill, tip_percent, number_of_people)
    print("Each person should pay: $", amount_per_person)
