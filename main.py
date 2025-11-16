def open_file(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


file1_name = "TF2_1.txt"
file2_name = "TF2_2.txt"

file_1w = open_file(file1_name, "w")

if file_1w is not None:
    file_1w.write("Group KN-42 has 28 students in 2025 year.\n")
    file_1w.write("In clasroom 310 there are 125 computers.\n")
    file_1w.write("The exam will start at 0900 and finish at 1130.\n")

    print("Information was successfully written to", file1_name, "!")
    file_1w.close()
    print("File", file1_name, "was closed!")


file_2r = open_file(file1_name, "r")
file_2w = open_file(file2_name, "w")

if file_2r is not None and file_2w is not None:
    text = file_2r.read()

    numbers = []
    for word in text.replace(",", " ").replace(".", " ").split():
        if word.isdigit() and len(word) > 2:
            numbers.append(word)

    file_2w.write(" ".join(numbers))

    print("Sequences of digits longer than two were written to", file2_name, "!")
    file_2r.close()
    file_2w.close()
    print("Files were closed!")


print("Content of", file2_name, ":")
file_3r = open_file(file2_name, "r")

if file_3r is not None:
    print(file_3r.read())
    file_3r.close()
    print("File", file2_name, "was closed!")