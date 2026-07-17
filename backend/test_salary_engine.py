from datetime import date

from app.ai.engines.salary_engine import SalaryEngine


def main():

    engine = SalaryEngine()

    user = {
        "monthly_income": 85000
    }

    transactions = engine.generate_salary(
        user=user,
        current_date=date(2026, 7, 1)
    )

    print("\nGenerated Transactions\n")

    print("-" * 60)

    for transaction in transactions:
        print(transaction)


if __name__ == "__main__":
    main()