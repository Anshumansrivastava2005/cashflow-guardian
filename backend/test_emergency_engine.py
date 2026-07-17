from datetime import date

from app.ai.engines.emergency_engine import EmergencyEngine


def main():

    engine = EmergencyEngine()

    print("\nEmergency Events\n")

    print("-" * 70)

    found = 0

    for day in range(1, 366):

        current_date = date.fromordinal(
            date(2026, 1, 1).toordinal() + day - 1
        )

        transactions = engine.generate(current_date)

        if transactions:

            found += 1

            print()

            print(current_date)

            for transaction in transactions:

                print(transaction)

    print()

    print(f"Total Emergencies Generated : {found}")


if __name__ == "__main__":
    main()