#Wandelt Text in Vektoren/Embeddings um
from sentence_transformers import SentenceTransformer
import numpy as np
#Für Ähnlichkeitssuche
import faiss
import json
import os

#Chunks laden
with open("data/chunks.json","r", encoding="utf-8") as f:
    chunks = json.load(f)

texts = chunks

 #Embedding-Modell laden
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

 #Wandelt Text in Vektoren um
embeddings = model.encode(texts)

 #Embeddings speichern
np.save("data/embeddings.npy", embeddings)

#Berechnet Vektor Länge
dimension = embeddings.shape[1]
#Erstellt FAISS-Index
index=faiss.IndexFlatL2(dimension)
#Fügt Embeddings zum Index hinzu
index.add(embeddings)

#Ordner für Index anlegen
if not os.path.exists("data/index"):
     os.mkdir("data/index")

#Index speichern
faiss.write_index(index, "data/index/faiss.index")

print("Embeddings und FAISS Index wurden erstellt.")