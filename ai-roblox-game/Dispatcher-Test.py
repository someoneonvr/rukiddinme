from dispatcher import Dispatcher

def main():
    dispatcher = Dispatcher()

    tasks = [
        {"agent": "environment", "description": "Create a volcanic island level"},
        {"agent": "ui", "description": "Design a sci-fi health bar and ammo counter"},
        {"agent": "combat", "description": "Make a non-animated swordfight system"},
        {"agent": "scripting", "description": "Add a level-up mechanic"},
        {"agent": "shader", "description": "Build a lava glow shader"},
        {"agent": "model", "description": "Create a spaceship with modular parts"},
        {"agent": "animation", "description": "Animate a lava monster"},
        {"agent": "something_weird", "description": "This will throw an agent not found"}
    ]

    results = dispatcher.dispatch(tasks)

    for result in results:
        print("\n--- RESULT ---")
        print(result)

if __name__ == "__main__":
    main()
