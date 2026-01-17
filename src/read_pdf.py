from pypdf import PdfReader
#Speichern von Chunks als JSON Dateien
import json
#Ordner erstellen, Dateien durchgehen
import os

#Leere Liste, um Textstücke später zu speichern
chunks = []
#Ordner erstellen
if not os.path.exists("data"):
    os.makedirs("data")

#PDF laden
pdf_folder="C:/Users/dinse/PycharmProjects/Studienberater/data"


#PDFs durchgehen
for filename in os.listdir(pdf_folder):
    #Stellt sicher, dass der Dateiname klein geschrieben wird
    if filename.lower().endswith(".pdf"):
        #aus Ordner und Dateiname wird ein Pfad erstellt
        pdf_path = os.path.join(pdf_folder, filename)
        reader = PdfReader(pdf_path)


        #Text wird extrahiert und in die Variable whole_text gespeichert
        whole_text=""

        for page in reader.pages:
            page_text=page.extract_text()
            if page_text: #is not None :
               whole_text += page_text + "\n"

        #split() zerlegt Text in Wörter
        # join()fügt sie wieder zusammen; überflüssige (z.B) doppelte Leerzeichen werden entfernt
        clean_text = "".join(whole_text.split())

        # Zerteilt den Text in Chunks von 500 Wörtern
        chunk_size = 500
        start = 0
        # Erstellung der einzelnen Chunks
        while start < len(clean_text):
            end = start + chunk_size
            chunks.append({
                "source": filename,
                "text":clean_text[start:end]
            })
            start = end

#Chunks speichern
with open("data/chunks.json2","w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2, ensure_ascii=False)
print("PDFs wurde gelesen und Chunks wurden gespeichert")