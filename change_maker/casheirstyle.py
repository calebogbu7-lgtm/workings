DENOMINATIONS = [
    ("$100 bill", 10000),
    ("$50 bill", 5000),
    ("$20 bill", 2000),
    ("$10 bill", 1000),
    ("$5 bill", 500),
    ("$1 bill", 100),
    ("quarter", 25),
    ("dime", 10),
    ("nickel", 5),
    ("penny", 1)
]
def parse_money(text):
    try:
        value = float(text)
        cents = round(value * 100)
    except (ValueError, OverflowError):
        return None
    if cents < 0:
        return None
    return cents


def ask_money(prompt):
    while True:
        cents = parse_money(input(prompt))
        if cents is not None:
            return cents
        print("Invalid input. Please enter a positive number like 4.35")


def calculate_balance():
    price = ask_money("Item price: ")
    paid = ask_money("Amount paid: ")

    if paid < price:
        owed = price - paid
        print(f"Not enough. Still owed: {owed / 100:g}")
    elif paid == price:
        print("Exact amount. Balance: 0")
    else:
        balance = paid - price
        print(f"Balance: {balance / 100:g}")


def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Calculate balance")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            calculate_balance()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2 to continue.")


if __name__ == "__main__":
    main()