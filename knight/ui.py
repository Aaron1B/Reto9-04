import gradio as gr
from .game import KnightGame

def start_knight(num_moves):
    game = KnightGame(start_position=(0, 0))
    game.solve()

    # Obtener los nodos de la base de datos
    moves = game.get_all_moves_from_db()
    moves_text = ""
    
    for move in moves:
        moves_text += f"Movimiento {move.move_number} ({move.from_x}, {move.from_y}) -> ({move.to_x}, {move.to_y}). No posibilidades: {move.possibilities}\n"

    return f"Se realizaron {len(moves)} movimientos.\n\n{moves_text}"

def ui():
    with gr.Blocks() as demo:
        gr.Markdown("### Problema del Caballo (Ajedrez)")
        num_moves_input = gr.Number(label="Número de movimientos", value=10)
        start_button = gr.Button("Iniciar Juego")
        output_box = gr.Textbox(label="Movimientos realizados", lines=20)
        
        start_button.click(start_knight, inputs=[num_moves_input], outputs=[output_box])

    return demo
