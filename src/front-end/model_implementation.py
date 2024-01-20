import numpy as np
import pandas as pd
import warnings, string
warnings.filterwarnings('ignore')
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import joblib

# Tokenizzazione, Rimozione delle Stop Words, Rimozione dei Numeri, Rimozione della Punteggiatura
def text_cleaning(text):
    return ' '.join([word for word in word_tokenize(text) 
            if word not in stopwords.words('english') 
            and not word.isdigit() 
            and word not in string.punctuation])

# Applica lo stemming ad una stringa
def stem_words(text):
    stemmer = PorterStemmer()
    return ' '.join([stemmer.stem(word) for word in text.split()])

# Applica il lemmatazing ad una stringa
def lemmatize_words(text):
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

# Text process utilizzato pre addestramento
def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# Applica tutte le fasi di preprocessing utilizzate pre-training del modello
def review_preprocessing(raw_review):

    # Converte la stringa grezza in lowercase
    processed_review = raw_review.lower()

    # Applicata la fuznione text cleaning definita sopra
    processed_review = text_cleaning(processed_review)

    # Stemming & Lemmatizing
    processed_review = stem_words(processed_review)
    processed_review = lemmatize_words(processed_review)

    return processed_review

def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# Input dall'utente
input_review = input("Inserisci una recensione: ")

processed_review = review_preprocessing(input_review)

# Carica il modello addestrato
model_path = 'src/models/model_SVC.pkl'  # Aggiorna il percorso se necessario
model = joblib.load(model_path)

# Definisci i dati e il nome della colonna
data = {'text_': [processed_review]}

# Crea un DataFrame
df = pd.DataFrame(data)

# Converti il DataFrame in una Serie
# La Serie avrà un solo elemento con l'indice 0
serie = df['text_']

prediction = model.predict([serie])

if prediction=='OR':
    print(True)
elif prediction=='CG':
    print(False)


