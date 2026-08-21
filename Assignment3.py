from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("\nPayment Method: Credit Card")
        print(f"Amount Paid: ₹{amount}")
        print("Credit Card payment processed successfully.")
        print("----------------------")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print("\nPayment Method: PayPal")
        print(f"Amount Paid: ₹{amount}")
        print("PayPal payment processed successfully.")
        print("----------------------")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print("\nPayment Method: Bitcoin")
        print(f"Amount Paid: ₹{amount}")
        print("Bitcoin payment processed successfully.")
        print("----------------------")


class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
        print("Payment strategy changed successfully.")

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)


processor = PaymentProcessor()

while True:
    print("\n===== Payment Processing System =====")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")
    print("4. Process Payment")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        processor.set_strategy(CreditCardPayment())

    elif choice == "2":
        processor.set_strategy(PayPalPayment())

    elif choice == "3":
        processor.set_strategy(BitcoinPayment())

    elif choice == "4":
        amount = float(input("Enter payment amount: ₹"))
        processor.process_payment(amount)

    elif choice == "5":
        print("Exiting Payment Processing System.")
        break

    else:
        print("Invalid choice. Please try again.")