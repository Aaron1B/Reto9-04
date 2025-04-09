import gradio as gr
from hanoi.ui import ui as hanoi_ui 
from knight.ui import ui as knight_ui  
from nqueens.ui import ui as nqueens_ui 
with gr.Blocks() as app:
    gr.Markdown("## Juegos Automatizados")

    with gr.Tab("Torres de Hanoi"):
        hanoi_ui()  

    with gr.Tab("Recorrido del Caballo"):
        knight_ui()  
    with gr.Tab("Problema de las Reinas"):
        nqueens_ui()  
app.launch()
