# PROJECT 4 – EXAMINATION RESULT AND GRACE-MARK VALIDATION

## About the Project
The Examination Result and Grace-Mark Validation project is designed to evaluate a student's marks across multiple subjects and apply a controlled grace-mark rule for single-subject borderline failures. After moderation, it computes total marks, percentage, and final division classification.

## Technologies Used
- **Python** – Used to develop the marks evaluation and grace-mark logic.
- **Lists** – Used to store subject marks and track failed subject indices.
- **Loops** – Used to collect subject marks and check pass status across subjects.
- **Conditional Statements** – Used to apply grace marks and assign result classifications.
- **Built-in Functions** – Used for clamping mark bounds and computing totals.

## Main Features
- Accepts student name, subject count, and marks for each subject.
- Clamps subject marks within the valid `0–100` range.
- Awards up to 5 grace marks to bring a single failed subject up to `40` when needed.
- Calculates total marks, percentage, and final status (`Distinction`, `First Class`, `Second Class`, or `Fail`).

## Algorithm
1. Start the program.
2. Read student name and number of subjects.
3. Read marks for each subject and clamp values between `0` and `100`.
4. Find all subject indices where marks are below `40`.
5. If exactly one subject is below `40` and needs `<= 5` marks to reach `40`, add the required grace marks.
6. Check whether all subjects have marks `>= 40`.
7. Calculate total marks and percentage.
8. Determine final status (`Fail`, `Pass - Distinction`, `Pass - First Class`, or `Pass - Second Class`).
9. Display the examination result card.
10. Stop the program.

## Sample Output
Enter student name: Divya
Enter number of subjects: 4
Enter marks for Subject 1 (out of 100): 82
Enter marks for Subject 2 (out of 100): 76
Enter marks for Subject 3 (out of 100): 37
Enter marks for Subject 4 (out of 100): 69

----- EXAMINATION RESULT CARD -----
Student Name     : Divya
Final Marks      : [82, 76, 40, 69]
Grace Marks Used : 3
Total & Percent  : 267 / 400 (66.75%)
Final Status     : PASS - FIRST CLASS

## Conclusion
This project automates subject-wise mark moderation and academic classification cleanly. It demonstrates Python concepts such as lists, loops, conditional statements, and built-in functions.
