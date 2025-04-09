import gradio as gr
from .game import KnightTour

tour = None

def format_board(board):
    output = ""
    for row in board:
        output += " ".join(f"{cell:2}" if cell != -1 else "__" for cell in row) + "\n"
    return output

def start_knight_tour():
    global tour
    tour = KnightTour()
    solved = tour.solve()

    if not solved:
        return "No se pudo resolver el recorrido.", ""

    board_text = format_board(tour.get_board())
    moves_text = "\n".join(tour.get_move_list())
    count_text = f"Total de movimientos: {tour.get_move_count()}"

    full_output = f"{board_text}\n{count_text}\n\n{moves_text}"
    return "Recorrido del Caballo completado.", full_output

def ui():
    with gr.Blocks() as demo:
        gr.Markdown("### Problema del Caballo ♞ (Recorrido automático)")
        start_button = gr.Button("Iniciar Recorrido")
        msg_out = gr.Textbox(label="Resultado")
        output_box = gr.Textbox(label="Detalle del recorrido", lines=40)

        start_button.click(start_knight_tour, inputs=[], outputs=[msg_out, output_box])
    return demo
