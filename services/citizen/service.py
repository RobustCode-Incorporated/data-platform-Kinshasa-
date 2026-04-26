from services.db import get_connection

def insert_citizen(citizen):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO "Citoyens"
    ("communeId","nom","postnom","prenom","dateNaissance","sexe",
     "lieuNaissance","numeroUnique","password","email","createdAt","updatedAt")
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),NOW())
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

    citizen_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return citizen_id