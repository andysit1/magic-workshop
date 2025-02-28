import json
import os

SNAPSHOT_DIR = "snapshots"

class StateMachine:
    def __init__(self):
        os.makedirs(SNAPSHOT_DIR, exist_ok=True)
        self.history = sorted(os.listdir(SNAPSHOT_DIR))

    def save_state(self, files):
        """Save current file structure."""
        state_file = f"{SNAPSHOT_DIR}/state_{len(self.history)}.json"
        with open(state_file, "w") as f:
            json.dump(files, f, indent=4)
        self.history.append(state_file)

    def undo(self):
        """Revert to the previous state."""
        if len(self.history) < 2:
            print("No previous state to revert to.")
            return

        last_state = self.history.pop()
        prev_state = self.history[-1]

        with open(prev_state, "r") as f:
            files = json.load(f)

        # Restore files (simplified)
    for path, content in files.items():
            with open(path, "w") as f:
                f.write(content)

        print(f"Reverted to: {prev_state}")
