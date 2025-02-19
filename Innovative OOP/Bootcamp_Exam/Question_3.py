List = ["Alice", "Bob", "Charlie", "David", "Eve"]
for i in List:
    v = i[:1]
    if v == "A" or v == "D":
        print(f"The Student name is: {i}")