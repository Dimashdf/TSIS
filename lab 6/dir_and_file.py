#EXercises 1 ;
def show_directories(path : str) -> str :
    from os import listdir
    print(listdir(path))

show_directories("C:\\")


show_directories("C:\\Study\\")

#Exercises 2;
import os

class File_properties:
    def __init__(self, path) -> None:
        self.path = path

    def does_exist(self) -> str:
        return os.path.exists(self.path)

    def is_readible(self) -> bool:
        return os.access(self.path, os.R_OK)
    
    def is_writable(self) -> bool:
        return os.access(self.path, os.W_OK)
    
    def is_executable(self) -> bool:
        return os.access(self.path, os.X_OK)
    
    def properties(self) -> str:
        if(os.path.exists(self.path)):
            print(f"""File is{"not" if not File_properties.is_readible else ""} readible
File is{"not" if not File_properties.is_writable else ""} writable
File is{"not" if not File_properties.is_executable else ""} executable""")
        else:
            print("File does not exist...")

class_object = File_properties("C:\\Study\\Database_user_inf\\AusUniversum.txt")
class_object.properties()

class_object = File_properties("C:\\Study\\Database_user_inf\\AusUniversum")
class_object.properties()

#Exercises 3;
def does_file_exist(file_path : str) -> str:
    from os import path
    
    if path.exists(file_path):
        filename = path.basename(file_path)
        directory = path.dirname(file_path)
        print(f"Filename: {filename}\nDirectory: {directory}")
    else:
        print(f"Given path ({file_path}) does not exist")

does_file_exist("C:\\Study\\repos")
does_file_exist("C:\\Study\\c++")

#Exercises 4;
def how_much_lines_in_text(path : str) -> int:
    line_count = 0

    file = open(path, "r")
    for line in file:
        line_count += 1

    file.close()

    return line_count

print(f"There is {how_much_lines_in_text('file_1.txt')} lines in text")
print(f"There is {how_much_lines_in_text('file_2.txt')} lines in text")

#Exercises 5;
def write_a_list_in_file(path : str, some_list : list) -> None:
    file = open(path, "a")
    try:
        file.write("".join([x for x in some_list]) + '\n')
        print("List has been written")
    except Exception as e:
        print(f"Error: {e}")

    file.close()

    return None

write_a_list_in_file("file_to_write.txt", "[1 2 3 4 5 6]")

#Exercises 6;
def create_a_file() -> None:
    import string
    import os
    letters_A_to_Z = string.ascii_uppercase
    path_to_folder = "C:/Study/repos/python/TSIS_6/Files_and_Directories_manipulation/A-Z_files"

    for i in letters_A_to_Z:
        file_path = os.path.join(path_to_folder, f"{i}.txt")
        file = open(file_path, "w")

    return None

create_a_file()

#Exercises 7;
def copy_to_another(first_file_path : str, second_file_path : str) -> None:
    file_1 = open(first_file_path, "r")
    file_2 = open(second_file_path, "a")
    try:
        text_to_write = file_1.read()
        file_2.write(text_to_write + ' ')
        print("File has been written")
    except Exception as e:
        print(f"Error: {e}")


    file_1.close(), file_2.close()

    return None

copy_to_another("Copy_file.txt", "Write_file.txt")

#Exercises 8;
def delete_file(file_path : str) -> None:
    import os

    if os.path.exists(file_path):
        print("File exist.")
        if os.access(file_path, os.W_OK):
            print("File is accessible.")
            try:
                os.remove(file_path)
                print("File is deleted.")
            except Exception as e:
                print(f"Could not delete the file.\nError: {e}")
        else:
            print("File is not accessible.")
    else:
        print("File does not exist.")

    return None

delete_file("C:/Study/repos/python/TSIS_6/Files_and_Directories_manipulation/file_to_delete.txt")
delete_file("C:/Study/repos/python/TSIS_6/Files_and_Directories_manipulation/Not_existing_file.txt")

