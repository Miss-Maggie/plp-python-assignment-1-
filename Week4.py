file_edit = open("Week4.txt", "w")
data_edit = file_edit.write("Hello Maggie How are you ?")
file_edit.close()

file = input("Enter the file name: ")
try:
    file = open(file, "r")
    data = file.read()
    print(data)
    new_file = input("Enter the new_file name: ")
    searched_file = open(new_file, "w")
    # data_append = searched_file.write(data.replace(" ", "-"))
    data_append = searched_file.write(data.upper())
    searched_file.close()
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except Exception as e:
    print(f"An error occurred: {e}")

