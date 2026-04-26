from services.db import get_connection

def insert_citizen(citizen):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO "Citoyens"
    ("communeId","nom","postnom","prenom","dateNaissance","sexe",
     "lieuNaissance","numeroUnique","password","email","createdAt","updatedAt")
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),NOW())
    ON CONFLICT ("email") DO UPDATE SET email = EXCLUDED.email
    RETURNING id
    """

    cur.execute(query, (
        citizen["communeId"],
        citizen["nom"],
        citizen["postnom"],
        citizen["prenom"],
        citizen["dateNaissance"],
        citizen["sexe"],
        citizen["lieuNaissance"],
        citizen["numeroUnique"],
        citizen["password"],
        citizen["email"]
    ))

    result = cur.fetchone()

    conn.commit()
    cur.close()
    conn.close()

    return result[0] if result else None