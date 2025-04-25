AGENT_CLASSES = {}

def register_agent(name, cls):
    AGENT_CLASSES[name] = cls

def get_agent(name):
    return AGENT_CLASSES.get(name)
