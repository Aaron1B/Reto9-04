import gradio as gr
from .game import Hanoi

game_instance = None

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

def start_game(num_disks):
    global game_instance
    game_instance = Hanoi(num_disks)
    game_instance.solve()

    towers_text = format_towers(game_instance.get_state())
    history_text = "\n".join(game_instance.get_history())
    move_count = f"Total de movimientos: {game_instance.get_move_count()}"

    full_output = f"{towers_text}\n\n{move_count}\n\n{history_text}"
    return f"Resuelto con {num_disks} discos.", full_output

def ui():
    with gr.Blocks() as demo:
        gr.Markdown("### Torres de Hanoi Automático 🧠")

        num_disks = gr.Slider(1, 6, value=3, step=1, label="Número de Discos")
        start_btn = gr.Button("Resolver")
        message_output = gr.Textbox(label="Mensaje")
        state_output = gr.Textbox(label="Solución", lines=30)

        start_btn.click(start_game, inputs=[num_disks], outputs=[message_output, state_output])

    return demo
