import ollama

class CSGOAgent:
    """Agent for playing Counter-Strike: Global Offensive."""
    
    def __init__(self):
        pass
    
    def decide_action(self, game_state: str):
        """Decide next action based on game state."""
        prompt = f"""You are a CS:GO agent. Current game state: {game_state}
        
Decide the best action (movement, shooting, utility, positioning) to maximize win probability."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"action": response['message']['content']}
