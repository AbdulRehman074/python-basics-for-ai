"""
📘 Study Notes Manager
Author: Abdulrehman
Description:
A simple Python file-handling mini project to create, read, and manage study notes.
"""

import os

FILENAME = "notes.txt"

def create_note():
    """Create or append a note to the file."""
    note = input("✏️ Enter your note: ")
    with open(FILENAME, "a") as file:
        file.write(note + "\n")
    print("✅ Note saved successfully!")

def view_notes():
    """View all saved notes."""
    if not os.path.exists(FILENAME):
        print("⚠️ No notes found. Create one first!")
        return
    with open(FILENAME, "r") as file:
        content = file.read()
        if content.strip() == "":
            print("📂 No content yet.")
        else:
            print("\n🧠 Your Notes:")
            print("-" * 30)
            print(content)
            print("-" * 30)

def delete_notes():
    """Delete all notes after confirmation."""
    if not os.path.exists(FILENAME):
        print("⚠️ No notes file to delete.")
        return
    confirm = input("⚠️ Are you sure you want to delete all notes? (yes/no): ").lower()
    if confirm == "yes":
        open(FILENAME, "w").close()
        print("🗑️ All notes deleted successfully!")
    else:
        print("❌ Deletion cancelled.")

def main():
    """Main menu loop."""
    while True:
        print("\n====== 📓 Study Notes Manager ======")
        print("1️⃣  Create a new note")
        print("2️⃣  View all notes")
        print("3️⃣  Delete all notes")
        print("4️⃣  Exit")

        choice = input("\n👉 Enter your choice (1-4): ")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("👋 Exiting... Have a productive study session!")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    main()
