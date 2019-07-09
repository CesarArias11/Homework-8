
import os.path

fileName = str(input("Write the file name: ") + ".txt")


def options():
    print("A) Read the file\n")
    print("B) Delete the file and start over\n")
    print("C) Append the file\n")
    print("D) Replace a single line\n")
    choice = input("Select an option: ")
    return choice


def change_line():
    fl = open(fileName, "r").readlines()
    line_num = int(input("Which line would you like to edit? "))-1
    fl[line_num] = str(input("Write here your new line: ") + "\n")
    out_f = open(fileName, "w")
    out_f.writelines(fl)
    print("Line", line_num+1, "correctly changed.")
    out_f.close()


if os.path.isfile(fileName):
    print("File exist\n")
    get_choice = options()
    if get_choice == "A":
        file = open(fileName, "r")
        for line in file:
            print(line, end="")
        file.close()
    elif get_choice == "B":
        file = open(fileName, "w")
        while True:
            temp_inp = (input("Write for your file:\n"))
            file.write(str(temp_inp) + "\n")
            keep_on = str(input("Would you like to continue writing in your file? Yes/No\n"))
            if keep_on == "Yes":
                continue
            elif keep_on == "No":
                break
            else:
                keep_on = str(input("Would you like to continue writing in your file? Yes/No\n"))
        file.close()
    elif get_choice == "C":
        file = open(fileName, "a")
        while True:
            temp_inp = (input("Write for your file:\n"))
            file.write(str(temp_inp) + "\n")
            keep_on = str(input("Would you like to continue writing in your file? Yes/No\n"))
            if keep_on == "Yes":
                continue
            elif keep_on == "No":
                break
            else:
                keep_on = str(input("Would you like to continue writing in your file? Yes/No\n"))
        file.close()
    elif get_choice == "D":
        lines = len(open(fileName).readlines())
        print("This file has", lines, "lines.\n")
        change_line()
    else:
        print("Option does't exist")
else:
    print("File has just been created\n")
    file = open(fileName, "w")
    while True:
        temp_inp = (input("Write for your new file:\n"))
        file.write(str(temp_inp) + "\n")
        keep_on = str(input("Would you like to continue writing in your file? Yes/No\n"))
        if keep_on == "Yes":
            continue
        elif keep_on == "No":
            break
        else:
            keep_on = str(input("Would you like to continue writing in your file? Yes/No\n"))
    file.close()


