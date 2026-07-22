import sqlite3

DB_NAME = "log-meteo.db"

SQL_TABLE_INFOSYS = """
CREATE TABLE IF NOT EXISTS infosys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utente TEXT,
    nomecomputer TEXT,
    sisop TEXT,
    versionsop TEXT,
    architettura TEXT,
    UNIQUE(utente, nomecomputer)  -- La combinazione utente + PC è  unica
);
"""

SQL_TABLE_PREVISIONE = """
CREATE TABLE IF NOT EXISTS previsione (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utente_fk TEXT,
    nomecomputer_fk TEXT,
    dataora TEXT,
    citta TEXT,
    previsione INTEGER,
    FOREIGN KEY (utente_fk, nomecomputer_fk) REFERENCES infosys (utente, nomecomputer)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
"""

def creatabelle():
    con = sqlite3.connect(DB_NAME)
    cursore = con.cursor()
    # attivo la foreign key
    cursore.execute("PRAGMA foreign_keys = ON;")
    cursore.execute(SQL_TABLE_INFOSYS)
    cursore.execute(SQL_TABLE_PREVISIONE)
    con.commit()
    con.close()

def save_log(dataora, citta, esito, nome_computer, sistema_operativo, versione_os, architettura, utente):
    con = sqlite3.connect(DB_NAME)
    cursore = con.cursor()
    cursore.execute("PRAGMA foreign_keys = ON;")

 #   Inserisco la combinazione Utente+PC solo se non esiste già
    cursore.execute("""
    INSERT OR IGNORE INTO infosys (utente, nomecomputer, sisop, versionsop, architettura) 
    VALUES (?, ?, ?, ?, ?)
""", (utente, nome_computer, sistema_operativo, versione_os, architettura))

#   Registra la previsione 
    cursore.execute("""
    INSERT INTO previsione (utente_fk, nomecomputer_fk, dataora, citta, previsione) 
    VALUES (?, ?, ?, ?, ?)
""", (utente, nome_computer, dataora, citta, esito))
    
    con.commit()
    con.close()