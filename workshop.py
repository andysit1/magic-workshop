import sys
from file_organizer import FileOrganizer
from state_machine import StateMachine



def main():
    if len(sys.argv) < 2:
        print("Usage: python workshop.py <command>")
        return

    command = sys.argv[1]
    state_machine = StateMachine()
    organizer = FileOrganizer(state_machine)

    if command == "organize":
        organizer.organize()
    elif command == "move":
        organizer.move()
    elif command == "undo":
        state_machine.undo()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
