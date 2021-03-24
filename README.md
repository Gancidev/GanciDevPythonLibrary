# GanciDevPythonLibrary
 
## Funzioni disponibili
___
```
1. status_raspy
    -Stampa lo stato delle memorie e della CPU della Raspberry.

2. status_host
    -Stampa lo stato delle memorie.

3. download
    -Scarica file dal link fornito, nel percorso fornito.

4. media_file_downloader
    -Scarica file dal link fornito, dando loro nome ed estensione forniti. 

5. birthday_reminder
    -Notifica i nomi di chi compie gli anni in quella giornata.

6. previsioni_meteo
    -Fornisce le informazioni meteorologiche della città desiderata.

7. convert_file_to_pdf
    -Converte il file in input in un file pdf.

8. sizepage
    -Ritorna le dimensioni della pagina di un PDF.

9. fixpage
    -Ritorna le dimensioni corrette per apporre una filigrana ad un documento PDF.

10. filigrana
    -Appone una filigrana al documento PDF passato in input.

11. unrar_multiple_protected_files
    -Estrae file rar protetti da password.
```
## Librerie per l'utilizzo
___
```
1. os
2. subprocess
3. requests
4. urllib.request
5. bs4
6. datetime
7. json
8. PdfReader, PdfWriter, PageMerge (from pdfrw)
9. Path (from pathlib)
```
## Descrizione delle funzioni
___
```
1. status_raspy
    -Utilizza comandi di sistema, maggiori dettagli nel codice stesso.

2. status_host
    -Utilizza comandi di sistema, maggiori dettagli nel codice stesso.

3. download
    -Utilizza la libreria request per fare la richiesta e aprire uno stream che poi
    redirige su un file, nel quale scrive una porzione(chunk) alla volta.

4. media_file_downloader
    -Preleva da un file di testo i link e li utilizza per fare delle richieste http che
    ritornano il codice HTML della pagina di download di mediafire, dalla quale usando 
    BeautifulSoup4 viene estratto il link al download diretto da passare alla funzione di
    download.

5. birthday_reminder
    -Verifica la corrispondenza della data di oggi nel formato GG-MM con quelle presenti
    nella lista fornita in input e estraendo il nome del festeggiato lo notifica.

6. previsioni_meteo
    -Sfruttando le API gratuite di openweathermap si effettua una richiesta http
    che ritorni un json dal quale si può estrarre le previsioni meteo.
    N.B.: Il token per le API è generabile sul sito dopo la registrazione. 

7. convert_file_to_pdf
    -Utilizzando il software di sistema unoconv converte i file in pdf da differenti
    formati tra cui quelli di office e libreoffice.

8. sizepage
    -utilizza la funzione PageMerge per creare un pdf e poi con add vi aggiunge una pagina
    dal quale preleva le dimensioni.

9. fixpage
    -Preleva le dimensioni come nella funzione sizepage per poi controllare se il documento
    sia orizzontale o verticale e fixare automaticamente la dimensione di quest'ultimo
    così da poter editare le dimensioni della filigrana.

10. filigrana
    -Sfruttando PdfReader, PdfWriter, PageMerge e le funzioni sizepage e fixpage genera una 
    copia del pdf al quale poi appone una filigrana facendo il render di un pdf sopra
    l'altro.
    N.B.: La filigrana deve essere a sfondo trasparente e in PDF.

11. unrar_multiple_protected_files
    -Legge le password da un file txt e va estraendo tutti i file rar che trova nella
    directory indicata.
    N.B.: Le password devono essere ordinate con i rispettivi file, poichè la funzione
    estrae i file in ordine alfabetico anche le password devono rispettare lo stesso ordine.
    EX: 
            file1.rar       password_file1
            file2.rar       password_file2
```
## Installazione e Utilizzo
___
Per utilizzare la libreria è necessario installare i seguenti software:
```
1. unoconv
2. sysstat  (solo per raspberry)
3. unrar

Installazione: sudo apt-get install {nome_software}
```
Per la libreria bisogna scaricarla e inserirla nella cartella contenente lo script che poi dovrà utilizzarne i metodi ed importarla mediante la seguente riga:
```
import gancidev
```
