full_name = input("Enter your full name:")

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]

print("Initials:", first_name[0] + ". " + last_name[0] + ".")
print("uppercase name:", full_name.upper())
print("Reserved name:", full_name[::-1])