# Progetto-MCF

Assicurarsi di avere installate le seguenti librerie di python:
-sys, os
-numpy
-math
-matplotlib.pyplot
-scipy

Salvare tutti i file nella stessa cartella e con lo stesso nome che si trova su GitHub

Il file spett.py contiene tutte le funzioni necessarie per gli altri file.

All'esecuzione di ottimizzato.py all'inizio comparirà un grafico di tutte le possibili combinazioni per pixel e fenditura, rappresentate da punti nel piano.
Successivamente compariranno una serie di grafici rappresentanti l'efficienza di ogni configurazione in funzione del numero di massa (la configurazione a cui si riferisce il grafico verrà stamapata sul terminale).
Alla fine il programma stamperà il valore con l'efficienza media maggiore (in caso di parità stamperà il primo).

All'esecuzione di isotopi.py dapprima verrà eseguito ottimizzato.py, da cui saranno estratti i valori ottimizzati per pixel e fenditura.
Successivamente compariranno in ordine 9 grafici, nei quali vengono fatte variare la larghezza della fenditura e la dimensione dei pixel, i primi tre fanno riferimento agli isotopi carbonio 12 e 13, i secondi tre a polonio 209 e 210 e gli ultimi 3 a Germanio 72 e 74.
Per ogni blocco di tre nel primo viene cambiata solamente la larghezza della fenditura, nel secondo solo la grandezza del pixel mentre nel terzo entrambe simultaneamente.

All'esecuzione di materiali.py dapprima verrà eseguito ottimizzato.py, da cui saranno estratti i valori ottimizzati per fenditura e pixel.
Successivamente compariranno in ordine i grafici della risposta dello strumento ottimizzato ai due materiali richiesti.


