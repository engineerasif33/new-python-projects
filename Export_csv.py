import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Asif", 22, "Lahore"])
    writer.writerow(["Sara", 20, "Islamabad"])
    writer.writerow(["Ahmed", 25, "Karachi"])

print("Student data saved successfully.")