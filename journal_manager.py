"""
File Operator - Personal Journal Manager
----------------------------------------
A menu-driven console application that stores journal entries in a plain
text file (journal.txt). Demonstrates:
  * File handling (modes r, w, a, x)
  * Exception handling (FileNotFoundError, PermissionError, ...)
  * Object-Oriented Programming (JournalManager class)
"""

import os
from datetime import datetime


class JournalManager:
    """Encapsulates all journal functionality: file handling and exception handling."""

    TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # ------------------------------------------------------------------ helpers
    def _format_entry(self, text, timestamp=None):
        """Return an entry string: '[timestamp]\\ntext\\n\\n'."""
        timestamp = timestamp or datetime.now().strftime(self.TIMESTAMP_FORMAT)
        return f"[{timestamp}]\n{text}\n\n"

    def _read_entries(self):
        """Read the file (mode 'r') and return a list of entries (each a string).

        Raises FileNotFoundError if the journal file does not exist.
        """
        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
        if not content:
            return []
        return [block.strip() for block in content.split("\n\n") if block.strip()]

    # --------------------------------------------------------------- operations
    def add_entry(self, text):
        """Add a new entry.

        Mode 'x' (exclusive create) is tried first - it creates the file and
        fails with FileExistsError if it is already there. In that case we fall
        back to mode 'a' (append) so existing entries are preserved.
        """
        entry = self._format_entry(text)
        try:
            try:
                with open(self.filename, "x", encoding="utf-8") as file:
                    file.write(entry)
            except FileExistsError:
                with open(self.filename, "a", encoding="utf-8") as file:
                    file.write(entry)
            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")
        except OSError as error:
            print(f"Error: Could not write to the journal file ({error}).")

    def view_entries(self):
        """Display all entries (mode 'r')."""
        try:
            entries = self._read_entries()
        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
            return
        except PermissionError:
            print("Error: Permission denied. Cannot read the journal file.")
            return
        except OSError as error:
            print(f"Error: Could not read the journal file ({error}).")
            return

        if not entries:
            print("No journal entries found. Start by adding a new entry!")
            return

        print("Your Journal Entries:")
        print("-" * 33)
        for entry in entries:
            print(entry + "\n")

    def search_entries(self, keyword):
        """Search for a keyword or a date (case-insensitive) in all entries."""
        try:
            entries = self._read_entries()
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
            return
        except PermissionError:
            print("Error: Permission denied. Cannot read the journal file.")
            return
        except OSError as error:
            print(f"Error: Could not read the journal file ({error}).")
            return

        matches = [e for e in entries if keyword.lower() in e.lower()]
        if matches:
            print("Matching Entries:")
            print("-" * 33)
            for entry in matches:
                print(entry + "\n")
        else:
            print(f"No entries were found for the keyword: {keyword}.")

    def delete_all_entries(self):
        """Delete the journal file after asking the user for confirmation."""
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        choice = input("\nAre you sure you want to delete all entries? (yes/no): ")
        choice = choice.strip().lower()
        if choice == "yes":
            try:
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            except PermissionError:
                print("Error: Permission denied. Cannot delete the journal file.")
            except FileNotFoundError:
                print("No journal entries to delete.")
            except OSError as error:
                print(f"Error: Could not delete the journal file ({error}).")
        else:
            print("\nDeletion cancelled. Your entries are safe.")


# ------------------------------------------------------------------------- UI
MENU = """
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
"""


def main():
    manager = JournalManager("journal.txt")
    print(MENU)

    while True:
        try:
            choice = input("User Input:\n").strip()

            if choice == "1":
                text = input("\nEnter your journal entry:\n").strip()
                if text:
                    manager.add_entry(text)
                else:
                    print("Error: Entry cannot be empty.")
            elif choice == "2":
                print()
                manager.view_entries()
            elif choice == "3":
                keyword = input("\nEnter a keyword or date to search: ").strip()
                print()
                if keyword:
                    manager.search_entries(keyword)
                else:
                    print("Error: Search term cannot be empty.")
            elif choice == "4":
                manager.delete_all_entries()
            elif choice == "5":
                print("\nThank you for using Personal Journal Manager. Goodbye!")
                break
            else:
                print("\nInvalid option. Please select a valid option from the menu.")
        except (KeyboardInterrupt, EOFError):
            print("\n\nThank you for using Personal Journal Manager. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
