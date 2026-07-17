from datetime import date

from app.ai.engines.subscription_engine import SubscriptionEngine


def main():

    engine = SubscriptionEngine()

    print("\nSubscriptions\n")

    print("-" * 60)

    for day in range(1, 31):

        transactions = engine.generate(
            date(2026, 7, day)
        )

        if transactions:

            print(f"\nDay {day}")

            for transaction in transactions:
                print(transaction)


if __name__ == "__main__":
    main()