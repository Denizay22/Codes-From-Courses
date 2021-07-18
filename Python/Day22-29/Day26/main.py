import random
import pandas
numbers = [1, 2, 3]
square = [n ** 2 for n in numbers]
print(square)
# -------------------------
names = ["asda", "qwdfgdfge", "zqwexc", "fsgh"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# -------------------------
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = [n for n in numbers if n % 2 == 1]
print(odd_numbers)

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list if test}
# new dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["asda", "qwdfgdfge", "zqwexc", "fsgh"]
scores = {student: random.randint(1, 100) for student in names}
print(scores)
passed_scores = {student: score for (student, score) in scores.items() if score > 60}
print(passed_scores)

# -------------------------
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_length = {word: len(word) for word in sentence.split()}
print(words_length)

# -------------------------


student_dict = {
    "student": ["Deno", "Mezo", "Asd"],
    "score": [50, 60, 70]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row)  # <----- panda.Series object
    print(row.student)
    print(row.score)

# there is a lot more ways to iterate over pandas dataframe:
# https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
