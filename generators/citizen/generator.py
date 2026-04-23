import random
import string
from datetime import date

def generate_numero_unique():
    return f"CI-{random.randint(100000,999999)}"


def generate_citizen(person, commune_ids):
    return {
        "communeId": random.choice(commune_ids),
        "nom": person["nom"],
        "postnom": person["postnom"],
        "prenom": person["prenom"],
        "dateNaissance": "2000-01-01",
        "sexe": random.choice(["Homme", "Femme"]),
        "lieuNaissance": "RDC",
        "numeroUnique": generate_numero_unique(),
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "email": f"{person['prenom'].lower()}.{person['nom'].lower()}@mail.com"
    }