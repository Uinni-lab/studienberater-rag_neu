#  Studienberater

## Beschreibung
Dieses Projekt ist meine erste Anwendung mit RAG. Damit kann man PDF-Dateien einlesen und dann Fragen dazu stellen. Das System such die relevanten Textstellen heraus und beantwortet Fragen mit einem lokalen LLM.

## Ordnerstruktur
/src
- read_pdf.py: Liest PDFs ein und erstellt Text-Chunks
- build_index.py: Erstellt Embeddings und FAISS-Index
- rag_app.py: Kombination aus Suche + LLM
- app.py: Gradio-Interface
## Installation
1. Virtuelle Umgebung automatisch durch PyCharm angelegt
2. Packages installieren:
- pip install pydf sentence-transformers faiss-cpu gradio
3. Lokales LLM installieren (in meinem Fall Ollama):
- pip install Ollama

## Benutzung
1. PDFs anlegen:
- alle PDFs, die ich analysieren möchte, lege ich in /data
2. PDFs einlesen:
- src/read_pdf.py: Liest alle PDFs ein, bereinigt den Text und speichert Chunks in chunks.json
3. Embeddings und Index erstellen:
- src/build_index.py: Wandelt Chunks in Vektor-Embeddings um und erstellt einen FAISS-Index für eine schnelle Suche
4. RAG-Anwendung starten:
- scr/app.py: Started das Webinterface Gradio
- Wenn der User eine Frage eingibt, dann wird eine Antwort aus dem LLM mit Kontext aus den PDFs erstellt

## Funktionsweise
- Chunking: PDFs werden in kleine Textabschnitte geteilt
- Embeddings: Jeder Textabschnitt wird in einen Vektor umgewandelt
- FAISS: Schnelle Suche nach den Texten, die zu den jeweils gestellten Fragen passen
- RAG: Kombination aus Suche (Retrieval) und Antwortgenerierung (Generation)
