try:
    text=input("Enter a short message: \n")
    with open("note.txt", "w") as file:
        file.write(text + "\n")

    print("\nNice! Your message has been saved")
    print()

except:
    print("There was an error while writing to the file.")

try:
    print("Content of the file: ")
    with open("note.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not Found!")

try:
    add_con = input("Enter a message here to be added to the file:\n")
    with open("note.txt", "a") as file:
        file.write(add_con + "\n")

    print("\nUpdated Message:")
    with open("note.txt", "r") as file:
        new_content = file.read()
        print(new_content)
except:
    print("There was an error while adding a content to the file.")
