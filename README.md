FILE OPERATOR - PERSONAL JOURNAL MANAGER
========================================

OVERVIEW
A menu-driven Python console application for keeping a personal journal in a
plain text file. It demonstrates file handling, exception handling and
Object-Oriented Programming (OOP).


FEATURES
1. Add a New Entry      - appends a timestamped entry to journal.txt
                          (creates the file if it does not exist)
2. View All Entries     - displays all entries from the file
3. Search for an Entry  - finds entries by keyword or date
4. Delete All Entries   - deletes the journal file after confirmation
5. Exit                 - closes the program

Every entry is saved with a timestamp. Example:

[2026-11-02 10:00:00]
Today was a productive day. I learned about file handling in Python.


PROJECT STRUCTURE
journal_manager.py   - Main program (JournalManager class and menu)
file_modes_demo.py   - Shows the difference between file modes r, w, a, x
demo_runner.py       - Runs scripted sessions to record the output
make_pdf.py          - Builds Project_Output.pdf from the recorded output
output.txt           - Recorded console output of the main program
modes_output.txt     - Recorded output of the file modes demo
Project_Output.pdf   - Project output in PDF format
journal.txt          - Created automatically when the first entry is added
README.txt           - This file


REQUIREMENTS
- Python 3.7 or newer
- No external libraries are needed for the main program
- reportlab is needed only to regenerate the PDF (pip install reportlab)


HOW TO RUN
python journal_manager.py            (start the Personal Journal Manager)
python file_modes_demo.py            (see file modes r, w, a, x in
