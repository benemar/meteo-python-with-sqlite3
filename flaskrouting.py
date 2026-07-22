from flask import Flask, render_template
import time
from random import Random
import os
import platform

#---------------------
import database

app = Flask (__name__)

# rotte

@app.route("/meteo/<citta>", methods=['GET', 'POST'])
def previsione_meteo(citta: str):
    rand = Random()
    dataora = time.strftime("%Y-%m-%d %H:%M:%S")
    ora = int(time.strftime("%H"))
    meteo_level = rand.randint(1, 10)

    if meteo_level >= 1 and meteo_level < 4:
        esito = 0  # sole
    elif meteo_level >= 4 and meteo_level < 6:
        esito = 1  # sereno
    else:
        esito = 2  # pioggia

    nome_computer = platform.node()          # nome host del computer
    sistema_operativo = platform.system()    # es. 'Linux', 'Windows', 'Darwin'
    versione_os = platform.version()         # versione dettagliata del SO
    architettura = platform.machine()        # es. 'x86_64'
    utente = os.getlogin()    

    _log_app(dataora, citta, esito, nome_computer, sistema_operativo, versione_os, architettura, utente)


    return render_template("index.html",
        citta=citta,
        previsione_meteo=esito,
        ora=ora
    )

def _log_app(dataora, citta, previsione, nomecomputer, sisop, versop, archit, utente):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"Nome computer: {nomecomputer}\n")
        file.write(f"Sistema operativo: {sisop}\n")
        file.write(f"Versione: {versop}\n")
        file.write(f"Architettura: {archit}\n")
        file.write(f"Utente: {utente}\n")
        file.write(f"Ora connessione: {dataora}\n")
        file.write(f"Città richiesta: {citta}\n")
        file.write(f"Previsione: {previsione}\n")
        file.write("-" * 50 + "\n")
    
    database.save_log(dataora, citta, previsione, nomecomputer, sisop, versop, archit, utente)




if __name__ == "__main__":
    database.creatabelle()
     
    app.run(debug=True, port=5555)