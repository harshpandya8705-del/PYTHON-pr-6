"""
Runs journal_manager.main() with scripted input so the full console
interaction can be recorded (saved to output.txt and used for the PDF).
Each scripted answer is echoed as if the user typed it.
"""
import builtins, os, sys
import journal_manager

def run_session(title, inputs):
    print(f"##### {title}")
    it = iter(inputs)
    def fake_input(prompt=""):
        value = next(it)
        print(prompt + value)
        return value
    builtins.input = fake_input
    journal_manager.main()
    print()

if __name__ == "__main__":
    if os.path.exists("journal.txt"):
        os.remove("journal.txt")
    run_session("Session 1: Errors when the file does not exist",
                ["2", "3", "productive", "4", "6", "5"])
    run_session("Session 2: Add, view, search and delete",
                ["1", "Today was a productive day. I learned about file handling in Python.",
                 "1", "Had a great session on OOP concepts!",
                 "2", "3", "productive", "3", "holiday",
                 "4", "no", "4", "yes", "2", "5"])
