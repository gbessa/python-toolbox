print("""
===========================
    Start of the Program
===========================""")

print("\nTypes:")
diff_types_list = [1, 1.0, "Hi", True, [1, 2], {1: "Name"}]

for diff_type in diff_types_list:
    print(type(diff_type))

print("\nList:")
names_list = ["Luis", "Miguel", "João", "Maria", "Ana"]
for name in names_list:
    print(f"Hello, World, {name}!")

surnames_list = []
surnames_list.append("Bessa")
surnames_list.append("Silva")
for surname in surnames_list:
    print(f"Hello, World, {surname}!")

print("\nDict:")
names_dict = {3: "Luis", 1: "Miguel", 2: "João", 5: "Maria", 4: "Ana"} # {key : value,...}
for index, name in names_dict.items():
    print(f"{index}. Hello, World, {name}!")

print("\nDict Sorted:")
for index, name in sorted(names_dict.items()):
    print(f"{index}. Hello, World, {name}!")