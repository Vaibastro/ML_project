import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
import nltk

print("All libraries imported successfully!")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")

print(f"Seaborn version: {sns.__version__}")
print(f"NLTK version: {nltk.__version__}")

# Test SpaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello, world!")
print(f"SpaCy processed: {doc.text}")

# Test NLTK
from nltk.tokenize import word_tokenize
words = word_tokenize("This is an NLTK test.")
print(f"NLTK tokenized: {words}")

print("Everything looks good!")