import random
import string
from faker import Faker

fake = Faker()

# 🧠 Pondération réaliste des communes (Kinshasa)
COMMUNE_WEIGHTS = {
    6: 4,   # Kimbanseke
    14: 4,  # Masina
    23: 4,  # Ndjili
    16: 3,  # Mont Ngafula
    9: 2,   # Lemba
    10: 2,  # Limete
    12: 2,  # Makala
}

# 🎯 Choix pondéré des communes (simulation population réelle)
def weighted_commune_choice(commune_ids):
    weighted_list = []

    for cid in commune_ids:
        weight = COMMUNE_WEIGHTS.get(cid, 1)

        # sécurité type
        if not isinstance(weight, int):
            weight = 1

        weighted_list.extend([cid] * weight)

    return random.choice(weighted_list)


# 🔢 numéro unique citoyen
def generate_numero_unique():
    return f"CI-{random.randint(100000000, 999999999)}"


# 📧 email réaliste + unique
def generate_email(prenom, nom):
    base = f"{prenom}.{nom}".lower().replace(" ", "")
    unique = random.randint(100000, 999999)
    return f"{base}{unique}@mail.com"


# 👤 génération citoyen complet
def generate_citizen(person, commune_ids):
    return {
        "communeId": weighted_commune_choice(commune_ids),
        "nom": person["nom"],
        "postnom": person["postnom"],
        "prenom": person["prenom"],

        # 📅 données réalistes
        "dateNaissance": fake.date_of_birth(minimum_age=18, maximum_age=65),
        "sexe": random.choice(["Homme", "Femme"]),
        "lieuNaissance": "RDC",

        # 🆔 identité
        "numeroUnique": generate_numero_unique(),

        # 🔐 sécurité simulée
        "password": ''.join(random.choices(
            string.ascii_letters + string.digits,
            k=10
        )),

        # 📧 contact
        "email": generate_email(person["prenom"], person["nom"])
    }