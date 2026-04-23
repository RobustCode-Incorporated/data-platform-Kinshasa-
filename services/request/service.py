from services.db import get_connection

def insert_request(request):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO "Requests"
    ("citizenId","type","status","createdAt","updatedAt")
    VALUES (%s,%s,%s,NOW(),NOW())
    RETURNING id
    """

    cur.execute(query, (
        request["citizenId"],
        request["type"],
        request["status"]
    ))

    request_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return request_id


# --- Types métiers e-Gov ---
def generate_request_types():
    return [
        "ACTE_NAISSANCE",
        "ACTE_MARIAGE",
        "ATTESTATION_RESIDENCE"
    ]