from services.db import get_connection

def insert_request(request):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO "Requests"
    ("citizenId","type","status","createdAt","updatedAt")
    VALUES (%s,%s,%s,NOW(),NOW())
    """

    cur.execute(query, (
        request["citizenId"],
        request["type"],
        request["status"]
    ))

    conn.commit()
    cur.close()
    conn.close()