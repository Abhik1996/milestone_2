import random

favourite_fruit = ['apple', 'banana','grape','kiwi','avacado']

word_list = random.choice(favourite_fruit)
print(word_list)

###########task3#####################
# Step 1: Using the input function, ask the user to enter a single letter.
user_input = input("Please enter a single letter: ")

# Step 2: Assign the input to a variable called guess and convert to uppercase.
guess = user_input.upper()

# Print the entered letter in uppercase to verify.
print("You entered:", guess)

###########task4#####################
# Step 1: Using the input function, ask the user to enter a single letter.
user_input = input("Please enter a single letter: ")

# Step 2: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(user_input) == 1 and user_input.isalpha():
    # Step 2: In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    # Step 3: Create an else block that prints "Oops! That is not a valid input."
    print("Oops! That is not a valid input.")
