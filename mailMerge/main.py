#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def read_names_file():
    with open(file="./Input/Names/invited_names.txt") as file:
        # list of names
        names = file.readlines()
        return names

def write_letter(person_invited, content):
    with open(file=f"./Output/ReadyToSend/{person_invited}.txt", mode="w") as letter:
        letter.write(content)

def open_letter_template():
    with open(file="./Input/Letters/starting_letter.txt") as letter_template:
        # read just first line where greeting is to be replace with name
        template = letter_template.read()
        names = read_names_file()
        for name in names:
            # remove the newline character
            stripped_name = name.strip("\n")
            # replace [name] in first line
            formatted_letter = template.replace("[name]", stripped_name)
            write_letter(person_invited=stripped_name, content=formatted_letter)
        

open_letter_template()
