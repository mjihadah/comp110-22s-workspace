"""An example of a while loop statement."""

counter: int = 0
maximum: int = int(input("Count up to, but not including, what? "))
while counter < maximum:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1 
    # counter necessary because the loop needs to make progress in order to eventually stop

print("Done!")