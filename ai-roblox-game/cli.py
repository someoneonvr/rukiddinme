import sys
import argparse
from dispatcher import Dispatcher

def create_task(agent_type, description):
    """
    Function to create a task in the format that the dispatcher can handle.
    """
    task = {
        "agent": agent_type,
        "description": description
    }
    return task

def run_dispatcher(tasks):
    """
    Run the dispatcher with the provided tasks.
    """
    dispatcher = Dispatcher()
    results = dispatcher.dispatch(tasks)
    for result in results:
        print(result)

def main():
    """
    Main CLI logic.
    """
    parser = argparse.ArgumentParser(description="AI Game Development CLI")
    
    # Command to create a task
    parser.add_argument(
        "--create-task", 
        help="Create a new task for a specific agent",
        nargs=2, 
        metavar=("agent", "description"),
        dest="task"
    )
    
    # Command to run the dispatcher
    parser.add_argument(
        "--run", 
        help="Run the dispatcher with the provided tasks", 
        action="store_true"
    )
    
    args = parser.parse_args()

    # If no task is provided, notify the user
    if not args.task:
        print("No task provided. Use --create-task to specify a task.")
        sys.exit(1)
    
    agent_type, description = args.task
    task = create_task(agent_type, description)

    # Print the task to confirm it was created
    print(f"Created task for agent '{agent_type}': {description}")
    
    tasks = [task]

    # If the --run flag is provided, dispatch the task
    if args.run:
        print("Running dispatcher with the created task...")
        run_dispatcher(tasks)

if __name__ == "__main__":
    main()
