"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)

if response == 0:
    print("Most definitely")
elif response == 1:
    print("Highly likely")
elif response == 2:
    print("Ask again later")
else:
    print("No way, not a chance")