import random
import string
import re

# --- Nettoyage des strings (très important vu ton parsing PDF) ---
def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z]', '', text)  # garde uniquement lettres
    return text


# --- Numéro unique ---
def generate_numero_unique():
    return f"CI-{random.randint(100000000,999999999)}"


# --- Email unique ---
def generate_email(prenom, nom):
    prenom_clean = clean_text(prenom)
    nom_clean = clean_text(nom)

    unique_suffix = random.randint(1000, 999999)

    return f"{prenom_clean}.{nom_clean}{unique_suffix}@mail.com"


# --- Génération citoyen ---
def generate_citizen(person, commune_ids):
    numero_unique = generate_numero_unique()

    return {
        "communeId": random.choice(commune_ids),
        "nom": person["nom"],
        "postnom": person["postnom"],
        "prenom": person["prenom"],
        "dateNaissance": "2000-01-01",
        "sexe": random.choice(["Homme", "Femme"]),
        "lieuNaissance": "RDC",
        "numeroUnique": numero_unique,
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "email": generate_email(person["prenom"], person["nom"])
    }