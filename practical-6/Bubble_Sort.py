def bubble_sort(scores):
    n = len(scores)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
                swapped = True
        if not swapped:
            break
    return scores

student_scores = [78, 65, 90, 82, 70, 88, 85]

print("Original scores:", student_scores)
sorted_scores = bubble_sort(student_scores)
print("Sorted scores:", sorted_scores)

rankings = {score: rank for rank, score in enumerate(sorted(set(sorted_scores), reverse=True), 1)}
student_rankings = [rankings[score] for score in student_scores]

print("Student rankings:", student_rankings)
