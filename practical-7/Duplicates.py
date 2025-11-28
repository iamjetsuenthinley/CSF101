def containsDuplicate(x):
    seen = set()
    for num in x:
        if num in seen:
            return True
        seen.add(num)
    return False
x=[1,2,3,4,5,6,7,7]
def containsDuplicate(x):
    seen = set()
    for num in x:
        if num in seen:
            return True
        seen.add(num)
    return False
x=[1,2,3,4,5,6,7,7]
print(containsDuplicate(x))