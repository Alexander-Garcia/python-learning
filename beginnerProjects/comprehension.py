import random

names = ["Jack", "Hendrix", "Clapton", "John"]
# list comprehension
numbers = [n for n in range(10)]
print(numbers)

# dictionary comprehension
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# dictionary comprehension with conditional
pass_students = {student: score for (student, score) in student_scores.items() if score > 50}
print(pass_students)

# dict comprehension challenge 
# create dict where each word is a key and value is number of chars
sentence = "What is the Airspeed Velocity of a Unladen Swallow"
chars_dict = {word: len(word) for word in sentence.split(" ")}
print(chars_dict)

# dict challenge 2
# convert to new dict where temps are F
# conversion - temp_c * 9/5 + 32
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# dict.items() returns a view object which is a list of tuples [(k, v), ...]
# print(weather_c.items())
