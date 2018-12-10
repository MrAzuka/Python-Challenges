# Write a small program to ask for a name and age
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31)
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("What is your name: ")
age = int(input("How old are you: "))

if (age >= 18) and (age < 31):
    print("{0}, your are eligible for the trip because you are {1} years old.". format(name, age))
    print("Welcome Aboard")
elif (age > 30):
    print("{0}, your to old for this trip.". format(name))
else:
    print("{0}, your aren't eligible for the trip because you are {1} years old.". format(name, age))
    print("Come back in {} years.". format(18 - age))



