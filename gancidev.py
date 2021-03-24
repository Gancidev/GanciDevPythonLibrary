"""
@author GanciDev

Questa libreria contiene tutti i software da me scritti sotto forma di funzioni,
così che possano essere utilizzate da chiunque voglia.

La libreria è spiegata nel dettaglio nel file README della repository.

N.B.: Installare le librerie di seguito prima di utilizzare questa libreria.
"""
import os
import subprocess
import requests
import urllib.request
import bs4
import datetime
import json
from pdfrw import PdfReader, PdfWriter, PageMerge
from pathlib import Path


# Compatibile con Raspberry Pi
# Stampa l'IP e lo stato della Raspberry Pi (N.B.: E' necessario installare sysstat per l'utilizzo della CPU)
def status_raspy():
    # IP
    ip = subprocess.check_output("hostname -I", shell=True).decode("utf-8")
    print(f"Indirizzo Locale:  {ip}")
    # Stato RAM
    testo = subprocess.check_output("free -m", shell=True)
    test = str(testo.decode('utf-8')).split("         ")
    mem_totale = test[2]
    mem_uso = test[3]
    mem_disponibile = test[7].replace("\nSwap:", "")
    print(f"Stato RAM:\n Totale: {mem_totale}MB\n In Uso: {mem_uso}MB\n Disponibile: {mem_disponibile}MB")
    # Stato HDD
    testo = subprocess.check_output("df -h", shell=True)
    test = str(testo.decode('utf-8')).split("\n")
    tes = test[1].split(" ")
    mem_tot_HDD = tes[7]
    mem_uso_HDD = tes[9]
    mem_disponibile_HDD = tes[13]
    print(f"\nStato HDD:\n Totale: {mem_tot_HDD}B\n In Uso: {mem_uso_HDD}B\n Disponibile: {mem_disponibile_HDD}B")
    # Stato CPU
    # Temperatura
    testo = subprocess.check_output("cat /sys/class/thermal/thermal_zone*/temp", shell=True).decode('utf-8')
    temperatura = testo[:2] + "." + testo[2:3]
    print(f"\n\nStato CPU:\n Temperatura: {temperatura}'C\n Utilizzo:")
    # Utilizzo
    testo = subprocess.check_output("mpstat", shell=True)
    testo = str(testo.decode('utf-8')).split("\n")
    testo = testo[3].split(" ")
    utilizzo = 100 - float(testo[-1].replace(",", "."))
    print(f" {str(utilizzo)}")


# Valido per ogni Sistema Linux
# Bisogna editare la riga dell'output del comando df -h a seconda delle partizioni presenti sul proprio disco.
def status_host():
    # IP
    ip = subprocess.check_output("hostname -I", shell=True).decode("utf-8")
    print(f"Indirizzo Locale:  {ip}")
    # Stato RAM
    testo = subprocess.check_output("free -m", shell=True)
    test = str(testo.decode('utf-8')).split("        ")
    mem_totale = test[4]
    mem_uso = test[5]
    mem_disponibile = test[6].replace("\nSwap:", "")
    print(f"Stato RAM:\n Totale: {mem_totale}MB\n In Uso: {mem_uso}MB\n Disponibile: {mem_disponibile}MB")
    # Stato HDD
    testo = subprocess.check_output("df -h", shell=True)
    test = str(testo.decode('utf-8')).split("\n")
    indice = 1  # {RIGA CORRISPONDENTE AL DISCO DI CUI STAMPARE LE INFO}
    tes = test[indice].split(" ")
    mem_tot_HDD = tes[10]
    mem_uso_HDD = tes[12]
    mem_disponibile_HDD = tes[14]
    print(f"\nStato HDD:\n Totale: {mem_tot_HDD}B\n In Uso: {mem_uso_HDD}B\n Disponibile: {mem_disponibile_HDD}B")

