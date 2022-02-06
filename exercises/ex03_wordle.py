"""Building a better-structured wordle."""

__author__ = "730307805"


def contains_char(any_length: str, single_char: str) -> bool:
    """Returns 'True' if the single character of second string is found at any index of the first string."""
    assert len(single_char) == 1
    i: int = 0
    while i < len(any_length):
        if single_char == any_length[i]:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis to codify the accuracy of the guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8" 
    emoji: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            exists = False
            if contains_char(secret, guess[i]) is True:
                exists = True
            if exists:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Given an expected length, prompt user for a guess of that length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")

    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entry point of the program and main game loop."""
    turns: int = 1
    won = True
    secret: str = "codes"
    while turns <= 6 and won:
        print(f"=== Turn {turns}/6 ===")
        # print(input_guess(len(secret)))
        input_tracker: str = input_guess(len(secret))
        print(emojified(input_tracker, secret))
        # print(emojified(input_guess(len(secret)), secret))
        if input_tracker == secret:
            won = False
        else:
            turns += 1
    if not won:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()   