# ===============================
# AIRPORT ATM + CURRENCY EXCHANGE
# ===============================

balance = 0.0   # balance stored in INR (Indian Rupees)

# Exchange rates (approx)
USD_RATE = 83.0      # 1 USD = 83 INR
EUR_RATE = 90.0      # 1 EUR = 90 INR
KWD_RATE = 270.0     # 1 KWD = 270 INR


# -------------------------------
# Deposit Function
# -------------------------------
def deposit():
    global balance
    amount = float(input("Enter amount to deposit (INR): "))
    if amount > 0:
        balance += amount
        print("Deposited successfully.")
    else:
        print("Invalid amount.")


# -------------------------------
# Withdraw Function
# -------------------------------
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw (INR): "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance.")


# -------------------------------
# Balance Check
# -------------------------------
def check_balance():
    print(f"Current Balance: ₹{balance:.2f}")


# -------------------------------
# Currency Exchange
# -------------------------------
def currency_exchange():
    global balance

    print("\n===== Currency Exchange =====")
    print("1. USD (United States Dollar)")
    print("2. EUR (Euro)")
    print("3. KWD (Kuwait Dinar)")

    choice = int(input("Select currency: "))

    if choice == 1:
        inr = float(input("Enter INR amount: "))
        if inr <= balance:
            usd = inr / USD_RATE
            balance -= inr
            print(f"You received: {usd:.2f} USD")
        else:
            print("Insufficient balance.")

    elif choice == 2:
        inr = float(input("Enter INR amount: "))
        if inr <= balance:
            eur = inr / EUR_RATE
            balance -= inr
            print(f"You received: {eur:.2f} EUR")
        else:
            print("Insufficient balance.")

    elif choice == 3:
        inr = float(input("Enter INR amount: "))
        if inr <= balance:
            kwd = inr / KWD_RATE
            balance -= inr
            print(f"You received: {kwd:.3f} KWD")
        else:
            print("Insufficient balance.")

    else:
        print("Invalid currency option.")


# -------------------------------
# ATM Main Menu
# -------------------------------
def ATM():
    while True:
        print("\n==============================")
        print(" AIRPORT ATM MACHINE ")
        print("==============================")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Currency Exchange")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            deposit()

        elif choice == 2:
            withdraw()

        elif choice == 3:
            check_balance()

        elif choice == 4:
            currency_exchange()

        elif choice == 5:
            print("Thank you for using Airport ATM.")
            break

        else:
            print("Invalid choice.")


# -------------------------------
# Program Start
# -------------------------------
ATM()
