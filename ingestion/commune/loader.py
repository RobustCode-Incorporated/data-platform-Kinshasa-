from services.db import get_connection

def get_communes():
    conn = get_connection()
    cur = conn.cursor()

    query = 'SELECT id FROM "Communes";'
    cur.execute(query)

    communes = cur.fetchall()

    cur.close()
    conn.close()

    return communes