import random

# Generate the computer's number
computer_number = str(random.randint(100, 999))

# Start the game
print("Welcome to the number baseball game!")
while True:
    user_guess = input("Enter your guess (3 digits): ")
    if user_guess == computer_number:
        print("Congratulations! You won the game!")
        break
    else:
        strike_count = 0
        ball_count = 0
        for i in range(3):
            if user_guess[i] == computer_number[i]:
                strike_count += 1
            elif user_guess[i] in computer_number:
                ball_count += 1
        print("Strikes:", strike_count, "Balls:", ball_count)