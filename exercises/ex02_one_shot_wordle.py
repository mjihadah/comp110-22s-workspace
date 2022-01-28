"""Exercise 02: Wordles in one try!"""

__author__ = "730307805"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
user_guess: str = input(f"What is your {len(secret)}-letter guess? ")
i: int = 0
emoji: str = ""

while len(user_guess) != len(secret):
    user_guess = input(f"That was not {len(secret)} letters! Try again: ")

while i < len(user_guess):
    if user_guess[i] == secret[i]:
        emoji = emoji + GREEN_BOX
    else:
        exists = False
        alt: int = 0
        while not exists and alt < len(user_guess):
            if user_guess[i] == secret[alt]:
                exists = True
            else:
                alt += 1
        if exists:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    i = i + 1
print(emoji)

if user_guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")