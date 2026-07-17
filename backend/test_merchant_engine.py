from app.ai.engines.merchant_engine import MerchantEngine


def main():

    engine = MerchantEngine()

    print("\nExpense Transactions\n")

    for _ in range(10):
        print(engine.random_expense())

    print("\nIncome Transactions\n")

    for _ in range(5):
        print(engine.random_income())

    print("\nRandom Transactions\n")

    for _ in range(10):
        print(engine.random_transaction())


if __name__ == "__main__":
    main()