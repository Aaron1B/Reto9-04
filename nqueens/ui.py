import gradio as gr
from .game import NQueensGame

def ui():
    def start_game(n):
        game = NQueensGame(n)
        game.solve()  # Resuelve el problema de las N reinas
        moves_history = game.get_moves()
        
        # Convertimos los movimientos en una cadena para mostrar en la interfaz
        moves_str = "\n".join([f"Movimiento {move.move_number}:\n{move.board}" for move in moves_history])
        return moves_str
    
    interface = gr.Interface(fn=start_game, inputs="number", outputs="text", live=True)
    interface.launch()
