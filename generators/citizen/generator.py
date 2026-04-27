import random
import string
from faker import Faker

fake = Faker()

# 📊 Distribution réelle (MAPPÉE à tes IDs DB)
COMMUNE_DISTRIBUTION = {
    6: 16.7,   # Kimbanseke
    18: 9.0,   # Ngaliema
    14: 7.7,   # Masina
    22: 7.0,   # Kisenso
    20: 6.7,   # Nsele
    16: 6.1,   # Mont Ngafula
    10: 5.4,   # Limete
    9: 4.8,    # Lemba
    12: 4.2,   # Makala
    15: 3.7,   # Matete
    2: 3.5,    # Bumbu
    23: 3.3,   # Ndjili
    17: 3.1,   # Ngaba
    19: 2.9,   # Ngiri-Ngiri
    3: 2.7,    # Kalamu
    1: 2.4,    # Bandalungwa
    21: 2.2,   # Selembao
    8: 1.8,    # Kintambo
    24: 1.6,   # Barumbu
    11: 1.4,   # Lingwala
    4: 1.2,    # Kasa-Vubu
    7: 1.0,    # Kinshasa
    13: 1.0,   # Maluku
    5: 0.6     # Gombe
}

# 🔧 Préparation des listes (IMPORTANT)
COMMUNE_IDS = list(COMMUNE_DISTRIBUTION.keys())
COMMUNE_WEIGHTS = list(COMMUNE_DISTRIBUTION.values())


# ✅ FONCTION MANQUANTE (c’est ça ton erreur)
def weighted_commune_choice():
    return random.choices(
        COMMUNE_IDS,
        weights=COMMUNE_WEIGHTS,
        k=1
    )[0]


def generate_numero_unique():
    return f"CI-{random.randint(100000000, 999999999)}"


def generate_email(prenom, nom):
    base = f"{prenom}.{nom}".lower().replace(" ", "")
    unique = random.randint(100000, 999999)
    return f"{base}{unique}@mail.com"


def generate_citizen(person):
    return {
        "communeId": weighted_commune_choice(),  # ✅ maintenant OK

        "nom": person["nom"],
        "postnom": person["postnom"],
        "prenom": person["prenom"],

        "dateNaissance": fake.date_of_birth(minimum_age=18, maximum_age=65),
        "sexe": random.choice(["Homme", "Femme"]),
        "lieuNaissance": "RDC",

        "numeroUnique": generate_numero_unique(),

        "password": ''.join(random.choices(
            string.ascii_letters + string.digits, k=10
        )),

        "email": generate_email(person["prenom"], person["nom"])
    }