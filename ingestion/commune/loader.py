from services.db import get_connection

def get_communes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT id FROM "Communes"')
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [r[0] for r in rows]