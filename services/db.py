import os
import psycopg2
from dotenv import load_dotenv

# Charger les variables d'environnement (.env)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    if not DATABASE_URL:
        raise ValueError("❌ DATABASE_URL non définie dans .env")

    try:
        conn = psycopg2.connect(
            DATABASE_URL,
            sslmode="require"  # obligatoire pour Neon
        )
        return conn

    except Exception as e:
        print("❌ Erreur connexion DB:", e)
        raise e