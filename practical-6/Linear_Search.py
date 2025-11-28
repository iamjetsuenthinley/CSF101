def find_student(student_ids, target_id):
    for i, student_id in enumerate(student_ids, start=1):
        if student_id == target_id:
            return f"Student with ID {target_id} is present at position {i}."
    return f"Student with ID {target_id} is not present in the class."

class_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
target_student = 1005

result = find_student(class_ids, target_student)
print(result)

missing_student = 1010
result = find_student(class_ids, missing_student)
print(result)
