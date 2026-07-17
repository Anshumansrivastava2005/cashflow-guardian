import json
import os

BASE_DIR = os.path.join(
    os.path.dirname(__file__),
    "config",
    "india"
)

os.makedirs(BASE_DIR, exist_ok=True)

# ------------------------------------
# Merchants
# ------------------------------------

MERCHANTS = {
    "Food": [
        "Swiggy","Zomato","Dominos","Pizza Hut","McDonald's",
        "KFC","Burger King","Subway","Starbucks","Cafe Coffee Day",
        "Haldiram","Bikanervala","Behrouz","Faasos","FreshMenu",
        "Wow Momo","EatSure","Barbeque Nation","Local Restaurant"
    ],

    "Shopping": [
        "Amazon","Flipkart","Myntra","Ajio","Nykaa",
        "Meesho","Reliance Digital","Croma","DMart","IKEA",
        "Vijay Sales","Lifestyle","Pantaloons","Westside",
        "Decathlon","Tata CliQ","Shoppers Stop"
    ],

    "Travel": [
        "Uber","Ola","Rapido","IRCTC","RedBus",
        "Goibibo","MakeMyTrip","Yatra","IndiGo",
        "Air India","SpiceJet","Metro","Auto Rickshaw"
    ],

    "Bills": [
        "Airtel","Jio","Vi","BSNL",
        "ACT Fibernet","Electricity Board",
        "Water Board","Gas Agency"
    ],

    "Entertainment": [
        "Netflix","Amazon Prime","Disney+ Hotstar",
        "Spotify","BookMyShow","PVR",
        "INOX","Steam","PlayStation Store"
    ],

    "Medical": [
        "Apollo Pharmacy","MedPlus",
        "NetMeds","PharmEasy","1mg",
        "Apollo Hospital","Fortis"
    ],

    "Fuel": [
        "Indian Oil",
        "HP",
        "BPCL",
        "Shell"
    ],

    "Investment": [
        "Groww",
        "Zerodha",
        "Upstox",
        "Angel One",
        "Paytm Money"
    ]
}

# ------------------------------------
# Categories
# ------------------------------------

CATEGORIES = {
    "Income": [
        "Salary",
        "Freelancing",
        "Business",
        "Investment"
    ],

    "Expense": [
        "Food",
        "Shopping",
        "Travel",
        "Bills",
        "Medical",
        "Fuel",
        "Entertainment",
        "Education",
        "Insurance"
    ]
}

# ------------------------------------
# Payment Methods
# ------------------------------------

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

# ------------------------------------
# Cities
# ------------------------------------

CITIES = [
    "Ahmedabad",
    "Vadodara",
    "Surat",
    "Rajkot",
    "Mumbai",
    "Pune",
    "Delhi",
    "Noida",
    "Gurgaon",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Jaipur",
    "Lucknow"
]

# ------------------------------------
# Occupations
# ------------------------------------

OCCUPATIONS = [
    "Student",
    "Software Engineer",
    "Doctor",
    "Teacher",
    "Business Owner",
    "Government Employee",
    "Lawyer",
    "Freelancer",
    "Startup Founder",
    "Chartered Accountant"
]

# ------------------------------------
# Lifestyles
# ------------------------------------

LIFESTYLES = [
    "Student",
    "Minimalist",
    "MiddleClass",
    "UpperMiddleClass",
    "Luxury",
    "Investor"
]

# ------------------------------------
# Festivals
# ------------------------------------

FESTIVALS = {
    "Diwali": "2026-11-08",
    "Holi": "2026-03-04",
    "Christmas": "2026-12-25",
    "NewYear": "2026-01-01",
    "IndependenceDay": "2026-08-15",
    "RepublicDay": "2026-01-26"
}

# ------------------------------------
# Personas
# ------------------------------------

PERSONAS = [
    {
        "name": "Student",
        "salary_min": 5000,
        "salary_max": 15000,
        "lifestyle": "Student"
    },
    {
        "name": "Software Engineer",
        "salary_min": 40000,
        "salary_max": 200000,
        "lifestyle": "UpperMiddleClass"
    },
    {
        "name": "Doctor",
        "salary_min": 80000,
        "salary_max": 500000,
        "lifestyle": "Luxury"
    },
    {
        "name": "Business Owner",
        "salary_min": 50000,
        "salary_max": 1000000,
        "lifestyle": "Luxury"
    },
    {
        "name": "Government Employee",
        "salary_min": 35000,
        "salary_max": 120000,
        "lifestyle": "MiddleClass"
    }
]

FILES = {
    "merchants.json": MERCHANTS,
    "categories.json": CATEGORIES,
    "payment_methods.json": PAYMENT_METHODS,
    "cities.json": CITIES,
    "occupations.json": OCCUPATIONS,
    "lifestyles.json": LIFESTYLES,
    "festivals.json": FESTIVALS,
    "personas.json": PERSONAS
}

for filename, data in FILES.items():
    path = os.path.join(BASE_DIR, filename)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

print("Configuration files generated successfully.")