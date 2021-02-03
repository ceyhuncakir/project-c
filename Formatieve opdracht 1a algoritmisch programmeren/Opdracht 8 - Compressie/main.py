#test het met de bestandjes

def compressie():
    with open("read.txt", "r") as file1:
        file1_lines = file1.readlines()

    with open("write.txt", "w") as file2:
        for i in range (len(file1_lines)):
            file2.write(file1_lines[i].lstrip(" \t\n"))

compressie()
