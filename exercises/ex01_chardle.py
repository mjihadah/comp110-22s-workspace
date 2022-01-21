"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730307805"


five_letter_word: str = input("Enter a 5-character word: ")
if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters.")
    quit()
single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    print("Error: Character must be a single character.")
    quit()
matches: int = 0
print("Searching for " + single_char + " in " + five_letter_word)

if five_letter_word[0] == single_char: 
    print(single_char + " found at index 0.")
    matches = matches + 1
if five_letter_word[1] == single_char:
    print(single_char + " found at index 1.")
    matches = matches + 1
if five_letter_word[2] == single_char:
    print(single_char + " found at index 2.")
    matches = matches + 1
if five_letter_word[3] == single_char:
    print(single_char + " found at index 3.")
    matches = matches + 1
if five_letter_word[4] == single_char:
    print(single_char + " found at index 4.")
    matches = matches + 1

if matches == 0:
    print("No instances of " + single_char + " found in " + five_letter_word)
if matches == 1:
    print("1 instance of " + single_char + " found in " + five_letter_word)
else:
    print(str(matches) + " instances of " + single_char + " found in " + five_letter_word)
# variable 'matches' needs to count the number of matching characters, somehow, and use it to tell people how many instances of each character there are
# matches is initially zero... need to then add +1 every time there is a match.. HMMMMM HOW DO I COUNT THE MATCHES THOUGH
