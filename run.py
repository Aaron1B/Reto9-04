import gradio as gr
from hanoi.ui import ui as hanoi_ui

def main():
    with gr.TabbedInterface([hanoi_ui()], ["Torres de Hanoi"]) as app:
        app.launch()

if __name__ == "__main__":
    main()
