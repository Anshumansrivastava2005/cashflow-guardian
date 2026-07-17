from datetime import date

from app.ai.engines.expense_engine import ExpenseEngine


def main():

    engine = ExpenseEngine()

    print("\nGenerated Expenses\n")

    print("-" * 70)

    for _ in range(20):

        transaction = engine.generate_expense(
            current_date=date.today()
        )

        print(transaction)


if __name__ == "__main__":
    main()