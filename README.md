# 🌤️ Meteo Flask App & System Logger

Un'applicazione web sviluppata in Python con **Flask** che simula la previsione del tempo per una città richiesta e registra automaticamente sia su file che su **SQLite3** i dati della sessione e l'hardware del client.

---

## 📌 Features

- **Previsione Meteo Dynamics:** Generazione di un esito meteo simulato (Sole, Sereno, Pioggia) in base alla richiesta dell'utente.
- **System Information Logging:** Rilevamento automatico delle informazioni di sistema (Utente, Nome Computer, OS, Versione, Architettura).
- **Tracciamento Multi-Dispositivo (SQLite3):** 
  - Tabella `infosys`: Salva in modo univoco la combinazione `utente + nomecomputer`.
  - Tabella `previsione`: Mantiene la cronologia delle richieste meteo collegate all'hardware tramite chiavi esterne con supporto `ON DELETE CASCADE` / `ON UPDATE CASCADE`.
- **Log su File Locale:** Backup aggiuntivo delle sessioni in un file di testo `log.txt`.

---

## 📁 Struttura del Progetto

```text
├── flaskrouting.py     # Script principale dell'app Flask (rotte e gestione richieste)
├── database.py         # Modulo per la gestione dello schema SQLite3 e query
├── log.txt             # File di testo per il log (generato automaticamente)
├── log-meteo.db        # Database SQLite3 (generato automaticamente, escluso da Git)
├── templates/
│   └── index.html      # Template HTML per la resa visuale del meteo
├── .gitignore          # File per ignorare virtualenv e database locale
└── README.md           # Documentazione del progetto
