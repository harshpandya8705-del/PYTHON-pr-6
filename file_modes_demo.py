"""
Demonstrates the difference between file modes r, w, a and x
using a temporary file (demo_modes.txt).
"""

import os

FILE = "demo_modes.txt"


def show(label):
    with open(FILE, "r") as f:
        print(f"   File content after {label}: {f.read()!r}")


def main():
    if os.path.exists(FILE):
        os.remove(FILE)

    print("1. Mode 'x' - exclusive create (fails if file exists)")
    with open(FILE, "x") as f:
        f.write("Line 1\n")
    show("'x'")
    try:
        with open(FILE, "x") as f:
            f.write("never written\n")
    except FileExistsError:
        print("   Second 'x' open -> FileExistsError (file already exists)")

    print("\n2. Mode 'a' - append (keeps old data, adds at the end)")
    with open(FILE, "a") as f:
        f.write("Line 2\n")
    show("'a'")

    print("\n3. Mode 'r' - read (file must exist)")
    with open(FILE, "r") as f:
        print(f"   Read: {f.read()!r}")
    try:
        open("missing_file.txt", "r")
    except FileNotFoundError:
        print("   Opening a missing file with 'r' -> FileNotFoundError")

    print("\n4. Mode 'w' - write (OVERWRITES all existing content)")
    with open(FILE, "w") as f:
        f.write("Only this line remains\n")
    show("'w'")

    os.remove(FILE)


if __name__ == "__main__":
    main()
