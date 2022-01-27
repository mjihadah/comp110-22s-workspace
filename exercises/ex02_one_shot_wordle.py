"""Exercise 02: Wordles in one try!"""

__author__ = "730307805"


secret: str = "python"
# need to implement f-string so that no matter what the secret word is, and no matter how long it is,
# the program will still work just the same.. I'm thinking that I need to use len(secret) 
# in the output so that it'll just use whatever length the secret word is in the prompt and everything else.
user_guess: str = input(f"What is your {len(secret)}-letter guess? ")
while len(user_guess) != len(secret):
    user_guess = input(f"That was not {len(secret)} letters! Try again: ")
if user_guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")