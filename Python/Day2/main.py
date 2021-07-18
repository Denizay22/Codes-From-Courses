# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

lower_name1name2 = name1.lower() + name2.lower()

perc1 = 0
perc2 = 0

perc1 += lower_name1name2.count("t")
perc1 += lower_name1name2.count("r")
perc1 += lower_name1name2.count("u")
perc1 += lower_name1name2.count("e")

perc2 += lower_name1name2.count("l")
perc2 += lower_name1name2.count("o")
perc2 += lower_name1name2.count("v")
perc2 += lower_name1name2.count("e")

perc = int(str(perc1) + str(perc2))

if perc < 10 or perc > 90:
    print(f"Your score is {perc}, you go together like coke and mentos.")
elif 40 < perc < 50:
    print(f"Your score is {perc}, you are alright together.")
else:
    print(f"Your score is {perc}")
