# Analisi delle Recensioni False Mediante Machine Learning: Sviluppo di un Bot per la Rilevazione Automatica

## Autori
[DomenicoAnzalone](https://github.com/DomenicoAnzalone), [pierago01](https://github.com/pierago01)



## Descrizione
Questo progetto implementa un modello di machine learning per rilevare recensioni false su piattaforme online. Utilizzando tecniche di Natural Language Processing e algoritmi di apprendimento supervisionato, il sistema è in grado di identificare recensioni potenzialmente ingannevoli o non autentiche. L'utente può utilizzare il bot "FakeReviewDetector", sviluppato in Telegram per identificare in modo rapido se una recensione di un prodotto o di un servizio trovato online è autentica o meno.

## Caratteristiche
- **Algoritmi di Machine Learning:** 
  - Multinomial Naive Bayes
  - Random Forest
  - Decision Tree Classifier
  - KNeighbors Classifier
  - Support Vector Classifier
  - Logistic Regression
- **Preprocessing dei Dati:**
  Abbiamo utilizzato diverse tecniche di NLP per la pre-elaborazione dei dati, tra cui la conversione in stringa e in lowercase, la tokenizzazione e l'ottimizzazione del testo con lemming e stemming.
- **Analisi Esplorativa:**
  Gli strumenti utilizzati per l'analisi esplorativa dei dati sono stati Jupyter Notebook per documentare e presentare il flusso di lavoro di analisi e Matplotlib per la creazione e la personalizzazione di grafici e visualizzazioni di dati.  
- **Valutazione del Modello:** La scelta del modello da utilizzare è stata basata sull'accuratezza di ciascuno algoritmo durante la fase di testing.

## Prerequisiti
- Python 3.11.4
- Pandas, NumPy
- Scikit-Learn
- Matplotlib
- TensorFlow o PyTorch (opzionale)

## Installazione
Per utilizzare il modello seguire questi passi:
```bash
git clone https://github.com/tuo-username/fake-review-detection.git
cd fake-review-detection
```
Se si vuole modificare il codice del bot, bisogna crearne uno personale attraverso BotFather in Telegram e riutilizzare il codice presente all'interno del progetto.

## Utilizzo
Cercare "FakeReviewDetector" o @frdetection_bot in Telegram.
Premere il pulsante "Avvia" e inviare come messaggio una recensione. Il bot identificherà se la recensione è autentica o creata da un altro bot.

<p align='center'> 
    <img width="250" src="https://github.com/DomenicoAnzalone/FakeReviewDetection/assets/81223389/ded699df-1157-482c-8eb3-b4e9dd47a042">
    <img width="250" src="https://github.com/DomenicoAnzalone/FakeReviewDetection/assets/81223389/97ece750-5309-486c-8cd3-557d70d29c02">
</p>



## License
This project is distributed under the [The Unlicense](LICENSE).
<p align='left'> 
    <img width="100" src="https://github.com/DomenicoAnzalone/FakeReviewDetection/assets/81223389/cfc25399-b043-4a7f-8029-79fc1cad2e45">
</p>


