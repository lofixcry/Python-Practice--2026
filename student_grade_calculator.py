name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)

if average >= 50:
    print("Status: PASS")
else:
    print("Status: FAIL")
