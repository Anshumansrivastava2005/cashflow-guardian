from app.ai.engines.transaction_engine import TransactionEngine


def main():

    engine = TransactionEngine()

    user = {
        "monthly_income": 85000
    }

    transactions = engine.generate_month(
        user=user,
        year=2026,
        month=7
    )

    print()

    print("=" * 80)

    print("MONTHLY TRANSACTIONS")

    print("=" * 80)

    print()

    print(f"Total Transactions : {len(transactions)}")

    print()

    for transaction in transactions[:20]:

        print(transaction)


if __name__ == "__main__":
    main()