name = "Nikita"
surname = "Matlaiev"
age = 17
HW = "Hello World"

types_list = [type(name), type(surname), type(age), type(HW)]

# Виводимо список типів
print("Список типів:", types_list)

if all(t == types_list[0] for t in types_list):
    print("Good")
else:
    most_common_type = max(set(types_list), key=types_list.count)
    filtered_list = [t for t in types_list if t == most_common_type]
    print("Список після видалення:", filtered_list)
