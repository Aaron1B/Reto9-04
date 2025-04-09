import gradio as gr
from .game import HanoiGame

def start_hanoi(num_disks):
    game = HanoiGame(num_disks)
    game.solve()
    # Obtener los nodos de la base de datos
    moves = game.get_all_moves_from_db()
    moves_text = "\n".join([f"Movimiento {move.move_number}: {move.from_peg} -> {move.to_peg}" for move in moves])
    return f"Se resolvieron {len(moves)} movimientos.\n\n{moves_text}"

def ui():
    with gr.Blocks() as demo:
        gr.Markdown("### Torres de Hanoi")
        num_disks_input = gr.Number(label="Número de discos", value=3)
        start_button = gr.Button("Iniciar Juego")
        output_box = gr.Textbox(label="Movimientos realizados", lines=10)
        
        start_button.click(start_hanoi, inputs=[num_disks_input], outputs=[output_box])

    return demo
