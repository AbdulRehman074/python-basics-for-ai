def input_collection():
    name = str(input("Enter your name: "))
    study_hours = float(input("Study hours today: "))
    favorite_topic = input("Favorite topic: ")
    return name, study_hours, favorite_topic

def validate_hours(study_hours):
    if study_hours < 0:
        print("Invalid study hours. Please enter a non-negative value.")
        return False
    return True

def build_record(name, study_hours, favorite_topic):
    return f"✅ Summary: {name} studied {study_hours} hours today, focusing on {favorite_topic}."

def summary_string(record):
    return record  # record is already a summary string

def main():
    while True:
        name, study_hours, favorite_topic = input_collection()

        while not validate_hours(study_hours):
            study_hours = int(input("Study hours today: "))

        record = build_record(name, study_hours, favorite_topic)
        print(summary_string(record))

        another = input("Do you want to enter another record? (yes/no): ").lower()
        if another != "yes":
            print("Goodbye! Keep learning daily 💪")
            break

# Run main function
main()
