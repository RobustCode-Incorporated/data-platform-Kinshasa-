import random
import string
from faker import Faker

fake = Faker()

# Pondération réaliste des communes (Kinshasa)
COMMUNE_WEIGHTS = {
    6: 4,   # Kimbanseke
    14: 4,  # Masina
    23: 4,  # Ndjili
    16: 3,  # Mont Ngafula
    9: 2,   # Lemba
    10: 2,  # Limete
    12: 2,  # Makala
}

def weighted_commune_choice(commune_ids):
    weighted = []
    for cid in commune_ids:
        weight = COMMUNE_WEIGHTS.get(cid, 1)
        weighted.extend([cid] * weight)
    return random.choice(weight)


def generate_numero_unique():
    return f"CI-{random.randint(100000000,999999999)}"


def generate_email(prenom, nom):
    return f"{prenom}.{nom}{random.randint(1000,999999)}@mail.com".lower()


def generate_citizen(person, commune_ids):
    return {
        "communeId": weighted_commune_choice(commune_ids),
        "nom": person["nom"],
        "postnom": person["postnom"],
        "prenom": person["prenom"],
        "dateNaissance": fake.date_of_birth(minimum_age=18, maximum_age=65),
        "sexe": random.choice(["Homme", "Femme"]),
        "lieuNaissance": "RDC",
        "numeroUnique": generate_numero_unique(),
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "email": generate_email(person["prenom"], person["nom"])
    }