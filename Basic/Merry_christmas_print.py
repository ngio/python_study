message = "Merry Christmas"
message_length = len(message)

for row in range(6):  # Number of rows for the heart
    for col in range(7):  # Number of columns for the heart
        if (
            (row == 0 and col % 3 != 0) or
            (row == 1 and col % 3 == 0) or
            (row == 2) or
            (row == 3 and col not in [0, 6]) or
            (row == 4 and col in [1, 2, 3, 4, 5])
        ):
            # Calculate character to print from the message
            char_index = (row * 7 + col) % message_length
            print(message[char_index], end="")
        else:
            print(" ", end="")
    print()  # Move to the next row
