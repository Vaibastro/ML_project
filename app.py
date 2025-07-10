import streamlit as st
import pickle 
import string 
from nltk.corpus import stopwords
import nltk 
import re 
import spacy 


nlp = spacy.load("en_core_web_sm")

# Use spaCy's built-in stopwords
stopwords_list = nlp.Defaults.stop_words

# Preprocessing function
def transform_text(text):
    text = text.lower()
    text = re.findall(r'\b\w+\b', text)  # keeps only words (removes punctuation etc.)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords_list:
            y.append(i)

    return " ".join(y)  # return string for vectorizer



#load the model and vectorizer
model = pickle.load(open('model.pk1', 'rb'))
tfidf = pickle.load(open('vectorizer.pk1','rb'))

#title 
st.title("SMS/Email Spam Classifier")

#Input Box 
input_text = st.text_area("Enter the message")

if st.button("Predict"):
    transformed_input = transform_text(input_text)

    vector_input = tfidf.transform([transformed_input])
    result = model.predict(vector_input)[0]



    #Display the result 
    if result == 1:
        st.error("SPAM")

    else:
        st.success("NOT A SPAM")    
        