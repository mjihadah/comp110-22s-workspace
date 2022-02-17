"""An example of for in syntax."""

names: list[str] = ["Melia", "Jalen", "Rayna", "Madison"]

print("While output:")
# Example of iterating through names using a while loop
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("For...in output:")
# The following for...in loop is the same as the while loop above
for name in names:
    print(name)