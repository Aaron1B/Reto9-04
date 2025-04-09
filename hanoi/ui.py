import gradio as gr
from .game import Hanoi

game_instance = None

def start_game(num_disks):
    global game_instance
    game_instance = Hanoi(num_disks)
    return f"Juego iniciado con {num_disks} discos.", format_towers(game_instance.get_state())

def make_move(from_tower, to_tower):
    global game_instance
    if not game_instance:
        return "Inicia el juego primero.", []

    success, msg = game_instance.move(from_tower, to_tower)
    if game_instance.is_completed():
        msg += " ¡Has completado el juego!"
    return msg, format_towers(game_instance.get_state())


def ui():
    with gr.Blocks() as demo:
        gr.Markdown("### Torres de Hanoi")

        num_disks = gr.Slider(3, 6, value=3, step=1, label="Número de Discos")
        start_btn = gr.Button("Iniciar Juego")
        state_output = gr.Textbox(label="Estado de las Torres", lines=10)

        message_output = gr.Textbox(label="Mensaje")

        with gr.Row():
            from_tower = gr.Number(label="Desde Torre (0-2)", value=0)
            to_tower = gr.Number(label="Hacia Torre (0-2)", value=2)

        move_btn = gr.Button("Mover Disco")

        start_btn.click(start_game, inputs=[num_disks], outputs=[message_output, state_output])
        move_btn.click(make_move, inputs=[from_tower, to_tower], outputs=[message_output, state_output])

    return demo

def format_towers(towers):
    output = ""
    max_height = max(len(t) for t in towers)
    for level in reversed(range(max_height)):
        for tower in towers:
            if len(tower) > level:
                output += f"  {tower[level]}  "
            else:
                output += "     "
        output += "\n"
    output += " [0]  [1]  [2] "
    return output

