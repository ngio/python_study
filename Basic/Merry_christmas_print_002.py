message = "Merry Christmas"
message_length = len(message)
index = 0

for row in range(7):  # Number of rows for the heart
    for col in range(25):  # Width of the heart
        # Define the heart shape using a formula
        if (
            (row == 0 and (col >= 4 and col <= 9 or col >= 15 and col <= 20)) or
            (row == 1 and (col >= 2 and col <= 22)) or
            (row == 2 and (col >= 1 and col <= 23)) or
            (row == 3 and (col >= 0 and col <= 24)) or
            (row == 4 and (col >= 2 and col <= 22)) or
            (row == 5 and (col >= 4 and col <= 20)) or
            (row == 6 and (col >= 7 and col <= 17))
        ):
            print(message[index % message_length], end="")
            index += 1
        else:
            print(" ", end="")
    print()  # Move to the next row
