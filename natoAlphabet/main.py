# TODO: read csv and create a dict
# { "A": "Alfa", "B": "Bravo"}
# TODO: Create a list of phonetic code words from a word the user inputs
import pandas

CSV_FILENAME = "nato_phonetic_alphabet.csv"

nato_file = pandas.read_csv(filepath_or_buffer=CSV_FILENAME)


# iterate through df and create dict
nato_dict = {row.letter: row.code for (_, row) in nato_file.iterrows()}

user_word = input("Enter a word to receive its phonetic code:\n ").upper()

phonetic_list = [nato_dict[letter] for letter in user_word]
print(phonetic_list)
