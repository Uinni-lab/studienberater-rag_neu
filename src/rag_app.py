import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
#Damit führe ich Ollama aus
import subprocess


#Embedding-Modell laden
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

#Chunks laden
with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)
#Index laden
index = faiss.read_index("data/index/faiss.index")

#Funktion, welche die geeigneten Chunks (hier 3)
def retrieve_chunks(query, k=3):
    #Anfrage wird in Vektor umgewandelt
    query_vec = model.encode([query])
    #distance = numerischer Abstand zwichen Query-Vektor und Chunk-Vektor
    #Index = Position des Vektors
    distances, indices = index.search(query_vec, k)
    #Leere Liste, wo results gespeichert werden
    results=[]
    for idx in indices[0]:
        #index wird in Zahl umgewandelt
        idx = int(idx)
        #Falls FAISS -1 ausgibt
        if idx >= 0:
            #Chunks werden zur Liste hinzugefügt
            results.append(chunks[idx])
    return results

def ask_llm(context_text, question):
    prompt=f"Kontext:\n{context_text}\n\nFrage:{question}\nAntwort:"


    result = subprocess.run(
        ["ollama", "run", "llama3.1"],
        input = prompt,
        text = True,
        capture_output = True,
        encoding = "utf-8"
    )
    if result.returncode != 0:
        return f"LLM-Fehler:\n{result.stderr}"

    answer = result.stdout.strip()
    if answer == "":
        return "Keine Antwort erhalten."
    return answer

def rag_system(question):
    #Liste von Chunks, die zur Frage passen
    context_list = retrieve_chunks(question)
    #Liste wird zu einem Text zusammengefügt
    context_text = "\n\n".join(context_list)
    answer = ask_llm(context_text, question)
    return answer
