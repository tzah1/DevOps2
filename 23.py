current_name = input("Enter your current name: ")
while current_name != "quit":
    print (f"Hello, {current_name}!")
    if current_name == "tzah":
        continue
        current_name = input("Enter your current name: ")
    if current_name == "liron":
        break
        print(f"Hello, {current_name}!")
        current_name = input("Enter your current name: ")
    current_name = input("Enter your current name: ")
else:
    print("thanks for playing!")

