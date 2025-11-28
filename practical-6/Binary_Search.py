def find_rank(scores, target_score):
    left, right = 0, len(scores) - 1

    while left <= right:
        mid = (left + right) // 2
        if scores[mid] == target_score:
            return len(scores) - mid  
        elif scores[mid] < target_score:
            right = mid - 1  
        else:
            left = mid + 1  

    return len(scores) - right


scores = [95, 90, 85, 80, 75, 70, 65, 60]  
student_score = 82

rank = find_rank(scores, student_score)
print(f"A student with a score of {student_score} would rank {rank} in the class.")
