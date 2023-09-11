# FileNotFound Error
# with open("a_file.txt") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    value = a_dict["blah"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("blah")
except KeyError as error:
    print(f"The key {error} does not exist")
else:
    content = file.read()
# finally:
    # anything here will run no matter what

# Key Error
# a_dict = {"key": "value"}
# value = a_dict["blah"]

# IndexError
# fruit_list = ["blah", "derp", "durka"]
# fruit = fruit_list[3]

# Type Error
# text = "abc"
# print(text + 5)

