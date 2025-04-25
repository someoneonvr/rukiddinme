import queue
import threading
import uuid
from typing import Dict, Any, Callable

# -- Agent Profiles --
AGENT_PROFILES = {
    "ScriptingAI": {"receives": ["logic", "combat", "ui"], "produces": ["code"]},
    "ModelingAI": {"receives": ["model", "weapon", "character"], "produces": ["models"]},
    "AnimationAI": {"receives": ["animation", "combat"], "produces": ["animations"]},
    "ShaderAI": {"receives": ["shader", "lighting"], "produces": ["shaders"]},
    "EnvironmentAI": {"receives": ["terrain", "props"], "produces": ["environment"]},
    "CombatAI": {"receives": ["combat", "damage", "physics"], "produces": ["combat_logic"]},
    "UIAI": {"receives": ["ui", "hud"], "produces": ["interfaces"]},
    "FileManager": {"receives": ["code", "models", "animations", "shaders"], "produces": ["file_structures"]}
}

# -- Message Schema Template --
def create_message(sender: str, recipient: str, task_type: str, content: Dict[str, Any], priority: int = 1) -> Dict[str, Any]:
    return {
        "id": str(uuid.uuid4()),
        "sender": sender,
        "recipient": recipient,
        "task_type": task_type,
        "content": content,
        "priority": priority,
        "status": "queued"
    }

# -- CommunicationHub Class --
class CommunicationHub:
    def __init__(self):
        self.message_queue = queue.PriorityQueue()
        self.history = []
        self.listeners: Dict[str, Callable[[Dict[str, Any]], None]] = {}

    def register_agent(self, agent_name: str, handler: Callable[[Dict[str, Any]], None]):
        self.listeners[agent_name] = handler

    def send_message(self, message: Dict[str, Any]):
        print(f"Queueing message from {message['sender']} to {message['recipient']}")
        self.message_queue.put((message['priority'], message))
        self.history.append(message)

    def dispatch(self):
        while True:
            if not self.message_queue.empty():
                _, message = self.message_queue.get()
                recipient = message['recipient']
                if recipient in self.listeners:
                    try:
                        self.listeners[recipient](message)
                        message['status'] = 'delivered'
                    except Exception as e:
                        print(f"Failed to deliver message to {recipient}: {e}")
                        message['status'] = 'failed'
                        self.retry_message(message)
                else:
                    print(f"No listener registered for {recipient}, retrying later.")
                    self.retry_message(message)

    def retry_message(self, message: Dict[str, Any]):
        message['priority'] += 1
        self.message_queue.put((message['priority'], message))

    def start_dispatcher(self):
        threading.Thread(target=self.dispatch, daemon=True).start()

# Example usage (to be implemented in agents)
# def handle_script_message(message):
#     print(f"[ScriptingAI] Received: {message['content']}")

# hub = CommunicationHub()
# hub.register_agent("ScriptingAI", handle_script_message)
# hub.start_dispatcher()
# hub.send_message(create_message("Mastermind", "ScriptingAI", "logic", {"prompt": "Build Vader saber logic."}))
