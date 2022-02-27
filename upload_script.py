import os.path

save_path = 'C:\\Users\\USER\\PycharmProjects\\DE-DUPLICATION'

name_of_file = input("What is the name of the file: ")

Name = os.path.join(save_path, name_of_file+".txt")

file1 = open(Name, "w")

toFile = input("Write what you want into the field:")

file1.write(toFile)

file1.close()