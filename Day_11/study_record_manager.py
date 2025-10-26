# 🧠 Study Record Manager
# Author: Abdulrehman


import datetime

class Student:
    def __init__(self, name, study_hours, topics):
        self.name = name
        self.study_hours = study_hours
        self.topics = topics
        self.date = datetime.date.today()

    def record_summary(self):
        """Return a formatted study summary string."""
        return (f"📘 {self.name} studied {self.study_hours} hours today ({self.date}), "
                f"focusing on: {', '.join(self.topics)}")

    def save_to_file(self, filename="study_records.txt"):
        """Save the record to a text file."""
        with open(filename, "a") as f:
            f.write(self.record_summary() + "\n")
        print("✅ Record saved successfully!\n")


def add_record():
    name = input("Enter your name: ")
    study_hours = float(input("How many hours did you study today? "))
    topics = input("Enter topics studied (comma-separated): ").split(",")
    student = Student(name, study_hours, [t.strip() for t in topics])
    student.save_to_file()


def view_records(filename="study_records.txt"):
    """Display all saved study records."""
    try:
        with open(filename, "r") as f:
            records = f.readlines()
            if not records:
                print("No records found yet. Start by adding one!\n")
                return
            print("\n📚 Your Study Records:")
            for record in records:
                print(record.strip())
            print()
    except FileNotFoundError:
        print("No records file found. Try adding a record first!\n")


def main():
    while True:
        print("🧩 Study Record Manager")
        print("1️⃣ Add a new record")
        print("2️⃣ View all records")
        print("3️⃣ Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("👋 Goodbye! Keep learning daily 💪")
            break
        else:
            print("❌ Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