#Scarica i file dal web
def download(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


#Scarica i file rar da mediafile
def media_file_downloader(path_file, name, formato):
    url = open(path_file, "r").readlines()
    cont = 1
    for l in url:
        l = str(l).replace("\n", "")
        if l != "":
            site = urllib.request.urlopen(l)
            site = urllib.request.urlopen(str(l))
            html = site.read()
            soup = bs4.BeautifulSoup(html)
            list_urls = soup.find_all('a')
            component = str(list_urls[7]).split(" ")
            component = str(component[5]).split("=")
            link = str(component[1]).replace('"', "")
            print(str(cont) + ":" + link)
            download(link, name + str(cont) + "." + formato)
        cont = cont + 1


#Ti ricorda dei compleanni dei parenti
def birthday_reminder(giorni_compleanni,nomi_festeggiati, oggi = datetime.datetime.now()):
    if oggi.strftime("%d-%m") in giorni_compleanni:
        pos = giorni_compleanni.index(oggi.strftime("%d-%m"))
        persona = nomi_festeggiati[pos]
        testo = "Oggi e' il compleanno di: " + persona
        print(testo)
        del giorni_compleanni[pos]
        del nomi_festeggiati[pos]
        if oggi.strftime("%d-%m") in giorni_compleanni:
            pos = giorni_compleanni.index(oggi.strftime("%d-%m"))
            persona = nomi_festeggiati[pos]
            testo = "Oggi e' il compleanno di: " + persona
            print(testo)


#Il token viene direttamente dal sito di openweathermap usato per assolvere al compito di reperire le informazioni meteo
def previsioni_meteo(citta, token):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + citta + ',IT&lang=IT&units=metric&appid='+token)
    x = r.text
    y = json.loads(x)
    if y['cod'] == 200:
        testo = "Previsioni per " + y['name'] + ":\n"
        testo = testo + "  Condizioni: " + y['weather'][0]['description'].capitalize() + "\n"
        testo = testo + "  Temperatura Attuale: " + str(y['main']['temp']) + " C" + "\n"
        testo = testo + "  Temperatura (min/max): " + str(y['main']['temp_min']) + " C / " + str(
            y['main']['temp_max']) + " C\n"
        testo = testo + "  Umidita': " + str(y['main']['humidity']) + "%\n"
        testo = testo + "  Vento: " + str(y['wind']['speed']) + " m/s\n"
        print(testo)
    else:
        print(f"La citta' -{citta}- non e' stata trovata.")


#E' necessario installare unoconv sulla macchina in cui si sfrutta questa funzione.
#Il file convertito si troverà nella cartella in cui è eseguito il codice.
def convert_file_to_pdf(path_file):
    comando = "unoconv " + path_file
    os.system(comando)


#Ritorna le dimensioni della pagina in pdf
def sizepage(page):
    result = PageMerge()
    result.add(page)
    return result[0].w, result[0].h


#Ritorna le dimensioni per la filigrana
def fixpage(page, width, height):
    result = PageMerge()
    result.add(page)
    if width > height:
        if width > 842:
            result[0].w = height * 1.6
            result[0].x = 50
        else:
            result[0].x = 0
            result[0].w = height * 1.4
    else:
        if height > 842:
            result[0].y = 125
        result[0].w = width
        result[0].x = 0
    return result.render()


#Filigrana il documento in input con la filigrana specificata
def filigrana(input_file,output_file="output.pdf",path_filigrana_ver="",path_filigrana_or=""):
    reader_input = PdfReader(input_file)
    writer_output = PdfWriter()
    page=reader_input.pages[0]
    w,h = sizepage(page)
    watermark_input = None
    watermark = None
    if int(w) > int(h):
        if path_filigrana_or=="":
            print("Non hai fornito la corretta filigrana o hai dimenticato di fornirla.")
        else:
            watermark_input=PdfReader(path_filigrana_or)
            watermark = fixpage(watermark_input.pages[0],int(w),int(h))
    else:
        if path_filigrana_ver=="":
            print("Non hai fornito la corretta filigrana o hai dimenticato di fornirla.")
        else:
            watermark_input=PdfReader(path_filigrana_ver)
            watermark = fixpage(watermark_input.pages[0],int(w),int(h))

    for current_page in range(len(reader_input.pages)):
        merger = PageMerge(reader_input.pages[current_page])
        merger.add(watermark).render()
    writer_output.write(output_file, reader_input)


#Bisogna installare unrar sul sistema prima di poter usare questa funzione.
def unrar_multiple_protected_files(path_rar_file, path_password_file):
    password = open(path_password_file, "r").readlines()
    cont=0
    for f in Path(path_rar_file).glob('*.rar'):
        comando="unrar x -p"+str(password[cont]).replace("\n", "")+" "+str(f)
        os.system(comando)
        cont=cont+1