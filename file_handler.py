
import json
import csv
import os

JSON_FILE = "students.json"
CSV_FILE = "students.csv"


def load_students():
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError) as error:
            print("Error loading records:", error)

    return []


def save_students(students):
    try:
        with open(JSON_FILE, "w") as file:
            json.dump(students, file, indent=4)

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "name", "course", "marks"]
            )

            writer.writeheader()
            writer.writerows(students)

        print("Records saved successfully!")

    except OSError as error:
        print("File error:", error)
