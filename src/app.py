import gradio as gr
from rag_app import rag_system

def answer_question(question):
    return rag_system(question)

ui = gr.Interface(
    #rag_app wird aufgerufen, sobald User eine Frage eingibt
    fn = answer_question,
    inputs = gr.Textbox(label = "Deine Frage", lines = 5, placeholder = "Deine Frage hier eingeben"),
    outputs = gr.Textbox(label = "Antwort", lines = 5, placeholder = "Antwort"),
    title = "Studienberater Uni Regensburg"
)

ui.launch()
