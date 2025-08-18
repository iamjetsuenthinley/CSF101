name= "Jetsuen Thinley"
age=19
height=1.70
is_student=True

personal_info={
    "Name": name,
    "Age": age,
    "Height": height,
    "Is_Student": is_student
}
print(personal_info)

personal_info["Favourite_colour"]= "Red"
print(personal_info)

try:
    print(personal_info["Weight"])
except KeyError as e:
    print(f"Error: {e}")