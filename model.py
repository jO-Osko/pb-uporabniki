import sqlite3

import naredi_bazo

conn = sqlite3.connect("baza.sqlite3")
# Nastavimo, da sledi tujim ključem
conn.execute("PRAGMA foreign_keys = ON")

naredi_bazo.pripravi_bazo(conn)

class Uporabnik:
    def __init__(self, uid, email, polno_ime):
        self.uid = uid
        self.email = email
        self.polno_ime = polno_ime
        
    @staticmethod
    def dobi_uporabnika(conn, email):
        with conn:
            cursor = conn.execute("""
                SELECT (uid, email, polno_ime) 
                FROM uporabnik
                WHERE email=?
            """, [email])
            podatki = cursor.fetchone()
            
            return Uporabnik(podatki[0], podatki[1], podatki[2])
        
