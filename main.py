import os
print("current folder:",os.getcwd())
file_name = input("Enter file name (example: data.txt): ")

while True:
    
    print("\n========== File Management ==========")
    print("1. Create File")
    print("2. Write File")
    print("3. Append File")
    print("4. Read File")
    print("5. Delete File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Create file
        try:
            with open(file_name, "w") as file:
                pass
            print("File created successfully!")

        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        # Write file
        try:
            text = input("Enter text to write: ")

            with open(file_name, "w") as file:
                file.write(text + "\n")

            print("Data written successfully!")

        except Exception as e:
            print("Error:", e)

    elif choice == "3":
        # Append file
        try:
            text = input("Enter text to append: ")

            with open(file_name, "a") as file:
                file.write(text + "\n")

            print("Data appended successfully!")

        except Exception as e:
            print("Error:", e)

    elif choice == "4":
        # Read file
        try:
            with open(file_name, "r") as file:
                data = file.read()

            print("\n----- File Content -----")
            print(data)

        except FileNotFoundError:
            print("File not found!")

        except Exception as e:
            print("Error:", e)

    elif choice == "5":
        # Delete file
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                print("File deleted successfully!")
            else:
                print("File not found!")

        except Exception as e:
            print("Error:", e)

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Please try again.")
        