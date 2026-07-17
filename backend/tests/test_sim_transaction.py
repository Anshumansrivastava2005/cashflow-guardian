from app.models.sim_transaction import SimTransaction


def main():

    transaction = SimTransaction(

        sim_user_id=1,

        type="Expense",

        category="Food",

        amount=450.75,

        description="Lunch at Restaurant",

        date="2026-07-15",

        payment_method="UPI",

        merchant="Swiggy",

        recurring=False

    )

    print()

    print(transaction.__tablename__)

    print()

    print(vars(transaction))


if __name__ == "__main__":
    main()