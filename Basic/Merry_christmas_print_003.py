message = "Merry Christmas"
message_length = len(message)
index = 0

# Adjust the heart dimensions for 30 lines
for row in range(30):  # Number of rows for the heart
    for col in range(61):  # Width of the heart (adjusted for proportions)
        # Define the heart shape using a mathematical formula
        x = col / 30 - 1  # Normalize col to range [-1, 1]
        y = 1 - row / 15  # Normalize row to range [-1, 1]

        # Heart formula: (x^2 + y^2 - 1)^3 - x^2 * y^3 <= 0
        if (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0:
            print(message[index % message_length], end="")
            index += 1
        else:
            print(" ", end="")
    print()  # Move to the next row
