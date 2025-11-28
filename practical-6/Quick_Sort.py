def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x['total_score'] > pivot['total_score']]
        middle = [x for x in arr if x['total_score'] == pivot['total_score']]
        right = [x for x in arr if x['total_score'] < pivot['total_score']]
        return quicksort(left) + middle + quicksort(right)


students = [
    {"name": "Alice", "total_score": 385},
    {"name": "Bob", "total_score": 350},
    {"name": "Charlie", "total_score": 400},
    {"name": "David", "total_score": 395},
    {"name": "Eve", "total_score": 355}
]

print("Original order:")
for student in students:
    print(f"{student['name']}: {student['total_score']}")

sorted_students = quicksort(students)

print("\nRanked order:")
for rank, student in enumerate(sorted_students, 1):
    print(f"Rank {rank}: {student['name']} - {student['total_score']}")
