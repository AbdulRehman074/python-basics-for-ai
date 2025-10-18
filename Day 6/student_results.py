# student_results.py
# Developed by Abdulrehman
# Description: This program allows you to input multiple students' marks, calculate their average,
# grade their performance, and save the results in a text file automatically.

def input_student_data():
    """Takes input for multiple students and returns a list of student dictionaries."""
    num_students = int(input("How many students data you want to enter? "))
    students = []
    for i in range(num_students):
        name = input(f"\nEnter the name of student {i + 1}: ")
        marks = input(f"Enter the marks of {name} (comma-separated): ").split(",")
        students.append({"name": name, "marks": marks})
    return students


def calculate_average(marks):
    """Calculates average marks from a list of marks (strings)."""
    total = sum(map(int, marks))
    return total / len(marks)


def display_results(students):
    """Displays results and returns a list of formatted result strings."""
    results = []
    for student in students:
        average = calculate_average(student["marks"])
        if average >= 80:
            status = "Excellent"
        elif average >= 60:
            status = "Good"
        else:
            status = "Needs Improvement"
        result_text = f"{student['name']}: Average = {average:.2f} → {status}"
        print(result_text)
        results.append(result_text)
    return results


def save_results_to_file(results, filename="student_results.txt"):
    """Saves results to a text file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write("----- New Batch -----\n")
        for line in results:
            file.write(line + "\n")
        file.write("\n")
    print(f"\n📁 Results have been saved to '{filename}' successfully!")


def main():
    """Main loop to input data, display results, and optionally repeat."""
    print("🎓 Welcome to the Student Result Calculator!\n")

    while True:
        students = input_student_data()
        print("\n--- Results ---")
        results = display_results(students)
        save_results_to_file(results)

        answer = input("\nDo you want to enter another batch? (yes/no): ").lower()
        if answer != "yes":
            print("\n✅ Goodbye! Keep learning daily 💪")
            break


if __name__ == "__main__":
    main()
