name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = int(input(f"Enter marks for Subject {i + 1} (out of 100): "))
    marks.append(max(0, min(100, m)))

failed_indices = []
for i in range(n):
    if marks[i] < 40:
        failed_indices.append(i)

grace_used = 0
if len(failed_indices) == 1:
    idx = failed_indices[0]
    deficit = 40 - marks[idx]
    if deficit <= 5:
        marks[idx] = min(100, marks[idx] + deficit)
        grace_used = deficit

all_passed = True
for m in marks:
    if m < 40:
        all_passed = False

total = sum(marks)
percentage = total / n

if not all_passed:
    result = "FAIL"
elif percentage >= 75:
    result = "PASS - DISTINCTION"
elif percentage >= 60:
    result = "PASS - FIRST CLASS"
else:
    result = "PASS - SECOND CLASS"

print("\n----- EXAMINATION RESULT CARD -----")
print("Student Name     :", name)
print("Final Marks      :", marks)
print("Grace Marks Used :", grace_used)
print(f"Total & Percent  : {total} / {n * 100} ({percentage:.2f}%)")
print("Final Status     :", result)
