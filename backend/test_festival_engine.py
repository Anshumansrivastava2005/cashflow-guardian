from datetime import date

from app.ai.engines.festival_engine import FestivalEngine


def main():

    engine = FestivalEngine()

    test_dates = [

        date(2026, 1, 1),

        date(2026, 3, 4),

        date(2026, 7, 15),

        date(2026, 11, 8),

        date(2026, 12, 25)

    ]

    for current_date in test_dates:

        print()

        print("=" * 70)

        print(current_date)

        print("=" * 70)

        transactions = engine.generate(current_date)

        if not transactions:

            print("No Festival")

            continue

        for transaction in transactions:

            print(transaction)


if __name__ == "__main__":
    main()