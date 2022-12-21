
def naredi_tabele(conn):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS 
            uporabnik(uid INTEGER PRIMARY KEY,
                      email TEXT, 
                      polno_ime TEXT
                      )             
        """
        )
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sledilec(
                zacetek INTEGER,
                tarca INTEGER,
                razlog TEXT,
                FOREIGN KEY(zacetek) REFERENCES uporabnik(uid),
                FOREIGN KEY(tarca) REFERENCES uporabnik(uid)
            )
        """)

def pripravi_bazo(conn):
    naredi_tabele(conn)
