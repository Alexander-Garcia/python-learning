# using with will allow python to close the file and free up resources without explicitly calling close()
with open(file="textFile.txt") as file:
    contents = file.read()
    print(contents)

# modes can be r - read, w -write, a - append
with open(file="textFile.txt", mode="a") as file:
    contents = file.write("\nTo sit with elders of the gentle race")
    print(contents)

# if files does not exist w will create the file
with open(file="created.txt", mode="w") as file:
    file.write("This world has seldom seen")
